from data_ingestion import get_data
from preprocess import preprocess_data
from model import build_model

# Collect and preprocess initial data
data = get_data()
if data:
    X, y, input_length = preprocess_data(data)

    # Build and train the model
    model = build_model(input_length)
    model.fit(X, y, epochs=5, batch_size=32)

# Function to train with new data
def train_with_new_data(new_data, input_length):
    new_X, new_y, _ = preprocess_data(new_data, input_length)
    model.fit(new_X, new_y, epochs=1, batch_size=1)
