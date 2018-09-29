import sys
import data, error
from sklearn import linear_model

"""
Predict and print error
"""
# Create linear regression object
regr = linear_model.LinearRegression(fit_intercept=True, normalize=True, copy_X=False)

# Train the model
regr.fit(data.train_X, data.train_Y)

# Predict
prediction = regr.predict(data.test_X)

# Use error.py module to print mean squared error and average percent error
error.print_error(prediction, data.test_Y)


