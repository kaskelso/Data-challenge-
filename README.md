# Data-challenge-

## This repo contains my approach to addressing the public data challenge found here https://github.com/8090-inc/top-coder-challenge/tree/main

In this challenge, the overall question was to reverse engineer a program that provides reimbursements based on mileage, days travelled, and receipts.
For this challenge I explored the data (data_challenge_EDA2.ipynb) and implemented a neural net approach (NeuralNet_rei.ipynb) using TensorFlow and RandomForest (randomforest_rei.ipynb). For this challenge you had to package your method in the run.sh scripts that are then evaluated by the eval.sh scripts. For my methods I used the predict_reimbursement.py to load the model and then print the prediction as an output. The "1" files runs the method using randomforest. Ultimately the randomforest model greatly outperformed the neural net. It was a good learning example about the pros and cons of these ML approachs when using a small dataset.

Neural Net results
![alt text](https://github.com/kaskelso/Data-challenge-/blob/main/NN_eval.jpg)

RandomForest results

![alt text](https://github.com/kaskelso/Data-challenge-/blob/main/random_forest_eval.jpg)
