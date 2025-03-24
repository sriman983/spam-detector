from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Load model and vectorizer
with open('spam_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    email_text = request.form['email_text']
    email_vec = vectorizer.transform([email_text])
    prediction = model.predict(email_vec)[0]
    probability = model.predict_proba(email_vec)[0][1]

    return jsonify({
        'prediction': "Spam" if prediction == 1 else "Not Spam",
        'probability': round(probability, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)