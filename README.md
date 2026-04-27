# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Heritage Housing Issues - House Price Prediction

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). A fictitious business case was created to demonstrate how predictive analytics can be applied in a real-world scenario.
- The dataset contains nearly 1,500 housing records from Ames, Iowa. It includes house attributes (floor area, basement, garage, kitchen quality, lot size, porch, wood deck, year built, etc.) and the corresponding sale price for houses built between 1872 and 2010.

| Variable      | Meaning                                                    | Units / Values                     |
| :------------ | :--------------------------------------------------------- | :--------------------------------- |
| 1stFlrSF      | First floor square feet                                    | 334 - 4692                         |
| 2ndFlrSF      | Second-floor square feet                                   | 0 - 2065                           |
| BedroomAbvGr  | Bedrooms above grade (does NOT include basement bedrooms)  | 0 - 8                              |
| BsmtExposure  | Walkout or garden level walls                              | Gd, Av, Mn, No, None               |
| BsmtFinType1  | Rating of basement finished area                           | GLQ, ALQ, BLQ, Rec, LwQ, Unf, None |
| BsmtFinSF1    | Type 1 finished square feet                                | 0 - 5644                           |
| BsmtUnfSF     | Unfinished square feet of basement area                    | 0 - 2336                           |
| TotalBsmtSF   | Total square feet of basement area                         | 0 - 6110                           |
| GarageArea    | Size of garage in square feet                              | 0 - 1418                           |
| GarageFinish  | Interior finish of the garage                              | Fin, RFn, Unf, None                |
| GarageYrBlt   | Year garage was built                                      | 1900 - 2010                        |
| GrLivArea     | Above grade (ground) living area square feet               | 334 - 5642                         |
| KitchenQual   | Kitchen quality                                            | Ex, Gd, TA, Fa, Po                 |
| LotArea       | Lot size in square feet                                    | 1300 - 215245                      |
| LotFrontage   | Linear feet of street connected to property                | 21 - 313                           |
| MasVnrArea    | Masonry veneer area in square feet                         | 0 - 1600                           |
| EnclosedPorch | Enclosed porch area in square feet                         | 0 - 286                            |
| OpenPorchSF   | Open porch area in square feet                             | 0 - 547                            |
| OverallCond   | Rates the overall condition of the house                   | 1 - 10                             |
| OverallQual   | Rates the overall material and finish of the house         | 1 - 10                             |
| WoodDeckSF    | Wood deck area in square feet                              | 0 - 736                            |
| YearBuilt     | Original construction date                                 | 1872 - 2010                        |
| YearRemodAdd  | Remodel date (same as construction date if no remodelling) | 1950 - 2010                        |
| SalePrice     | Sale price                                                 | 34900 - 755000                     |

---

## Business Requirements

A client has inherited four houses in Ames, Iowa, and wants support in maximizing the sales price of these properties. The client has access to a public dataset containing house prices and attributes from Ames, Iowa, and would like to use it to make informed decisions.

The client requires:

1. **Data Visualization and Correlation Study**  
   The client is interested in understanding how house attributes correlate with sale price. Therefore, the client expects visualizations of the most correlated variables against SalePrice.

2. **House Sale Price Prediction**  
   The client is interested in predicting the sale price of the four inherited houses, as well as any other house in Ames, Iowa.

## Project Hypotheses and Validation Plan

- **Hypothesis 1: House Size**  
  Houses with a larger above-ground living area (GrLivArea) tend to have higher sale prices.  
  This will be validated using scatter plots of GrLivArea vs SalePrice and by calculating Pearson correlation.

- **Hypothesis 2: Age of the House**  
  Newer houses tend to have higher sale prices than older houses.  
  This will be validated by creating a house age feature (based on YearBuilt), visualizing its relationship with SalePrice, and analyzing correlations and grouped summary statistics.

- **Hypothesis 3: Kitchen Quality**  
  Houses with higher kitchen quality (KitchenQual) tend to have higher sale prices.  
  This will be validated using boxplots comparing SalePrice across kitchen quality categories and calculating mean SalePrice per category.

## The Rationale to Map the Business Requirements to the Data Visualisations and ML Tasks

- **Business Requirement 1: Data Visualisation and Correlation Study**  
  Correlation analysis and visualizations (scatter plots, boxplots, and heatmaps) will be used to identify the house attributes most strongly associated with SalePrice. This helps translate raw housing data into actionable insights and supports feature selection for model training.

- **Business Requirement 2: Predictive Modelling**  
  A supervised regression machine learning model will be developed to predict SalePrice based on housing attributes. This enables the client to estimate the value of the inherited houses and provides a tool for predicting prices of other houses in Ames, Iowa.

## ML Business Case

### What are the business requirements?

- Identify which house attributes are most correlated with SalePrice through analysis and visualization.
- Predict sale prices for the four inherited houses and any other property in Ames, Iowa.

### Can conventional data analysis answer part of the business requirements?

Yes. Correlation studies, visualizations, and summary statistics can be used to understand which variables influence SalePrice.

### Does the client need a dashboard or an API endpoint?

The client requires a dashboard to explore insights and generate predicted house prices.

### What does the client consider a successful project outcome?

- A study showing the most relevant variables correlated to SalePrice.
- A model capable of predicting sale prices for the four inherited houses and other houses in Ames, Iowa.

### Epics and User Stories

- **Epic 1: Data Collection and Understanding**  
  User Story: As a client, I want housing data so that I can understand which factors influence house prices.

- **Epic 2: Data Cleaning and Preparation**  
  User Story: As a data analyst, I want to clean and prepare the dataset so that it is suitable for analysis and machine learning.

- **Epic 3: Data Visualization and Correlation Study**  
  User Story: As a client, I want visual insights showing which house attributes correlate with sale price.

- **Epic 4: Model Training and Evaluation**  
  User Story: As a client, I want a reliable model that predicts house sale price so I can estimate the value of the inherited properties.

- **Epic 5: Dashboard Development**  
  User Story: As a user, I want an interactive dashboard so I can explore insights and generate predictions.

- **Epic 6: Deployment**  
  User Story: As a client, I want the dashboard deployed so I can access the system easily.

### Ethical or Privacy Concerns

No major ethical or privacy concerns are expected, as the dataset is publicly available and does not contain sensitive personal information.

### Does the data suggest a particular model?

Yes. Since SalePrice is a continuous numeric variable, the problem is best approached using supervised regression models.

### What are the model inputs and intended outputs?

- **Inputs:** House attributes (for example: GrLivArea, YearBuilt, GarageArea, KitchenQual, etc.)
- **Output:** Predicted SalePrice

### Performance Goal

The agreed performance goal is an **R² score of at least 0.75** on both the training and test sets.

### How will the client benefit?

The client will benefit by being able to estimate the market value of the inherited properties and maximize potential sale prices using reliable predictive insights.

## Dashboard Expectations

The dashboard will include:

- **Project Summary Page**  
  Dataset overview and client requirements.

- **Correlation Study Page**  
  Visual findings showing which variables are most correlated with SalePrice.

- **Inherited House Price Prediction Page**  
  Displays the four inherited houses’ attributes and predicted sale price for each, including the summed predicted total.

- **House Price Prediction Tool**  
  Interactive widgets allowing users to input house attributes and generate real-time sale price predictions.

- **Hypothesis and Validation Page**  
  Lists project hypotheses and explains how they were tested.

- **Technical Page**  
  Displays model performance metrics and the deployed pipeline steps.

## Dashboard Design

The Streamlit dashboard was designed to allow the client to explore the dataset, understand the key factors influencing house sale prices, and generate real-time predictions for the four inherited houses and any other property in Ames, Iowa.

The dashboard contains the following pages:

### Page 1: Project Summary

**Purpose:** Provide an overview of the project and the client requirements.

**Content:**

- Project introduction and business context
- Dataset description and source information
- Summary of the two main business requirements
- Overview of the workflow (data analysis, modeling, and prediction system)

The summary page gives the user a clear understanding of the project scope and objectives before exploring deeper insights.

![Project Summary](assets/images/streamlitProjectSummary.png)

### Page 2: Correlation Study and Data Insights

**Purpose:** Identify which house attributes are most strongly associated with SalePrice.

This page helps the client understand which features have the greatest impact on house value.

**Content:**

- Correlation heatmap showing relationships between numerical features and SalePrice
- Table of top positively and negatively correlated variables
- Scatter plots showing key relationships (e.g., GrLivArea vs SalePrice)
- Boxplots showing categorical feature impact (e.g., KitchenQual vs SalePrice)
- Summary of key findings

The correlation analysis highlights the most influential predictors of house price.

The heatmap below shows the strength of relationships between all numerical variables and SalePrice.

![Correlation Study](assets/images/streamlit_correlation.png)

The second visualization provides additional correlation insights and confirms key feature relationships.

![Correlation Study](assets/images/streamlit_correlation1.png)

### Page 3: Inherited House Price Predictions

**Purpose:** Display predicted sale prices for the four inherited houses and their combined value.

This page provides the main business output of the project.

**Content:**

- Table of inherited house attributes
- Predicted SalePrice for each house
- Total combined predicted value for all four houses
- Explanation of prediction method

This allows the client to directly understand the financial value of the inherited properties.

The visualization below shows the predicted values generated by the trained ML pipeline.

![Inherited Houses](assets/images/streamlit_inherited_houses.png)

### Page 4: House Price Prediction Tool (Interactive)

**Purpose:** Allow users to input house features and receive real-time price predictions.

This page enables dynamic testing of different house configurations.

**Content:**

- Sliders for numeric inputs (e.g., GrLivArea, LotArea, GarageArea)
- Dropdowns for categorical inputs (e.g., KitchenQual, GarageFinish)
- Prediction button
- Output displaying estimated SalePrice

Users can explore how changing house features affects predicted value.

The interface below shows the interactive prediction tool.

![House Price Prediction Tool](assets/images/Streamlit_predict_prices.png)

### Page 5: Project Hypotheses and Validation

**Purpose:** Show how hypotheses were tested using data analysis.

This page connects business assumptions with actual data evidence.

**Content:**

- Hypotheses list (size, age, kitchen quality)
- Supporting visualizations (scatter plots, boxplots, grouped statistics)
- Conclusions on whether each hypothesis is supported

This page demonstrates how data analysis validates business assumptions.

The image below shows the hypothesis validation dashboard.

![Hypotheses](assets/images/streamlit_hypotheses.png)

### Page 6: Model Performance and Pipeline

**Purpose:** Present model evaluation results and technical transparency.

This page ensures the model meets the required performance standards.

**Content:**

- MAE, RMSE, and R² score
- Model type (Gradient Boosting Regressor)
- Pipeline steps (preprocessing + model training)
- Comparison against success criteria

This page confirms the reliability and performance of the prediction system.

The image below shows the technical performance of the trained model.

![Technical Page](assets/images/streamlit_technical.png)

## Unfixed Bugs and Limitations

During development, several modelling limitations and trade-offs were identified. These were not left unresolved due to oversight, but rather reflect deliberate design choices made during feature engineering and model optimisation to balance performance, interpretability, and data constraints.

### 1. Impact of Outliers After Winsorization

Outliers in numerical variables such as `GrLivArea`, `LotArea`, and `SalePrice` were addressed using winsorization.

- This reduced the influence of extreme values while preserving dataset integrity.
- However, some residual extreme values may still influence model predictions. Prediction error increases for higher-value houses due to fewer training examples in this range.

The plot shows that model prediction becomes less consistent at higher values.

![Actual vs Predicted](assets/images/model_plot.png)

- More aggressive approaches such as full removal or heavy transformation were avoided to maintain representation of rare but valid luxury homes.

### 2. Residual Skewness in Numerical Features

Power transformations (Box-Cox / Yeo-Johnson) were applied to reduce skewness in selected numerical features.

- Power transformations reduced skewness in key numerical features, improving distribution symmetry and model stability.
  ![Feature skewness before vs After transformation](assets/images/feature_skewness_plot.png)

- However, not all variables could be fully normalised due to mixed distributions.
- As a result, some mild skewness remains in the dataset, which may slightly affect model assumptions.

## Deployment

### Heroku

- The App live link is: <https://YOUR_APP_NAME.herokuapp.com/>
- Set the .python-version Python version to a [Heroku-24](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

- Here you should list the libraries you used in the project and provide example(s) of how you used these libraries.

## Credits

- In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism.
- You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open Source site
- The images used for the gallery page were taken from this other open-source site

## Acknowledgements (optional)

- In case you would like to thank the people that provided support through this project.
