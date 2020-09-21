import cv2
import numpy as np
import matplotlib.pyplot as plt
import PIL
import tkinter

def findnumberplate(path):
    return


window = tkinter.Tk()

window.title("번호판 인식")
# window.geometry("640x400+100+100")
window.resizable(False, False)

label = tkinter.Label(window, text="주소", anchor="nw")
label.grid(column=0, row=0)

strpath = tkinter.Entry(window)
strpath.grid(column=1, row=0)

btn = tkinter.Button(window, text="가져오기", command=findnumberplate())
btn.grid(column=2, row=0)

window.mainloop()