from playsound import playsound
from pynput import keyboard
import msvcrt
"""Change the Path to wherever the note directory or to wherever all the keys are stored"""
def piano(notess):
    if(notess=="q"):
        playsound('/note/key01.mp3')
    if (notess == "w"):
        playsound('/note/key02.mp3')
    if (notess == "e"):
        playsound('/note/key03.mp3')
    if (notess == "r"):
        playsound('/note/key04.mp3')
    if (notess == "t"):
        playsound('/note/key05.mp3')
    if (notess == "y"):
        playsound('/note/key06.mp3')
    if (notess == "u"):
        playsound('/note/key07.mp3')
    if (notess == "i"):
        playsound('/note/key08.mp3')
    if (notess == "p"):
        playsound('/note/key09.mp3')
    if (notess == "a"):
        playsound('/note/key10.mp3')
    if (notess == "s"):
        playsound('/note/key11.mp3')
    if (notess == "d"):
        playsound('/note/key12.mp3')
    if (notess == "f"):
        playsound('/note/key13.mp3')
    if (notess == "g"):
        playsound('/note/key14.mp3')
    if (notess == "h"):
        playsound('/note/key15.mp3')
    if (notess == "j"):
        playsound('/note/key16.mp3')
    if (notess == "k"):
        playsound('/note/key17.mp3')
    if (notess == "l"):
        playsound('/note/key18.mp3')
    if (notess == "z"):
        playsound('/note/key19.mp3')
    if (notess == "x"):
        playsound('/note/key20.mp3')
    if (notess == "c"):
        playsound('/note/key21.mp3')
    if (notess == "v"):
        playsound('/note/key22.mp3')
    if (notess == "b"):
        playsound('/note/key23.mp3')
    if (notess == "n"):
        playsound('/note/key24.mp3')

while True:
    a = input()
    a.lower()
    if a == "quit":
        break
    else:
        piano(a)







