import googleapiclient.discovery
import os
import pandas as pd
from google.api_core.client_options import ClientOptions
PROJECT_ID = os.environ['PROJECT_ID']
VERSION_NAME = os.environ['VERSION_NAME']
MODEL_NAME = os.environ['MODEL_NAME']
# Define the format of your input data including unused columns (These are the columns from the census data files)
COLUMNS = (
    'age',
    'workclass',
    'fnlwgt',
    'education',
    'education-num',
    'marital-status',
    'occupation',
    'relationship',
    'race',
    'sex',
    'capital-gain',
    'capital-loss',
    'hours-per-week',
    'native-country',
    'income-level'
)
# Categorical columns are columns that need to be turned into a numerical value to be used by scikit-learn
CATEGORICAL_COLUMNS = (
    'workclass',
    'education',
    'marital-status',
    'occupation',
    'relationship',
    'race',
    'sex',
    'native-country'
)
# Load the training census dataset
with open('./census_data/adult.data', 'r') as train_data:
    raw_training_data = pd.read_csv(train_data, header=None, names=COLUMNS)
# Remove the column we are trying to predict ('income-level') from our features list
# Convert the Dataframe to a lists of lists
train_features = raw_training_data.drop('income-level', axis=1).as_matrix().tolist()
# Create our training labels list, convert the Dataframe to a lists of lists
train_labels = (raw_training_data['income-level'] == ' >50K').as_matrix().tolist()
# Load the test census dataset
with open('./census_data/adult.test', 'r') as test_data:
    raw_testing_data = pd.read_csv(test_data, names=COLUMNS, skiprows=1)
# Remove the column we are trying to predict ('income-level') from our features list
# Convert the Dataframe to a lists of lists
test_features = raw_testing_data.drop('income-level', axis=1).as_matrix().tolist()
# Create our training labels list, convert the Dataframe to a lists of lists
test_labels = (raw_testing_data['income-level'] == ' >50K.').as_matrix().tolist()
endpoint = 'https://us-central1-ml.googleapis.com'
client_options = ClientOptions(api_endpoint=endpoint)
service = googleapiclient.discovery.build('ml', 'v1', client_options=client_options)
name = 'projects/{}/models/{}'.format(PROJECT_ID, MODEL_NAME)
name += '/versions/{}'.format(VERSION_NAME)
# Due to the size of the data, it needs to be split in 2
first_half = test_features[:int(len(test_features)/2)]
second_half = test_features[int(len(test_features)/2):]
complete_results = []
for data in [first_half, second_half]:
    responses = service.projects().predict(
        name=name,
        body={'instances': data}
    ).execute()
    if 'error' in responses:
        print(responses['error'])
    else:
        complete_results.extend(responses['predictions'])
# Print the first 10 responses
for i, response in enumerate(complete_results[:10]):
    print('Prediction: {}\tLabel: {}'.format(response, test_labels[i]))