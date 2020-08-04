from gtts import gTTS
import os

def sound_function(text):
    # text= " I was wondering that afterall these years you'd like to meet."

    output= gTTS(text, lang="en", slow=False)

    sound=output.save("output.mp3")

    return sound

    # os.system("start output.mp3")