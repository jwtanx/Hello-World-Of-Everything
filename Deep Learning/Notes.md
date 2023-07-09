# Deep Learning Journal: TENSORFLOW
Notes and reference links

# General steps
- https://analyticsindiamag.com/the-7-key-steps-to-build-your-machine-learning-model/

---

# Number of nodes and hidden layers
- https://www.researchgate.net/post/How-to-decide-the-number-of-hidden-layers-and-nodes-in-a-hidden-layer

# Activation functions
- [Some graphs for these activation functions](https://www.analyticsvidhya.com/blog/2020/01/fundamentals-deep-learning-activation-functions-when-to-use-them/)
- [List of activation functions and their derivative](https://www.analyticsvidhya.com/blog/2021/04/activation-functions-and-their-derivatives-a-quick-complete-guide/)

# Loss
- [The difference between categorical crossentropy and sparse categorical crossentropy](https://stackoverflow.com/questions/58565394/what-is-the-difference-between-sparse-categorical-crossentropy-and-categorical-c)
- https://datascience.stackexchange.com/questions/41921/sparse-categorical-crossentropy-vs-categorical-crossentropy-keras-accuracy
- [Multiclass vs multilabel](https://fmorenovr.medium.com/sparse-categorical-cross-entropy-vs-categorical-cross-entropy-ea01d0392d28)

# Metrics
- [Accuracy, Precision, Recall or F1](https://towardsdatascience.com/accuracy-precision-recall-or-f1-331fb37c5cb9)
- https://towardsdatascience.com/whats-the-deal-with-accuracy-precision-recall-and-f1-f5d8b4db1021
- https://medium.com/analytics-vidhya/confusion-matrix-accuracy-precision-recall-f1-score-ade299cf63cd
- 

---

# Recurrent Neural Network
## Note
- https://towardsdatascience.com/recurrent-neural-networks-by-example-in-python-ffd204f99470

## Tutorial
- [Github RNN tutorials with docker](https://github.com/WillKoehrsen/recurrent-neural-networks)

# Steps for building a model
1. Importing tensorflow, keras and some helper libraries like numpy and matplotlib
2. Load the data, specificatlly (x_train, y_train), (x_test, y_test), mostly a grayscale image for each pixel range between 0 to 255
3. Setting up the classes name in a list
4. Data preprocessing, divide all the pixel value by 255.0 into floating number for better computation, do this for all the x_train and x_test
5. Once divided, you will see all the values of the pixels are now ranged between 0 and 1, its floating point now
6. Build the model
```py
model = keras.Sequential([keras.layers.Flatten(input_shape=(28, 28)),  # The input layers, including the width and the height of the image, here is 28px x 28px
                          keras.layers.Dense(128, activation="relu"),  # The hidden layers
                          keras.layers.Dense(10, activation="softmax") # The output, the 10 is based on the number of classification, softmax because it is multiclass
])
```

7. Compiling the model
```py
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
```

8. Training / Fitting the model
```py
model.fit(x_train, y_train, epochs=10) # epoch = number of passes of the entire training dataset the machine learning algorithm has completed
```

9. Evaluating the model
```py
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=True) # Verbose True to output the log
```

10. Making prediction
```py
pred = model.predict(x_test)

# Getting the max probability for the first prediction
np.argmax(pred[0])

# Testing only one image
pred_1 = model.predict(np.array(x_test[0])) # NOTE: Make sure you have the np.array([])
```

# Extra notes
## Setting the threshold
[Reference](https://stackoverflow.com/questions/61342716/changing-thresholds-in-the-sigmoid-activation-in-neural-networks)
```py
predictions = probabilities > 0.8
```

Different thresholds for each class
```py
# Pytorch
thresholds = torch.tensor([0.1, 0.1, 0.8]).unsqueeze(0)
predictions = probabilities > thresholds
```

## Save model
```py
# https://www.tensorflow.org/guide/keras/save_and_serialize
def get_model():
    # Create a simple model.
    inputs = keras.Input(shape=(32,))
    outputs = keras.layers.Dense(1)(inputs)
    model = tf.keras.Model(inputs=inputs, outputs=outputs, name="Model_Name_Here")
    model.compile(optimizer="adam", loss="mean_squared_error")
    return model


model = get_model()

# Train the model.
test_input = np.random.random((128, 32))
test_target = np.random.random((128, 1))
model.fit(test_input, test_target)

# Calling `save('my_model')` creates a SavedModel folder `my_model`.
model.save("saved_model_path")

# Alternative method
tf.keras.models.save_model(model, "saved_model_path")

```

## Load model
```py
# It can be used to reconstruct the model identically.
reconstructed_model = tf.keras.models.load_model("my_model")

# Let's check:
np.testing.assert_allclose(
    model.predict(test_input), reconstructed_model.predict(test_input)
)

# The reconstructed model is already compiled and has retained the optimizer
# state, so training can resume:
reconstructed_model.fit(test_input, test_target)
```

## Loading model with custom object (metric / loss)
Sometimes, if you are using tensorflow addons object for the metrics, when you load the model, you might have a problem of loading the custom object, hence, you will need to change the parameter for the compile in the load_model to False first, then compile it again.
[Source](https://github.com/jakeret/unet/issues/8#issuecomment-787736353)
```py
# First method: Better approach
# https://www.tensorflow.org/api_docs/python/tf/keras/models/load_model
reconstructed_model = tf.keras.models.load_model("model_path", compile=False)

# Then compile again
reconstructed_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy', 'mean_squared_error'])
print(reconstructed_model.summary())

# Another way would be loading with the custom metric used before
# This method is not good because the metric cannot be get from the get_config of the model
# https://stackoverflow.com/questions/64797096/load-keras-model-with-custom-metrics-and-custom-loss
import tensorflow_addons as tfa
new_model = tf.keras.models.load_model("what", custom_objects={"MultiLabelConfusionMatrix": tfa.metrics.MultiLabelConfusionMatrix})
```

## Getting the summary of the model
```py
model.summary(
    line_length=None,
    positions=None,
    print_fn=None,
    expand_nested=True,
    show_trainable=True,
)
```

## Learning rate
```py
# Setting the learning rate
lr_schedule = keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate, decay_steps=100000, decay_rate=0.96, staircase=True
)

# pip install tensorflow-addons
import tensorflow_addons as tfa
f1 = tfa.metrics.F1Score(num_classes=2, average=None)

model=(..)
model.compile(
    loss="binary_crossentropy",
    optimizer=tfa.optimizers.AdamW(learning_rate=lr_schedule,weight_decay = 0.0001),
    metrics=["acc",'AUC',f1],
)
```

## Splitting - K-Fold
[Reference](https://github.com/christianversloot/machine-learning-articles/blob/main/how-to-use-k-fold-cross-validation-with-keras.md)
```py
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.losses import sparse_categorical_crossentropy
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import KFold
import numpy as np

# Merge inputs and targets
inputs = np.concatenate((input_train, input_test), axis=0)
targets = np.concatenate((target_train, target_test), axis=0)

# Define the K-fold Cross Validator
kfold = KFold(n_splits=num_folds, shuffle=True)

# K-fold Cross Validation model evaluation
fold_no = 1

for train, test in kfold.split(inputs, targets):
    # Define the model architecture
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(no_classes, activation='softmax'))

    # Compile the model
    model.compile(loss=loss_function,
                optimizer=optimizer,
                metrics=['accuracy'])


    # Generate a print
    print('------------------------------------------------------------------------')
    print(f'Training for fold {fold_no} ...')

    # Fit data to model
    history = model.fit(inputs[train], targets[train],
              batch_size=batch_size,
              epochs=no_epochs,
              verbose=verbosity)

    # Generate generalization metrics
    scores = model.evaluate(inputs[test], targets[test], verbose=0)
    print(f'Score for fold {fold_no}: {model.metrics_names[0]} of {scores[0]}; {model.metrics_names[1]} of {scores[1]*100}%')
    acc_per_fold.append(scores[1] * 100)
    loss_per_fold.append(scores[0])

    # Increase fold number
    fold_no = fold_no + 1
```

## Metrics
```py
# Taken from catering imbalanced dataset from Tensorflow tutorial
# https://www.tensorflow.org/tutorials/structured_data/imbalanced_data
METRICS = [
      tf.keras.metrics.TruePositives(name='tp'),
      tf.keras.metrics.FalsePositives(name='fp'),
      tf.keras.metrics.TrueNegatives(name='tn'),
      tf.keras.metrics.FalseNegatives(name='fn'), 
      tf.keras.metrics.BinaryAccuracy(name='accuracy'),
      tf.keras.metrics.Precision(name='precision'),
      tf.keras.metrics.Recall(name='recall'),
      tf.keras.metrics.AUC(name='auc'),
      tf.keras.metrics.AUC(name='prc', curve='PR'), # precision-recall curve
]


```

# MULTI-CLASS CLASSIFICATION


# MULTI-LABEL CLASSIFICATION
1. Metrics
a. Confusion Matrics
[Reference](https://stackoverflow.com/questions/53886370/multi-class-multi-label-confusion-matrix-with-sklearn)
[Reference](https://www.tensorflow.org/api_docs/python/tf/keras/metrics)
```py
import numpy as np
from sklearn.metrics import confusion_matrix

y_true = np.array([[0,0,1], [1,1,0],[0,1,0]])
y_pred = np.array([[0,0,1], [1,0,1],[1,0,0]])

labels = ["A", "B", "C"]

conf_mat_dict={}

for label_col in range(len(labels)):
    y_true_label = y_true[:, label_col]
    y_pred_label = y_pred[:, label_col]
    conf_mat_dict[labels[label_col]] = confusion_matrix(y_pred=y_pred_label, y_true=y_true_label)


for label, matrix in conf_mat_dict.items():
    print("Confusion matrix for label {}:".format(label))
    print(matrix)
```

2. Threshold
```py
preds = model.predict(X)

# Let's say that the preds are in np.array format
# preds = [0.23234, 0.418237, 0.7273695, 0.56834]

thresh = 0.5
final_preds = (preds > thresh).astype(int) # [0, 0, 1, 1] This will be 1 because the booleans are converted into 1 (True) / 0 (False)

```

3. Label Smoothing
```py
import tensorflow as tf

tf.keras.losses.binary_crossentropy(
                  y_true, y_pred,
                  from_logits=False,
                  label_smoothing=0) # Insert a factor like 0.3 for the label_smoothing parameter
```


Sklearn.classification_report(y_true, y_pred)

