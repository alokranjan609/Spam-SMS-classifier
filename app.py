# from flask import Flask,render_template,request
import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
import string

nltk.download('stopwords')
nltk.download('punkt')

from nltk import PorterStemmer
ps=PorterStemmer()
nltk.download('stopwords')
import string

def transform_text(text):
  text=text.lower()
  text=nltk.word_tokenize(text)

  y=[]
  for i in text:
    if i.isalnum():
      y.append(i)
  text=y[:]
  y.clear()
  for i in text:
    if i not in stopwords.words('english') and i not in string.punctuation:
      y.append(i)

  text=y[:]
  y.clear()

  for i in text:
    y.append(ps.stem(i))

  return " ".join(y)
tfifd=pickle.load(open('vectorized.pkl','rb'))
model=pickle.load(open('model_saved.pkl','rb'))

st.title("Email/SMS Spam classifier")

input_sms=st.text_area("Enter the Message")

if st.button('Predict'):

##preprocess
  transform_sms=transform_text(input_sms)
##vectorize
  vector_input=tfifd.transform([transform_sms])
##predict
  result=model.predict(vector_input)[0]
 ##display
  if result==1:
    st.header("spam")
  else:
    st.header("Not Spam")

