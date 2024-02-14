import requests
import json

# SPEAK FUNCTION
def speak(str):
    from win32com.client import Dispatch
    s = Dispatch("SAPI.SpVoice")
    s.Speak(str)

if __name__ == '__main__':
    speak("Today's News")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=3d13ed54184d41a6a69854ef3c85d121"
    news = requests.get(url).text
    news=json.loads(news)
    print(news["status"])
    # print(news["articles"])
    na = news['articles']
    for a in na:
        speak(a['title'])
        speak(a['description'])
        speak("Moving on to next news.")

    speak("thanks for listeing. Make sure to come tomorrow for latest updates.")
