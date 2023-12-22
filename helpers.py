import pandas as pd

def parse_reviews_to_pickle(path, output, is_first):

    all_reviews = list()
    review_dict = dict()

    with open(path) as infile:
        for i, line in enumerate(infile):
            if line == '\n':
                if not is_first and i < 80_000_000:
                    continue
                all_reviews.append(review_dict)
                review_dict = dict()
                if is_first and i > 80_000_000:
                    break
            else:
                line_splited = line.split(':')
                feature = line_splited[0]
                value = ''.join(line_splited[1:])
                if feature != 'text' and feature != 'review':
                    review_dict[feature] = value.strip()
        if review_dict:
            all_reviews.append(review_dict)

    df = pd.DataFrame(all_reviews)
    # df = df.astype({
    #     'beer_name': 'str', 
    #     'beer_id': 'int',
    #     'brewery_name':'str',
    #     'brewery_id': 'int',
    #     'style': 'str',
    #     'abv': 'float',
    #     'date': 'int',
    #     'user_id': 'int',
    #     'appearance': 'int',
    #     'aroma': 'int',
    #     'palate': 'int',
    #     'taste': 'int',
    #     'overall': 'int',
    #     'rating': 'float',
    #     })
    df = df.astype({
        'beer_name': 'str', 
        'beer_id': 'int',
        'brewery_name':'str',
        'brewery_id': 'int',
        'style': 'str',
        'abv': 'float',
        'date': 'int',
        'user_id': 'str',
        'appearance': 'float',
        'aroma': 'float',
        'palate': 'float',
        'taste': 'float',
        'overall': 'float',
        'rating': 'float',
        })
    df['date'] = pd.to_datetime(df['date'], unit='s')

    df.to_pickle(f'{output}/reviews_{int(is_first)}')



def parse_reviews(path, output):
    parse_reviews_to_pickle(path, output, True)
    parse_reviews_to_pickle(path, output, False)

    reviews_df0 = pd.read_pickle(f'{output}/reviews_0')
    reviews_df1 = pd.read_pickle(f'{output}/reviews_1')

    return pd.concat([reviews_df0, reviews_df1])



beer_style_mapping = {
"Bocks": ["Bock", "Doppelbock", "Eisbock", "Maibock", "Weizenbock"],
"Brown Ales": ["Altbier", "American Brown Ale", "Belgian Dark Ale", "English Brown Ale", "English Dark Mild Ale"],
"Dark Ales": ["Dubbel", "Roggenbier", "Scottish Ale", "Winter Warmer"],
"Dark Lagers": ["American Amber / Red Lager", "Czech Amber Lager", "Czech Dark Lager", "European Dark Lager", "Märzen", "Munich Dunkel","Euro Dark Lager", "Rauchbier", "Schwarzbier", "Vienna Lager"],
"Hybrid Beers": ["Bière de Champagne / Bière Brut", "Braggot", "California Common / Steam Beer", "Cream Ale"],
"India Pale Ales": ["American IPA", "Belgian IPA", "Black IPA", "Brut IPA", "English IPA", "Imperial IPA", "Milkshake IPA", "New England IPA"],
"Pale Ales": ["American Amber / Red Ale", "American Blonde Ale", "American Pale Ale", "Belgian Blonde Ale", "Belgian Pale Ale", "Bière de Garde", "English Bitter", "English Pale Ale", "English Pale Mild Ale", "Extra Special / Strong Bitter (ESB)", "Grisette", "Irish Red Ale", "Kölsch", "Saison"],
"Pale Lagers": ["American Adjunct Lager","Dortmunder / Export Lager", "Euro Strong Lager", "American Pale Lager", "Czech Pilsener", "German Pilsener", "American Lager", "Bohemian / Czech Pilsner", "Czech Pale Lager", "European / Dortmunder Export Lager", "European Pale Lager","Euro Pale Lager", "European Strong Lager", "Festbier / Wiesnbier", "German Pilsner", "Helles", "Imperial Pilsner", "India Pale Lager (IPL)", "Kellerbier / Zwickelbier", "Light Lager", "Malt Liquor"],
"Porters": ["American Porter", "Baltic Porter", "English Porter", "Imperial Porter", "Robust Porter", "Smoked Porter"],
"Specialty Beers": ["Chile Beer","American Black Ale","Black & Tan", "Pumpkin Ale", "Herbed / Spiced Beer","Low Alcohol Beer", "Fruit / Vegetable Beer", "Fruit and Field Beer", "Gruit / Ancient Herbed Ale", "Happoshu", "Herb and Spice Beer", "Japanese Rice Lager", "Kvass", "Low-Alcohol Beer", "Pumpkin Beer", "Rye Beer", "Sahti", "Smoked Beer"],
"Stouts": ["American Imperial Stout","Milk / Sweet Stout","American Double / Imperial Stout", "American Stout", "English Stout", "Foreign / Export Stout", "Irish Dry Stout", "Oatmeal Stout", "Russian Imperial Stout", "Sweet / Milk Stout"],
"Strong Ales": ["American Barleywine","Belgian Strong Pale Ale","Belgian Strong Dark Ale", "American Strong Ale", "Belgian Dark Strong Ale", "Belgian Pale Strong Ale", "English Barleywine", "English Strong Ale", "Imperial Red Ale", "Old Ale", "Quadrupel (Quad)", "Scotch Ale / Wee Heavy", "Tripel", "Wheatwine"],
"Wheat Beers": ["American Dark Wheat Beer","American Pale Wheat Ale", "American Dark Wheat Ale", "Kristalweizen", "American Pale Wheat Beer", "Dunkelweizen", "Grodziskie", "Hefeweizen", "Kristallweizen", "Witbier"],
"Wild/Sour Beers": ["Berliner Weisse","Berliner Weissbier", "Brett Beer", "Faro", "Flanders Oud Bruin", "Flanders Red Ale", "Fruit Lambic", "Fruited Kettle Sour", "Gose", "Gueuze", "Lambic", "Wild Ale"]
}

restructured_dict = {style: family for family, style in beer_style_mapping.items() for style in style} # Inversing keys and values 
