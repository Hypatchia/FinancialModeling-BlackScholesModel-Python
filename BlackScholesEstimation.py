
# Load libraries
import numpy, math

def  ParameterEstimation(Series):
    """
    Estimate parameters (drift and volatility) from a time series.

    Parameters:
    - Series (pandas.Series): A time series of asset prices or returns.

    Returns:
    - drift (float): Estimated drift.
    - volatility (float): Estimated volatility.


    """
    # Calculate daily returns by taking the difference of the logarithm of the series shifted by one day
    # and the logarithm of the original series. Then, drop the first NaN value.
    Rendements =(numpy.log(Series.shift()) - numpy.log(Series)).dropna()
    # Calculate the mean, variance and std of the daily returns
    R_mean=numpy.mean(Rendements)*252
    R_variance=numpy.var(Rendements)*252
    R_std=numpy.sqrt(R_variance)

    # Parameter Estimation 
    # Set the lag to 1
    lag=1
    # Calculate the drift using the mean and variance, annualized by dividing by lag.
    drift = (R_mean/lag) +R_variance/(2*lag)
    volatility=R_std/math.sqrt(lag)
    # Return the drift and volatility
    return drift, volatility

