import numpy as np

class NeuralNetwork:
    def __init__(self):
        self.loss = []
        self.layers = []

        self.data_layer = data_layer
        self.loss_layer = loss_layer
        self.weights = {}
    
    def _get_gradient_weights(self):
        return self.weights

    def forward(self):
        data = {}
        data[0] = data_layer.input_tensor
        for layer_nr in range(1,len(self.layers)+1):
            data[layer_nr] = np.dot(data[layer_nr-1].T,self.weights[layer_nr-1][:-1,:])
        return data

    def backward(self):
        backdata = {}
        backdata[len(self.layers)] = loss_layer
        for layerNr in reversed(range(2,len(self.layers)+1)):
            backdata[layer_nr-1] = np.dot(backdata[layerNr].T,self.weights[layerNr][:-1,:]) 
        return 1

    def train(iterations):
        
        loss.append(currentLoss)
        return 1

    def test(input_tensor):
        predict(activation_tensor)
    

