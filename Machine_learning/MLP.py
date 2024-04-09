import numpy as np
import matplotlib.pyplot as plt


# Hàm kích hoạt tasig
def tansig(x):
    return (2 / (1 + np.exp(-x))) - 1

#Đạo hàm hàm tansig
def dtansig(x):
    return 0.5*(1 - tansig(x)**2)


def train_MLP(epochs, input_size, hidden_size, output_size, learning_rate, x, y):
    weights_input_hidden = np.random.uniform(size=(input_size, hidden_size))
    # print(weights_input_hidden)
    weights_hidden_output = np.random.uniform(size=(hidden_size, output_size))
    print(weights_hidden_output)
    sum_error = 0
    for epoch in range(epochs):
        hidden_input = np.dot(x.reshape(-1, 1), weights_input_hidden)
        hidden_output = tansig(hidden_input)
        output_input = np.dot(hidden_output, weights_hidden_output)
        # print(output_input.reshape(-1))
        output = output_input.reshape(-1)
        
        #Lan truyền ngược
        d_output = (output - y)
        d_weights_hidden_output = np.dot(d_output.T, hidden_output)
        d_weights_hidden_output = d_weights_hidden_output.reshape(8, 1)
        weights_hidden_output += learning_rate*(d_weights_hidden_output)
        # print(weights_hidden_output)
        

        d_output = d_output.reshape(1, 300)
        d_hidden = np.dot(weights_hidden_output,d_output)
        d_hidden_input = d_hidden.T * dtansig(hidden_output)
        d_weights_input_hidden = np.dot(x.reshape(-1, 1).T, d_hidden_input)
        weights_input_hidden += learning_rate * d_weights_input_hidden
        #error
        for i in range(len(y)):
            sum_error += 0.5*(y[i] - output[i])
        if sum_error == 0.0000001:
            break
    return weights_input_hidden, weights_hidden_output.T


x = np.random.uniform(0, 2, 300)
y = (np.exp(-x)) * np.sin(10 * x)

# Khởi tạo mạng neuron
input_size = 1
hidden_size = 8
output_size = 1
learning_rate = 0.00001
epochs = 100

weights_input_hidden, weights_hidden_output = train_MLP(epochs, input_size, hidden_size, output_size, learning_rate, x, y)
print("Trọng số lớp ẩn: {}".format(weights_input_hidden))
print("Trọng số lớp ra: {}".format(weights_hidden_output))
# Dự đoán
X_test = np.linspace(0, 2, 300)
hidden_input = np.dot(X_test.reshape(-1, 1), weights_input_hidden)
hidden_output = tansig(hidden_input)
output_input = np.dot(hidden_output, weights_hidden_output.reshape(-1,1))
y_pred = output_input

# Vẽ biểu đồ kết quả
plt.scatter(x, y, label='Data')
plt.plot(X_test, y_pred, 'r', label='Predictions')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
