import streamlit as st
import pickle
import pandas as pd
import numpy as np
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string
ps = PorterStemmer()

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))


def preprocessing(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation and i.isalnum():
            y.append(ps.stem(i))

    return " ".join(y)


st.title("SMS Spam Detection ")
input = st.text_area("Enter the text")
if st.button('Predict'):
    preprocessed_text = preprocessing(input)
    vectorized_text = tfidf.transform([preprocessed_text])
    result = model.predict(vectorized_text)[0]
    if result == 1:
        st.header(":red[Spam]")
    else:
        st.header(":green[Not Spam]")
st.caption('List of messages :blue[messages] you can try:lollipop:')
Message = ['How are you? Long time no see!', 'Wanna go watch some movies? I got two tickets.', 'Congratulations, you won 1000$.', 'Not heard from U4 a while. Call 4 rude chat private line 01223585334 to cum. Wan 2C pics of me gettin shagged then text PIX to 8552. 2End send STOP 8552 SAM xxx	', 'Guess what! Somebody you know secretly fancies you! Wanna find out who it is? Give us a call on 09065394973 from Landline DATEBox1282EssexCM61XN 150p/min 18	', 'Then what about further plan?',
           'Come to me, sandra	. Your doing it again ... Going into your shell and unconsciously avoiding me ... You are making me unhappy :-(	', '\Gimme a few\" was &lt;#&gt; minutes ago', 'Buzz! Hey, my Love ! I think of you and hope your day goes well. Did you sleep in ? I miss you babe. I long for the moment we are together again*loving smile', 'In e msg jus now. U said thanks for gift.', 'SO IS TH GOWER MATE WHICH IS WHERE I AM!?! HOW R U MAN? ALL IS GOOD IN WALES ILL B BACK åÔMORROW. C U THIS WK? WHO WAS THE MSG 4? åÐ RANDOM!', 'Thanx 4 sending me home...']

df = pd.DataFrame(
    {'Messages': Message})

st.dataframe(df)
