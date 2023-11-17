### Project repository for tornADA group

## Title

Do you know ~~what~~ *who* you’re drinking?

## Abstract
In this study we aim to investigate the effect of acquisitions and mergers of big beer brands on the quality of the brewed beers. It is often the case that an acquisition of a (physical) product from a large company will lead to a noticeable drop in quality, mainly due to the company’s choice of quantity over quality. The effect will be studied through the reviews and ratings given by several users on two popular beer-rating sites, RateBeer and BeerAdvocate. Our goal is threefold: first to track acquisitions and mergers of breweries by big companies over the last 20 years, then to study the corresponding change -or lack thereof- in the reviews, and finally to study the bias of the brand name on the reviewers themselves.


## Research Questions
* Does the size of a company influence the consumers' opinions? 
* Does a merger between two companies, or an acquisition of one from another, change the quality of the brewed beers?
* Does the reviewer consider the scale of the brewery when evaluating their beers?

With more precise questions, we will try to answer:
* What beers and breweries are owned by which large brand names?
* Do beer reviewers fall in the trap of the brand name? I.e. when comparing the ratings of the brand name beer of large beer groups (Heineken, Asahi, etc.) with other beers they own and produce ([Heineken example], Peroni, etc.), are the brand names lower rated across all companies, or is there no effect?

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

> **Regression Analysis**: Determinants of Beer Ratings.     
> Objective: To evaluate the overall rating of a beer based on a set of independent variables.    
> Variables:     
> * Country Match: Whether the reviewer is from the same country as the beer (Binary).    
> * Company Size: Classification of the beer company as a large entity (Binary).    
> * Taste: The sensory evaluation score of the beer's flavor.    
> * Palate: The sensory evaluation score of the beer's mouthfeel.    
> * Aroma: The sensory evaluation score of the beer's scent.    
> * ABV (Alcohol by Volume): The percentage of alcohol contained in the beer.    
> * Company Scale: The market size or reach of the company producing the beer.
>           
> The analysis will quantify how each factor contributes to the overall satisfaction with a beer, as measured by its rating. This includes both categorical assessments (Country Match, Company Size) and continuous sensory attributes (Taste, Palate, Aroma, ABV), as well as the influence of the company's market presence.    


> **Textual analysis**
> Look at if there is a significant difference between reviews from “big” beers and “small” beers. Using something like doc2vec or LSI.

> **Is the knowledge of the beer owner influences ratings?**
> Compare the ratings of the beers from the same company that are branded as that company from the ones which are not.


## Proposed timeline

| Week/Day  | Tasks          |
| :------------------------- |:---------------|
| 20-26 nov (Week 10)    |   Gather all required data on mergers and acquisitions in the format discussed above (+ Homework 2)                                         |
| 27nov - 3dec (Week 11)  | Start doing data analysis: identify significant covariates, find interesting correlations. Make analysis discussed in "Methods".        |
| 4-10 dec (Week 12)     | Connecting graphs and results. Beginning to write the data story (by making its scheme) and create a github page for it.                                        |
| 11-17 dec (Week 13)   | Finalize the analysis by sum up all of our results. Writing the data story.                                      |
| 18-22 dec (Week 14)   | Finalize the data story and the report                                                        |

## Organization within the team

| Team Member  | Tasks          |
| :------------------------- |:---------------|
| Kajetan  |(1) Initial global analysis on the data  (2) Create the additional dataset on AB in Bev     (3) Compare the results of the big companies and the small ones |
| Matthew  |(1)  Create the additional dataset on Carlsberg   (2) Textual analysis    (3) Add up all interesting results and work on the data story format   |
| Clara  |(1)  Create the additional dataset on Heineken   (2) Compare the results of the 5 big companies     (3) Create the github page and finalize the layout |
| Anis  |(1)  Create the additional dataset on Diaego   (2) Make the regression analysis and find significant covariates to work with     (3) Make some deeper anlysis on the data (different criteria than size for example)  |
| Kontantinos  |(1)  Create the additional dataset on Asahi   (2) Work on the redaction of the data story     (3) Create the interactive graphs for the data story   (4) Document the ReadMe and comment the notebook  |

## Questions for TA (Optional)
