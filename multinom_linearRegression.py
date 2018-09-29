import sys
import multinom_data, error
from sklearn import linear_model

"""
Predict and print error
"""
# Create linear regression object
regr = linear_model.LinearRegression(fit_intercept=True, normalize=True, copy_X=False)

# Train the model
regr.fit(multinom_data.train_X, multinom_data.train_Y)

# Predict
prediction = regr.predict(multinom_data.test_X)

# Use error.py module to prin mean squared error and average percent error
error.print_error(prediction, multinom_data.test_Y)

