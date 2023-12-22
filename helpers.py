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

