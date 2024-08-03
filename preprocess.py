import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def preprocess_data(data, max_length=100):
    """
    Preprocesses the data for the neural network.
    """
    urls, contents, labels = zip(*data)
    vectorizer = CountVectorizer(max_features=10000, token_pattern=r"(?u)\b\w+\b")
    X = vectorizer.fit_transform(urls).toarray()
    X = pad_sequences(X, maxlen=max_length, padding='post')
    y = np.array([1 if label == "yes" else 0 for label in labels])
    return X, y, max_length
