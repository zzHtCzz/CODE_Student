import numpy as np
import matplotlib.pyplot as plt

# Hàm kích hoạt tansig
def tansig(x):
    return (2 / (1 + np.exp(-2 * x))) - 1

# Đạo hàm của tansig
def tansig_derivative(x):
    return 1 - np.square(tansig(x))

# Hàm loss (Mean Squared Error)
def mse_loss(y_true, y_pred):
    return ((y_true - y_pred) ** 2).mean()

# Tạo dữ liệu huấn luyện
np.random.seed(0)
X = np.random.uniform(0, 2, 300)
y = (np.exp(-X)) * np.sin(10 * X) + np.random.normal(0, 0.05, 300)

# Khởi tạo mạng neuron
input_size = 1
hidden_sizes = [10, 20, 30, 40, 50, 60]  # Số lượng đơn vị ẩn trong từng lớp ẩn
output_size = 1
learning_rate = 0.01

# Khởi tạo trọng số và bias cho lớp ẩn và lớp ra
weights = []
biases = []

input_dim = input_size
for hidden_dim in hidden_sizes:
    weights.append(np.random.uniform(size=(input_dim, hidden_dim)))
    biases.append(np.zeros((1, hidden_dim)))
    input_dim = hidden_dim

weights.append(np.random.uniform(size=(input_dim, output_size)))
biases.append(np.zeros((1, output_size)))

# Huấn luyện mạng neuron
epochs = 10000

for epoch in range(epochs):
    # Feedforward
    layer_input = X.reshape(-1, 1)
    layer_outputs = [layer_input]

    for i in range(len(hidden_sizes) + 1):
        layer_input = np.dot(layer_input, weights[i]) + biases[i]
        if i < len(hidden_sizes):
            layer_input = tansig(layer_input)
        else:
            output = layer_input
        layer_outputs.append(layer_input)

    # Tính loss
    loss = mse_loss(y, output)

    # Backpropagation
    d_output = 2 * (output - y)
    d_weights = []
    d_biases = []

    for i in range(len(hidden_sizes), -1, -1):
        d_weights.insert(0, np.dot(layer_outputs[i].T, d_output))
        d_biases.insert(0, np.sum(d_output, axis=0, keepdims=True))
        if i > 0:
            d_hidden = np.dot(d_output, weights[i].T)
            d_output = d_hidden * tansig_derivative(layer_outputs[i])
    
    # Cập nhật trọng số và bias
    for i in range(len(weights)):
        weights[i] -= learning_rate * d_weights[i]
        biases[i] -= learning_rate * d_biases[i]

    if epoch % 1000 == 0:
        print(f'Epoch {epoch}, Loss: {loss}')

# Dự đoán
X_test = np.linspace(0, 2, 100)
layer_input = X_test.reshape(-1, 1)

for i in range(len(hidden_sizes) + 1):
    layer_input = np.dot(layer_input, weights[i]) + biases[i]
    if i < len(hidden_sizes):
        layer_input = tansig(layer_input)
    else:
        y_pred = layer_input

# Vẽ biểu đồ kết quả
plt.scatter(X, y, label='Data')
plt.plot(X_test, y_pred, 'r', label='Predictions')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
