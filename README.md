### Project repository for tornADA group

## Title

Do you know ~~what~~ *who* you’re drinking?

## Abstract
There’s so many brands of beer out there to choose from. Some of them are global and very well known, like Heineken, Guinness, Carlsberg, or even Asahi, and others are quite a lot smaller, local brands, and even independent breweries. But do we always know what we’re drinking, or even who we’re drinking?

In the era of megacorporations, shareholders, and extremely diversified portfolios and assets, the lines connecting the “owners” to their “products” turn into a Gordian knot, impossible to untangle completely. This is especially the case for Beer groups. Some of the biggest and most well-known brands own breweries and other smaller brands all over the world. A shocking example is the Japanese-founded-and-owned Asahi group, which owns the Italian Peroni brand, considered a staple beer in Italy.


## Research Questions
* Do we always know who (whose beer) we’re drinking? 
* Does an acquisition of a beer/brewery affect the quality of the product?
* Are beer experts a self-fulfilling prophecy? I.e. does their expertise and knowledge of beers, companies, and news introduce bias in their reviews of large beer groups?

## Additional Datasets
We create one dataset for each of the 5 biggest brands of the original dataset (ABinBev, Heineken, Carlsberg, Asahi, Diaego) which track all the breweries they own for each year which interest us, i.e 2010-2016. These dataset are created from their annual reports available on the internet. 

## Methods
Before starting working on our project specifically, we did an initial check of our dataset. 

Then we create our five additional datasets. From them, we can combine the datasets (original and additional) and correctly tag breweries as “big” or “small” depending on if they belong to a big company or not. As there are many subtleties in ownership on beer market, we decide to make following assumptions:
* A beer is considered “big” if the brewery producing it belongs to a “big” company, where belonging is defined as the company owning more than 50% of its shares.
* We don’t consider as a big brands beers that are owned by big companies but are brewed under license by independent companies.
* We don’t take into account the fact that some beers (Corona, Labott) are distributed in some parts of the word (USA) by different companies as long as they don’t produce the beer by themselves.

In addition and if we have time, we can compare these companies beetween them based on their financial result and sales that are also available on annual reports.

Once we have these "tags", we can analyze how the size of the owner company influence the reviews. Moreover, we can try to understand if these reviews are improving or deteriorating

Moreover, we will try to understand the reason leading to possible improvements or deteriorations in reviews. Is this due to the quality of the beer or the assumptions made by consumers about the size of the company producing the beer?

We plan to make the following croncrete analysis : 

> **Regression analysis**
> Analyze the overall rating of a beer as a function of: 
>  - binary: is the reviewer from the country of the beer ?
>  - binary: is the beer from a big company ?
>  - taste 
>  - palate 
>  - aroma 
>  - abv   
> Goal: Is the binaries criteria influence the customer's opinions?

> **Textual analysis**
> Look at if there is a significant difference between reviews from “big” beers and “small” beers. Using something like doc2vec or LSI.

> **Is the knowledge of the beer owner influences ratings?**
> Compare the ratings of the beers from the same company that are branded as that company from the ones which are not.


## Proposed timeline

| Week/Day  | Tasks          |
| :------------------------- |:---------------|
| 20-26 nov (Week 10)    |   Gather all required data on mergers and acquisitions in the format discussed above (+ Homework 2)                                         |
| 27nov - 3dec (Week 11)  | Start doing data analysis: identify significant covariates, find interesting correlations. Make analysis discussed in "Methods".        |
| 4-10 dec (Week 12)     | Connecting graphs and results. Begin writing data story, create a github page for it.                                        |
| 11-17 dec (Week 13)   |                                     |
| 18-22 dec (Week 14)   | Finalize the data story and the report                                                        |

## Organization within the team

* Each team member create the additional dataset (about company merges) of one company
    * Kajetan: AB InBev 
    * Matthew: Carlsberg
    * Clara: heineken
    * Konstantinos: Asahi
    * Anis: Diageo 
* Analysis:
    * Kajetan:
    * Matthew: Textual Analysis
    * Clara:
    * Konstantinos:
    * Anis: Regression Analysis
* Data Story: Clara

## Questions for TA (Optional)
