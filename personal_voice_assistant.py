from urllib import response
from rich import reconfigure
import speech_recognition as sr
import pyttsx3
import requests
import datetime

engine = pyttsx3.init()
print("hello!! I'm your personal assistant how can I help you??")
engine.say("hello!! I'm your personal assistant how can I help you??")
engine.runAndWait()

while True:
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("please speak something..")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            text = recognizer.recognize_google(  # type: ignore
                audio, language="en-US").lower()  # type: ignore
            print("you: ", text)
        except sr.UnknownValueError:
            print("Assistant : Sorry,I did not understand that ")
            engine.say("assistant : Sorry,I did not understand that")

        if "weather" in text:
            city = "delhi"
            api_key = "1d9b31356ae53b2aac33115d8fa2572c"
            url = f"https://api.openweathermap.org/data/2.5/weather?q={
                city}&appid={api_key}&units='metric"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather = data["weather"][0]["description"]
                temp = data["main"]["temp"]
                print(f"assistant: The weather in {city} is{
                      weather} with a temperature of {temp} C")
                engine.say(f"The weather in {city} is  {
                           weather} with a temperature of {temp} C")
            else:
                engine.say("sorry, I couldn't fetch the weather")
                print("sorry, I couldn't fetch the weather ")
            engine.runAndWait()

        elif "news" in text:
            api_key_news = "3e2f8640500d46f39406aa6bf8a2a48b"
            url_news = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key_news}"
            response=requests.get(url_news)
            if response.status_code ==200:
                articles =response.json().get("articles",[])
                headline=[article['title'] for article in articles[:5]]
                print("Assistant : here are top 5 news headlines")
                print(headline)
                for i,headline in enumerate(headline,1):
                    print(f"{i}.{headline}")
                engine.say("here are top 5 news headlines:"+",".join(headline))
        
        elif "time" in text:
            time = datetime.datetime.now().strftime("%I:%M %p")
            print(f"Assistant :The current time is {time}.")
            engine.say(f"the current time is {time}.")
            engine.runAndWait()
        
        elif "exit" or "quit" in text:
            break

        else :
            print("Assistant : I'm not sure how to help you with that.")
            engine.say("Assistant : I'm not sure how to help you with that.")
            engine.runAndWait()