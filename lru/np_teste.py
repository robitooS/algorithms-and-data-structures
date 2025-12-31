import numpy as np

np.random.seed(42)
data = np.random.randint(low=0, high=100, size=100)

desvio_padrao = data.std()
mean = data.mean()

