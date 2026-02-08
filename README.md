📧 Spam Detection Web Application

A Machine Learning–based Spam Email/SMS Detection System built using Python, Flask, and Scikit-learn.
This application classifies messages as Spam or Ham (Not Spam) through a simple web interface.

🚀 Features

✅ Classifies messages as Spam or Ham

🧠 Machine Learning model trained on real spam dataset

🌐 Flask-based web application

⚡ Fast predictions using saved model & vectorizer

📂 Well-organized project structure

🎯 Beginner-friendly and easy to understand

🛠️ Technologies Used

Python

Flask

Scikit-learn

Pandas

NumPy

HTML, CSS, JavaScript

📁 Project Structure
Project/
│── app.py
│── train_model.py
│── test_model.py
│── spam.csv
│── spam_model.pkl
│── vectorizer.pkl
│── requirements.txt
│── Procfile
│
├── templates/
│   └── index.html
│
├── static/
│   ├── styles.css
│   ├── script.js
│   └── logo.png
│
└── venv/

📊 Dataset Information

Dataset file: spam.csv

Classes:

spam → Unwanted or promotional messages

ham → Genuine messages

⚙️ Installation & Execution Steps
Step 1: Clone the repository
git clone https://github.com/sriman983/spam-detector.git
cd spam-detector

Step 2: Create a virtual environment
python -m venv venv
venv\Scripts\activate

Step 3: Install dependencies
pip install -r requirements.txt

Step 4: Run the Flask application
python app.py

Step 5: Open in browser
http://127.0.0.1:5000

🧪 Working of the System

User enters a message in the web interface

The text is converted into numerical form using a vectorizer

The trained ML model predicts the class

Output is displayed as Spam or Ham

📸 Example

Input:

Congratulations! You have won a free prize. Click now!


Output:

Spam

📌 Future Enhancements

Improve UI/UX design

Deploy application on cloud (Render / Vercel)

Add accuracy comparison with multiple models

Make application mobile responsive

Add user authentication

👨‍💻 Author

Sriman
GitHub Profile: https://github.com/sriman983
