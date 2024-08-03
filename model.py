import tensorflow as tf
from tensorflow.keras import layers, models


def build_model(input_length):
    """
    Builds and compiles a neural network model.
    """
    model = models.Sequential()
    model.add(layers.Embedding(input_dim=10000, output_dim=128, input_length=input_length))
    model.add(layers.GlobalAveragePooling1D())
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    return model
