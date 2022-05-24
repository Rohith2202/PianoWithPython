from playsound import playsound
from pynput import keyboard
import msvcrt

def piano(notess):
    if(notess=="q"):
        playsound('C:/Users/ROHITH/Desktop/PianoSound/note/key01.mp3')
    if (notess == "w"):
        playsound('C:/Users/ROHITH/Desktop/PianoSound/note/key02.mp3')
    if (notess == "e"):
        playsound('C:/Users/ROHITH/Desktop/PianoSound/note/key03.mp3')
    if (notess == "r"):
        playsound('C:/Users/ROHITH/Desktop/PianoSound/note/key04.mp3')
    if (notess == "t"):
        playsound('C:/Users/ROHITH/Desktop/PianoSound/note/key05.mp3')
    if (notess == "y"):
        playsound('C:/Users/ROHITH/Desktop/PianoSound/note/key06.mp3')
    if (notess == "u"):
        playsound('C:/Users/ROHITH/Desktop/PianoSound/note/key07.mp3')
    if (notess == "i"):
        playsound('C:/Users/ROHITH/Desktop/PianoSound/note/key08.mp3')
    if (notess == "p"):
        playsound('C:/Users/ROHITH/Desktop/PianoSound/note/key09.mp3')
    if (notess == "a"):
        playsound('C:/Users/ROHITH/Desktop/PianoSound/note/key10.mp3')
    if (notess == "s"):
        playsound('C:/Users/ROHITH/Desktop/PianoSound/note/key11.mp3')
    if (notess == "d"):
        playsound('C:/Users/ROHITH/Desktop/PianoSound/note/key12.mp3')
    if (notess == "f"):
        playsound('C:/Users/ROHITH/Desktop/PianoSound/note/key13.mp3')
    if (notess == "g"):
        playsound('C:/Users/ROHITH/Desktop/PianoSound/note/key14.mp3')
    if (notess == "h"):
        playsound('C:/Users/ROHITH/Desktop/PianoSound/note/key15.mp3')
    if (notess == "j"):
        playsound('C:/Users/ROHITH/Desktop/PianoSound/note/key16.mp3')
    if (notess == "k"):
        playsound('C:/Users/ROHITH/Desktop/PianoSound/note/key17.mp3')
    if (notess == "l"):
        playsound('C:/Users/ROHITH/Desktop/PianoSound/note/key18.mp3')
    if (notess == "z"):
        playsound('C:/Users/ROHITH/Desktop/PianoSound/note/key19.mp3')
    if (notess == "x"):
        playsound('C:/Users/ROHITH/Desktop/PianoSound/note/key20.mp3')
    if (notess == "c"):
        playsound('C:/Users/ROHITH/Desktop/PianoSound/note/key21.mp3')
    if (notess == "v"):
        playsound('C:/Users/ROHITH/Desktop/PianoSound/note/key22.mp3')
    if (notess == "b"):
        playsound('C:/Users/ROHITH/Desktop/PianoSound/note/key23.mp3')
    if (notess == "n"):
        playsound('C:/Users/ROHITH/Desktop/PianoSound/note/key24.mp3')

while True:
    a = input()
    a.lower()
    if a == "quit":
        break
    else:
        piano(a)







