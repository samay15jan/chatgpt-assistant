import speech_recognition as aud
import time
import openai
import os
from gtts import gTTS
from io import BytesIO
import pygame

openai.api_key = ""

text = input()

completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}],
        temperature=0.5,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )

result = co
mpletion.choices[0].message
text = result["content"]
print(text)

tts = gTTS(text=text, lang='en', slow=False)

file = BytesIO()
tts.write_to_fp(file)
file.seek(0)

pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue


