import speech_recognition as sr
from time import sleep


def take():
    r = sr.Recognizer()

    #joy-audio is my recorded speech:
    audioFile = sr.AudioFile('joy-audio.wav')
    with audioFile as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
        print("Recognising your speech...")

    try:
        query = r.recognize_google(audio, language='en-Us')
        sleep(1)
        print("\n")
        print(query)

    except Exception as e:
        print("An error occured. Please enable internet connection")

        return "None"

    return query

query = take()
sleep(10)
print("Quitting the program now")
sleep(3)
