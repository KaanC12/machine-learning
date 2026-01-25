import numpy as np
import pandas as pd

class Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.inputs = inputs
        return np.dot(inputs, self.weights) + self.biases

    def backward(self, dvalues):
        self.dweights = np.dot(self.inputs.T, dvalues)
        self.dbiases = np.sum(dvalues, axis=0, keepdims=True)
        return np.dot(dvalues, self.weights.T)

    
class ReLu:
    def forward(self, input):
        self.input = input
        return np.maximum(0, input)
    
    def backward(self, dvalues):
        dinputs = dvalues.copy()
        dinputs[self.input <= 0] = 0
        return dinputs
    
class LossMSE:
    def forward(self, y_pred, y_true):
        self.y_pred = y_pred
        self.y_true = y_true

        loss = np.mean((y_true - y_pred) ** 2)
        return loss
    
    def backward(self):
        samples = len(self.y_pred)
        dinputs = (-2 * (self.y_true - self.y_pred) / samples)

        return dinputs
