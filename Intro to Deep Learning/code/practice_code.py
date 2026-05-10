
#pandas to visualise and manipulate data
import pandas as pd

#keras and layers and tensorflow to generate neurons
from tensorflow import keras
from tensorflow.keras import layers

#visualise the fisrt 5 entries of the red wine dataset
red_wine = pd.read_csv("red wine dataset location")
print(red_wine.head())

#we see there are 12 columns
#valuses in the forst 11 columns determine value of "quality" ie the twelfth column

red_wine.shape # gives output (rows, columns)

#define a model
model = keras.Sequential([layers.Dense(units=1 , input_shape = [11])])

#number of outputs ie units
#number of inputs ie input_shape

w,b = model.weights
#weigths and biases are stored as tensors, the above line unpacks them
#weights are initislly random, trianig is the process wirhre we change the weights to fit the desired output



# here we define a model with 1 input layer , 2 hidden layers and 1 output layer
#multiple layers allow a model to learn non linar graphs as well
model = keras.Sequential([layers.Dense(units = 512 , activation = 'relu' , input_shape = [8]),
                          layers.Dense(units = 512 , activation = 'relu'),
                          layers.Dense(units = 512 , activation = 'relu'),
                          layers.Dense(units = 1)])

#somtime we dont want to apply actiavtion reiht after input computatiosn, so we can define it outside the dense also

#THIS
model = keras.Sequential([
    layers.Dense(32, activation='relu', input_shape=[8]),
    layers.Dense(32, activation='relu'),
    layers.Dense(1),
])

#IS THE SAME AS THIS
model = keras.Sequential([
    layers.Dense(32, input_shape=[8]),
    layers.Activation('relu'),
    layers.Dense(32),
    layers.Activation('relu'),
    layers.Dense(1),
])

#See the noteboks for sgd and else
