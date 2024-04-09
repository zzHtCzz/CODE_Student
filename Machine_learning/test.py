import numpy as np


X = np.random.uniform(0, 2, 5)
X.reshape(-1, 1)
print(X)

weights_input_hidden = np.random.uniform(size=(1, 8))#1 hàng 8 cột
print(weights_input_hidden)