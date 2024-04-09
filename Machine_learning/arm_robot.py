import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


def Train(samples, input_size, hidden_size, output_size, learning_rate, epochs):
    l1 = 7
    l2 = 3
    thetas = np.random.rand(samples, 2) # 100 row 2 column
    # print(thetas)
    x_coords = l1 * np.cos(thetas[:, 0]) + l2 * np.cos(thetas[:, 0] + thetas[:, 1])
    y_coords = l1 * np.sin(thetas[:, 0]) + l2 * np.sin(thetas[:, 0] + thetas[:, 1])
    coords = np.column_stack((x_coords, y_coords))

    weights_input_hidden = np.random.uniform(size=(input_size, hidden_size))
    weights_hidden_output = np.random.uniform(size=(hidden_size, output_size))

    for epoch in range(epochs):
        # lan truyền thuận
        hidden_layer_input = np.dot(thetas, weights_input_hidden)
        # print(len(hidden_layer_input))
        hidden_layer_output = sigmoid(hidden_layer_input)
        output_layer_input = np.dot(hidden_layer_output, weights_hidden_output)
        output_layer_output = sigmoid(output_layer_input)

        # lan truyền ngược
        d_output = (coords-output_layer_output) * sigmoid_derivative(output_layer_output)#100 row 2 column
        # print(len(d_output))
        error_hidden_layer = d_output.dot(weights_hidden_output.T)
        d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

        # Cập nhật trọng số
        weights_hidden_output += hidden_layer_output.T.dot(d_output) * learning_rate
        weights_input_hidden += thetas.T.dot(d_hidden_layer) * learning_rate

        # lỗi
        error = np.sum((coords-output_layer_output)**2)

        if epoch % 1000 == 0:
            print(f"Epoch {epoch}, Error: {error}")

    return weights_hidden_output, weights_input_hidden

input_size = 2
hidden_size = 64
output_size = 2

learning_rate = 0.1
epochs = 10000
error =0

samples = 100

who, wih = Train(samples,input_size,hidden_size,output_size,learning_rate,epochs)
thetas = np.random.rand(samples, 2)
hidden_layer_input = np.dot(thetas, wih)
hidden_layer_output = sigmoid(hidden_layer_input)
output_layer_input = np.dot(hidden_layer_output, who)
output_layer_output = sigmoid(output_layer_input)
for i in range(len(thetas)):
    print("{} -> {}".format(thetas[i], output_layer_output[i]))
