import tkinter
from pygame import mixer
root = tkinter.Tk()
mixer.init()
mixer.music.load("cant_move.wav")
mixer.music.play()
root.mainloop()
