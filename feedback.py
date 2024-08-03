from training import model, train_with_new_data
from preprocess import preprocess_data

def get_user_feedback(url):
    """
    Placeholder function to get user feedback.
    """
    feedback = input(f"Is the URL {url} safe for kids? (yes/no): ")
    return 1 if feedback == "yes" else 0

def update_model(model, url, label, input_length):
    """
    Updates the model with new user feedback.
    """
    new_data = [(url, "", label)]
    new_X, new_y, _ = preprocess_data(new_data, input_length)
    model.fit(new_X, new_y, epochs=1, batch_size=1)

# Function to handle feedback and update model
def handle_feedback_and_update(urls, input_length):
    for url in urls:
        label = get_user_feedback(url)
        update_model(model, url, label, input_length)
