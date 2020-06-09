![Yelp Image](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Yelp_Logo.svg/2880px-Yelp_Logo.svg.png)


# Using Health Inspections to Predict Yelp Stars In New York City

### Contributors

[Omar Smiley](https://git.generalassemb.ly/smileyo)

## Problem Statement
Every restaurant in New York City is scheduled for an unannounced inspection at least once a year. Inspectors from the NYC Department of Health and Mental Hygiene (DOHMH) conducts checks for compliance with city and state food safety regulations and marks points for any condition that violates these rules.

Can the DOHMH inspection results and demographics data be used to predict whether a restaurant has a favorable or unfavorable Yelp review?


## Executive Summary
The Health Department inspects approximately 27,000 restaurants in New York City to monitor their compliance with food safety regulations. Inspectors observe how food is prepared, served and stored and whether restaurant workers are practicing good hygiene. Sanitary violations are issued when the safety of the food being prepared and served is threatened. Sanitary violations displayed in red text are the most critical violations. Examples of sanitary violations include food being held at an unsafe temperature and evidence of mice. Sanitary violations are scored and contribute to a restaurant’s grade. No other violations are scored or contribute to the grade. Examples of non-scored violations include failing to display the Health Department-issued permit and not posting the restaurant's letter grade.

Logistic regression model allows us to properly predict 60%  of observations as having a favorable Yelp average rating of 4 or higher.
Using lasso regression for feature selection and interpretation: Restaurants with larger number of Yelp reviews (log_review_count) less likely to have a poor rating (less than 4). The next step in further improving this project is to analyze additional health inspections on more years. While this may require additional get requests to the Yelp Fusion API, it will result in a more accurate and longer-term picture of the restaurant's health inspection scores. Another recommendation is to add additional features in order to see if it improves the model. This could include incorporating public and proprietary datasets that relate to the food industry. One example could be Michelin star ratings, often considered a high standard of dining excellence.


## Python Package Requirements

In order to succesfully clone this repository, please insure to have the following packages installed into your Python environment:
* [Numpy](https://pypi.org/project/numpy/)
* [Pandas](https://pypi.org/project/pandas/)
* [Scikit Learn](https://pypi.org/project/scikit-learn/)
* [Seaborn](https://pypi.org/project/seaborn/)
* [Matplotlib](https://pypi.org/project/matplotlib/)

## Contents

In this repo, you will find the following notebooks in the `code` folder:

1. 01_data_processing.ipynb
2. 02_EDA_and_Modeling.ipynb

You will also find three python scripts that were used to query the Yelp Fusion API in order to gather the relevant restaurant data.

## Data Dictionary

| Parameter | Description | Data Type | Example |
| ------ | ------ | ------- | ------ |
|camis | DOHMH RecordID number | Integer | 30075445 |
|dba | Doing Buisness As | String | "MORRIS PARK BAKE SHOP" |
|boro | New York City Borough | String | "BRONX" |
|zip_code | zip code | Integer | 10462 |
|cuisine_description| Description of cuisine | String | "Bakery"|
|inspection_date | Date of Inspection | String | "2015-09-04" |
|inspection_year | Year of inspection | String | "2015.0" |
|inspection_month | Month of inspection | String | "9.0" |
|score | Inspection score | String | "6.0" |
|grade | Inspection grade | String | A | 
|name | Restaurant name | String | "Morris Pk Bake Shop" |
|latitude | latitude of the coordinates for the restaurant | String | 40.848446 |
|longitude | longitude of the coordinates for the restaurant | String | -73.856079 |
|review_count | number of reviews for the restaurant | Integer | 31 |
|price | Restaurant price range per person | String | 2 |
|rating | Restaurant Yelp rating | Integer | 4.5 |
|categories | Restaurant categories | String | "['bakeries', 'desserts']" |
|city | City | String | "Bronx" |
|violation_code | DOHMH violation codes issued to restaurant | String | "[06C]" |


## References
- Yelp Fusion API Endpoint Documentation, https://www.yelp.com/developers/documentation/v3
- NYC OpenData, “DOHMH DOHMH New York City Restaurant Inspection Results https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/43nn-pn8j
- Python Timer Functions: Three Ways to Monitor Your Code https://realpython.com/python-timer/#creating-a-python-timer-class
- How to Use the Yelp’s Fusion API https://medium.com/@morgannegagne/how-to-use-the-yelp-fusion-api-70e62f96b0ab
- Levenshtein Distance and Text Similarity in Python https://stackabuse.com/levenshtein-distance-and-text-similarity-in-python/
