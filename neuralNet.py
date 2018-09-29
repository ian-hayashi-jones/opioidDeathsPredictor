### neuralNet.py ###
#
#
#

from sklearn.neural_network import MLPRegressor
import data, error

# Create neural network object
regr = MLPRegressor(max_iter=1000, hidden_layer_sizes=(128,128), verbose=True)

# Train model
regr.fit(data.train_X, data.train_Y)

# Predict
prediction = regr.predict(data.test_X)

# Use error.py module to print mean squared error and average percent error
error.print_error(prediction, data.test_Y)
