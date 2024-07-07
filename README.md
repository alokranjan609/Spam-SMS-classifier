# SMS Spam/Ham Classifier

This repository contains a Naive Bayes classifier for detecting whether an SMS message is spam or ham. This project was built to explore text classification techniques and understand the application of machine learning in natural language processing (NLP). A web interface for the classifier is built using Streamlit.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Data](#data)
- [Model](#model)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Spam messages are unsolicited messages sent in bulk, often for advertising or phishing purposes. This classifier helps in distinguishing between spam and legitimate (ham) messages using a Naive Bayes algorithm. Naive Bayes is a probabilistic classifier based on Bayes' theorem with strong independence assumptions between the features.

## Features

- **Text Preprocessing**: Tokenization, stop-word removal, and text normalization.
- **Model Training**: Uses a Naive Bayes classifier for training.
- **Evaluation**: Accuracy, precision, recall, and F1-score metrics.
- **Web Interface**: A simple web interface using Streamlit.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/alokranjan609/Spam-SMS-classifier
    cd Spam-SMS-classifier
    ```

2. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.**Running the applocation**
   ```bash
   pythom -m streamlit run app.py
   ```



## Data

The dataset used for training and evaluation is a collection of SMS messages labeled as spam or ham. The dataset should be placed in the `data/` directory.

- **Data Format**: The dataset should be a CSV file with two columns: `label` and `message`.

## Model

The Naive Bayes classifier is trained using the following steps:

1. **Preprocessing**: Cleaning and preparing the text data.
2. **Feature Extraction**: Converting text into numerical features using techniques like TF-IDF.
3. **Model Training**: Fitting the Naive Bayes classifier on the training data.
4. **Evaluation**: Assessing the model performance on a test set.

## Results

The classifier is evaluated using standard metrics:

- **Accuracy**: The percentage of correctly classified messages.
- **Precision**: The ratio of true positive predictions to the total predicted positives.
- **Recall**: The ratio of true positive predictions to the total actual positives.
- **F1-score**: The harmonic mean of precision and recall.

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**.
2. **Create a new branch**.
3. **Make your changes**.
4. **Submit a pull request**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
