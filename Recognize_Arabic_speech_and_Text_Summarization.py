import speech_recognition
import arabic_reshaper
from bidi.algorithm import get_display
from tkinter import *
from tkinter import font
from summa.summarizer import  summarize



root = Tk()
root.geometry("500x300")
root.title("التعرف على الكلام و تلخيصه")

recognizer = speech_recognition.Recognizer()  #In here we have created the object of our Recognizer and also we are using Microphone as source
def voiceReco():

    with speech_recognition.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.2) #also we need to add this line of code, it is used for removing noises if we have in the sound
        audio = recognizer.listen(mic)
        text = recognizer.recognize_google(audio, language='ar-AR')#And in here we are recognizing the speech using Google Speech
        print(text)


        textF.delete("1.0", "end")
        textF.insert(END, text)
        textF.tag_add("center", 1.0, "end")

        file = open('text.txt', 'a', encoding='utf-8')
        file.writelines(text + '\n')
        file.close()



        # write audio
        with open("recorded.wav", "wb") as f: #If you need to record your audio than you can use this code
            f.write(audio.get_wav_data())



def SummarizeُText():
            text = 'text.txt'
            summary = summarize(text, ratio=0.20, language="arabic")
            print(summary)





ButtonFont = font.Font(size=20)
LabelFont = font.Font(size=15)

Label(root, text="النص سوف يظهر هنا", font=LabelFont).pack()

textF = Text(root, height=5, width=52, font=LabelFont)
textF.tag_configure("center", justify='center')
textF.pack()

Button(root, text='التحدث', font=ButtonFont, command=voiceReco).place(x=150, y=200)
Button(root, text='الملخص', font=ButtonFont,command=SummarizeُText).place(x=250, y=200)


root.mainloop()