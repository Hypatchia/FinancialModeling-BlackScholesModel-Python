
# Import libraries
import numpy
import math


def  simulation_gbm(k, drift, volatility , initial_value, n, time_difference):

  """
    Simulate Geometric Brownian Motion (GBM) paths.

    Parameters:
    - drift (float): Drift rate of the asset.
    - volatility (float): Volatility of the asset.
    - initial_value (float): Initial value of the asset.
    - n (int): Number of simulation paths.
    - time_difference (float): Time increment for each simulation step.

    Returns:
    - S (numpy.ndarray): Array of simulated GBM paths.
    """
  # Generate N random variables following a standard normal distribution
  N = numpy.random.standard_normal((k+1,n))

  # Standardization: Center and scale the data
  N -= N.mean()
  N /= N.std()
  # Create an array to store the simulated paths
  S=numpy.zeros((k+1,n))
  S[0]=initial_value
  # Perform simulation
  for i in range(1,k+1):
    S[i] = S[i-1] * numpy.exp((drift - volatility ** 2 / 2) * time_difference + volatility * math.sqrt(time_difference) * N[i])
  return S