import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY

def voice_input():
    rec = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('Listening.....')
        audio = rec.listen(source, timeout=5, phrase_time_limit=10)
    try:
        text = rec.recognize_google(audio)
        print("You said : ", text)
        return text
    except sr.UnknownValueError:
        print("Not able to get what you said, can you repeat again")
    except sr.RequestError as e:
        print("No response from Google Speech Recognition service")
        

def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    tts.save("Speech.mp3")

    
def llm_model_object(user_text):
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(user_text)
    
    result = response.text
    return result