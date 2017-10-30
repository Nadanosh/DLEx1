import numpy as np



class FullyConnected:

    def forward(input_tensor):
        return input_tensor
    def __init__(self,input_size,output_size):
        self.input_size = input_size
        np.random.seed(1)
        self.delta = 0.001

        
