from gtts import gTTS

def ToMP(text):
    inp = text

    myobj = gTTS(text=inp, lang="en", tld='us', slow=False)
    myobj.save("testaudio.mp3")
    return myobj #maybe
