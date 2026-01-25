# Since the vast amount of dataset, the iteration cannot be done with mac M2 chip.

from data import taster
from models import ai
import numpy as np

FEATURE_COLUMNS = [
    "country",
    "province",
    "region_1",
    "region_2",
    "variety",
    "winery"
]

# DATA
datasets = taster.implement_encode("Roger Voss")
train_data = datasets["train_data"]
test_data  = datasets["test_data"] 

for col in FEATURE_COLUMNS:
    mean_value = train_data[col].mean()
    train_data[col] = train_data[col].fillna(mean_value)
    test_data[col]  = test_data[col].fillna(mean_value)

X_train = train_data[FEATURE_COLUMNS].values
y_train = train_data["points"].values.reshape(-1, 1)

X_test = test_data[FEATURE_COLUMNS].values
y_test = test_data["points"].values.reshape(-1, 1)


# MODEL
dense1 = ai.Dense(len(FEATURE_COLUMNS), 64)  
relu1  = ai.ReLU()

dense2 = ai.Dense(64, 32)
relu2  = ai.ReLU()

dense3 = ai.Dense(32, 16)
relu3  = ai.ReLU()

dense_out = ai.Dense(16, 1)   

loss_fn = ai.LossMSE()
learning_rate = 0.001
epochs = 1000

# TRAIN
for epoch in range(epochs):
    
    # Forward
    out = dense1.forward(X_train)
    out = relu1.forward(out)

    out = dense2.forward(out)
    out = relu2.forward(out)

    out = dense3.forward(out)
    out = relu3.forward(out)

    y_pred = dense_out.forward(out)
    
    # Loss
    loss = loss_fn.forward(y_pred, y_train)
    
    # Backward
    d = loss_fn.backward()

    d = dense_out.backward(d)

    d = relu3.backward(d)
    d = dense3.backward(d)

    d = relu2.backward(d)
    d = dense2.backward(d)

    d = relu1.backward(d)
    d = dense1.backward(d)
    
    # Update (SGD)
    for layer in [dense1, dense2, dense3, dense_out]:
        layer.weights -= learning_rate * layer.dweights
        layer.biases  -= learning_rate * layer.dbiases



# TEST
out = dense1.forward(X_test)
out = relu1.forward(out)

out = dense2.forward(out)
out = relu2.forward(out)

out = dense3.forward(out)
out = relu3.forward(out)

y_test_pred = dense_out.forward(out)

test_loss = loss_fn.forward(y_test_pred, y_test)
print("Test loss:", test_loss)