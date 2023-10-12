# Financial Modeling 
* This Project was part of my Master's Degree Class: Stochastic Analysis & Modeling.
# Project: Black Scholes model for Financial Modeling of Returns for a Stock Price.
- This project focuses on financial data Analysis and Modeling utilizing Geometric Brownian Motion and the Black-Scholes model for stock price return analysis.
  
### Approach:
* Analyse Time Series Data using Normality Tests, histograms, Correlation Plots (Partial Correlation and AutoCorrelation)...
* Implement geometric Brownian Motion to predict stock prices, a widely-used model in financial mathematics.
* Provide an Estimation model for CRSPR stock - a key player in the biotechnology industry
* Perform simulations for CRSPR stock to understand its behavior under various conditions and market scenarios.
* Simulate the behavior of the ARK ETF GENOMICS, a fund that invests in companies at the forefront of genomics and biotechnology.

### Data Sources
The financial data utilized in this project is primarily sourced from Yahoo Finance.
- The data is for Closing Price of 252 days between 07/06/2021 and 03/06/2022.
- The exact Time Series are in excel files in the directory /data

### Dependencies
To run the code and set up the environment for this project, you will need the following libraries and tools:
- Python 3.7
- NumPy
- Pandas
- Math
- Plotly
- Seaborn
- statmodels

## How to Use
To explore the estimation and simulation of stock price returns using the Black-Scholes model, follow these steps:
* Clone Rpository
  
~~~
git clone [<repository_url>](https://github.com/Hypatchia/FinancialModeling-BlackScholesModel/)https://github.com/Hypatchia/FinancialModeling-BlackScholesModel/
~~~

* Navigate to the project directory.
~~~
 cd FinancialModeling-BlackScholesModel
~~~
* Open and run the Jupyter Notebook to view all the steps of the project.
* Open the scrips to find two main functions:
  * Estimation of Drift & Volatility
  * Simulation of Black Scholes n Model Paths.
 
* For a better understanding of the financial modeling outputs, various plots (acf-pacf) and visualizations are provided in the notebook in addition to comments containing the information (I hope you speak french).

  

