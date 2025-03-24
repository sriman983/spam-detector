import pickle

# Load the trained model and vectorizer
with open('spam_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Test the model with a new email
test_email = ["Congratulations! You've won a free lottery. Claim your prize now!"]
test_email_vec = vectorizer.transform(test_email)
prediction = model.predict(test_email_vec)

# Print result
result = "Spam" if prediction[0] == 1 else "Not Spam"
print(f"Prediction: {result}")