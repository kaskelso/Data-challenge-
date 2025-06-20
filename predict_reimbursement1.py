#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 14:48:29 2025

@author: kennyaskelson
"""

import sys
import numpy as np
import joblib
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress INFO, WARNING, and ERROR logs

# Load the model
best_model = joblib.load('reimbursement_model.joblib')

# Read command-line arguments
trip_duration = float(sys.argv[1])
miles_traveled = float(sys.argv[2])
total_receipts = float(sys.argv[3])

# Make prediction
X = np.array([[trip_duration, miles_traveled, total_receipts]])
prediction = best_model.predict(X)

# Print the predicted value
print(round(float(prediction[0]), 2), file=sys.stdout)
