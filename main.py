from data_ingestion import get_data
from preprocess import preprocess_data
from model import build_model
from feedback import handle_feedback_and_update

# Collect and preprocess initial data
data = get_data()
if data:
    X, y, input_length = preprocess_data(data)

    # Build and train the model
    model = build_model(input_length)
    model.fit(X, y, epochs=5, batch_size=32)

    # Simulate getting feedback and updating the model
    urls = ["http://example.com", "http://carter.tech"]
    handle_feedback_and_update(urls, input_length)

    # Function to train with new data
    def train_with_new_data(new_data):
        new_X, new_y, _ = preprocess_data(new_data, input_length)
        model.fit(new_X, new_y, epochs=1, batch_size=1)
