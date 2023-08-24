import random
import numpy as np
import pickle
import json
import nltk
from tensorflow.keras.models import load_model
from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
intents=json.loads(open('intents.json').read())
words=pickle.load(open('words.pkl','rb'))
classes=pickle.load(open('classes.pkl','rb'))
model=load_model('chatbot.h5')
app = Flask(__name__)
run_with_ngrok(app)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/get", methods=["POST"])


def clean_up_sentence(sentence):
        sentence_words=nltk.word_tokenize(sentence)
        sentence_words=[lemmatizer.lemmatize(word) for word in sentence_words]
        return sentence_words
def bag_of_words(sentence):
    sentence_words=clean_up_sentence(sentence)
    bag=[0]*len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word==w:
                bag[i]=1
    return np.array(bag)           
def predict(sentence):
    bow= bag_of_words(sentence)
    res=model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD=0.25
    result=[[1,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    result.sort(key=lambda x:x[1],reverse=True)
    return_list=[]
    for r in result:
        return_list.append({'intent':classes[r[0]],'probability':str(r[1])})
    return return_list    
def get_response(intents_list,intents_json):
    tag=intents_list[0]['intent']
    list_of_intents=intents_json['intents']
    for i in list_of_intents:
        if i['tag']==tag:
            results=random.choice(i['responses'])
            break
    return results
print("hii ")
while True:
    messgae=input('')
    ints=predict(messgae)
    res=get_response(ints,intents)
    
    print(res)

    
if __name__ == "__main__":
    app.run()



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




