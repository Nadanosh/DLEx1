import numpy as np



class FullyConnected:

    def forward(self,input_tensor):
        input_tensor = np.dot(self.weights.T,input_tensor)
        return input_tensor

    def __init__(self,input_size,output_size):
        np.random.seed(1)
        self.weights = np.random.rand(input_size,output_size)
        self.delta = 1

    def backward(self,error_tensor):
        new_error_tensor = np.dot(self.weights.T,error_tensor)
        self.weights = self.weights- self.delta*np.dot(error_tensor,self.input_tensor.T)
        return new_error_tensor
         
