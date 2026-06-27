# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This project uses Random Forest Classifier from scikit-learn to predict whether a person's annual income is greater than $50,000 based on demographic and employment information from the U.S. Census dataset. 

## Intended Use
The model is intended to demonstrate how to build, evaluate, and deploy a machine learning model using FastAPI. It predicts whether an individual's income is above or below $50,000 based on the input features. It is not intended to be used for the real world or to help make high-stakes decisions. 

## Training Data
The model was trained using the Census Income dataset provided with the project. The dataset contains demographic and employment information such as age, education, occupation, workclass, marital status, race, sex, hours worked per week, and native country. The data was split into training and testing datasets before training the model. 

## Evaluation Data
The evaluation data consist of the test portion of the Census Income dataset that was not used during training. The same preprocessing steps were applied to both the training and testing data before evaluation. 

## Metrics
The model was evaluated using Precision, Recall and F1 Score.
Precision: 0.7419
Recall: 0.6384
F1 Score: 0.6863
The model also computes these metrics for each category within every categorical feature and stores the results in slice_output.txt.

## Ethical Considerations
This dataset contains sensitive demographic information such as race, sex, and native country. Because of this, the model may make predictions that are affected by bias in the data. The model should be used for learning purposes only and should not be used by itself to make important decisions about people. 

## Caveats and Recommendations
This model was created for learning purposes and was trained using one dataset. It may not work as well with different data. The model could be improved by trying different machine learning models, adjusting the model settings, and testing how well it performs for different groups of people. 