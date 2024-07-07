# Spam-SMS-classifier
This repository contains a Naive Bayes classifier for detecting whether an SMS message is spam or ham. This project was built to explore text classification techniques and understand the application of machine learning in natural language processing (NLP).

Table of Contents
Introduction
Features
Installation
Usage
Data
Model
Results
Contributing
License
Introduction
Spam messages are unsolicited messages sent in bulk, often for advertising or phishing purposes. This classifier helps in distinguishing between spam and legitimate (ham) messages using a Naive Bayes algorithm. Naive Bayes is a probabilistic classifier based on Bayes' theorem with strong independence assumptions between the features.

Features
Text Preprocessing: Tokenization, stop-word removal, and text normalization.
Model Training: Uses a Naive Bayes classifier for training.
Evaluation: Accuracy, precision, recall, and F1-score metrics.
Installation
To run this project locally, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/alokranjan609/Spam-SMS-classifier
cd Spam-SMS-classifier
python -m streamlit app.py



Data Format: The dataset should be a CSV file with two columns: label and message.
Model
The Naive Bayes classifier is trained using the following steps:

Preprocessing: Cleaning and preparing the text data.
Feature Extraction: Converting text into numerical features using techniques like TF-IDF.
Model Training: Fitting the Naive Bayes classifier on the training data.
Evaluation: Assessing the model performance on a test set.
Results
The classifier is evaluated using standard metrics:

Accuracy: The percentage of correctly classified messages.
Precision: The ratio of true positive predictions to the total predicted positives.
Recall: The ratio of true positive predictions to the total actual positives.
F1-score: The harmonic mean of precision and recall.
Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch.
Make your changes.
Submit a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

