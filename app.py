from flask import Flask
from flask import render_template
from flask import url_for, flash, redirect, request
app = Flask(__name__)

###################################################
# for Dialog.html
import speech_recognition as sr
import playsound # to play mp3 files # Install using pip install playsound
from gtts import gTTS # This module is imported so that we can play the converted audio
import os
###################################################
# For nlp.html
from tfidfnlpcode import *
###################################################
@app.route("/")
def main():
    return render_template('index.html')
@app.route("/dialog", methods=['GET', 'POST'])
def dialog():
    text = ""
    result = ""
    start = ""
    path = ""
    score = ""
    if request.method == 'POST':
        r = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                # read the audio data from the default microphone
                audio_data = r.record(source, duration=5)
                #print("Recognizing...")
                start = "Recognizing..."
                # convert speech to text
                text = r.recognize_google(audio_data)
            except:
                print("error")
            else:
                text = text
                start = ""
                reply = []
                score = []
                reply, score = Talk_To_Javris(str(text))
                result = reply
                language = 'en'
                myobj = gTTS(text=result, lang=language, slow=False)
                myobj.save("welcome.mp3")
                playsound.playsound('welcome.mp3', True)
                os.remove('welcome.mp3')

    return render_template('dialog.html', text = text, result = result, start = start, score = score)

@app.route("/nlp", methods=['GET', 'POST'])
def nlp():
    news = ""
    result = ""
    sentence = ""
    score = ""
    # start = time.time()
    if request.method == 'POST':
        sentence = request.form['subject']
    if (sentence.lower() == 'bye'):
        result = "Bye! Take Case"
    elif (sentence.lower() == 'thank you'):
        result = "Its my pleasure to help you"
    elif (sentence.lower() == 'Hello' or sentence.lower() == 'Hi' ):
        result = "Hi, How can I help you"
    else:
        reply = []
        score = []
        news = []
        reply, score = Talk_To_Javris(str(sentence))
        result = reply
        score = score
    return render_template('nlp.html', result = result , reply = reply, score = score)

if __name__ == "__main__":
    app.run(debug=True)
