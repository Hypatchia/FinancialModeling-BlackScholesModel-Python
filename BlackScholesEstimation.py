def  ParameterEstimation(Series):
    Rendements =(numpy.log(Series.shift()) - numpy.log(Series)).dropna()
    Rendements_2=Rendements**2
    R_mean=numpy.mean(Rendements)*252
    R_variance=numpy.var(Rendements)*252
    R_std=numpy.sqrt(R_variance)
    #Parameter Estimation :
    lag=1
    drift = (R_mean/lag) +R_variance/(2*lag)
    volatility=R_std/math.sqrt(lag)
    return drift, volatility