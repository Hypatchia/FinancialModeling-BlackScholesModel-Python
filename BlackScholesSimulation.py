def  simulation_gbm(drift, volatility , initial_value, n, time_difference):
  #simuler N variables aleatoires suivant la loi normal (0,1) 
  # on utilise la fonction predéfinie standard_normal 
  # Standardization : Données centrées reduites
  N = numpy.random.standard_normal((k+1,n))
  N -= N.mean()
  N /= N.std()

  S=numpy.zeros((k+1,n))
  S[0]=initial_value
  for i in range(1,k+1):
    S[i] = S[i-1] * numpy.exp((drift - volatility ** 2 / 2) * time_difference + volatility * math.sqrt(time_difference) * N[i])
  return S