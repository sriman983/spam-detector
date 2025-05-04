from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Load model and vectorizer
with open(r'C:\Users\srima\OneDrive\Desktop\Project\spam_model.pkl', 'rb') as model_file:
     model = pickle.load(model_file)

with open(r'C:\Users\srima\OneDrive\Desktop\Project\vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

@app.route('/')
def home():
    return render_template('index.html')  # your HTML page

@app.route('/predict', methods=['POST'])
def predict():
    email_text = request.form['email_text']

    email_vector = vectorizer.transform([email_text])
    prediction = model.predict(email_vector)[0]
    probability = model.predict_proba(email_vector)[0][1] * 100  # probability as percentage

    # Return JSON result
    return jsonify({
        'prediction': 'Spam' if prediction == 1 else 'Not Spam',
        'spamProbability': round(probability, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)
