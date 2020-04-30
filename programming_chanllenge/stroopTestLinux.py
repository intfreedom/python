#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tkinter
from tkinter import *
import random
import time
from stroopTestResult import StroopTestResult
win = tkinter.Tk()
win.title("StroopTest")
win.geometry("750x500+100+20")

L = ['Red', 'Orange', 'Yellow', 'Green', 'Cyan', 'Blue', 'Purple']
SubjectInformationList = ["WenjunLiu", 18]
ImageTextList = []
ImageFgList = []
ImageClickTimeList = []
ClickAnswerList = []
# using dictionaries (Python) for data storage
D = {SubjectInformationList[0]: {"Information": SubjectInformationList,
                       "ImageText": ImageTextList,
                       "ImageFg": ImageFgList,
                       "ImageClickTime": ImageClickTimeList,
                       "ClickAnswer": ClickAnswerList
                     }}

class ChangeImage(object):
    def __init__(self, ImageText, ImageFg, ClickTime):
        self.ImageText = ImageText
        self.ImageFg = ImageFg
        self.ClickTime = "%.2f" % time.clock()
    def changeImageText(self):
        label1["text"] = self.ImageText
        print(label1["text"])
    def changeImageFg(self):
        label1["fg"] = self.ImageFg
        print(label1["fg"])
    def changeClickTime(self):
        print("%.2f" % time.clock())
    def dateCount(self):
        ImageTextList.append(self.ImageText)
        ImageFgList.append(self.ImageFg)
        ImageClickTimeList.append(self.ClickTime)
        print(ImageTextList)
        print(ImageFgList)
        print(ImageClickTimeList)

def func1():
    ClickButton1 = ChangeImage(random.choice(L), random.choice(L), time.clock())
    ClickButton1.changeImageText()
    ClickButton1.changeImageFg()
    ClickButton1.changeClickTime()
    ClickButton1.dateCount()
    ClickAnswerList.append("Red")
    print(ClickAnswerList)

def func2():
    ClickButton2 = ChangeImage(random.choice(L), random.choice(L), time.clock())
    ClickButton2.changeImageText()
    ClickButton2.changeImageFg()
    ClickButton2.changeClickTime()
    ClickButton2.dateCount()
    ClickAnswerList.append("Orange")
    print(ClickAnswerList)

def func3():
    ClickButton3 = ChangeImage(random.choice(L), random.choice(L), time.clock())
    ClickButton3.changeImageText()
    ClickButton3.changeImageFg()
    ClickButton3.changeClickTime()
    ClickButton3.dateCount()
    ClickAnswerList.append("Yellow")
    print(ClickAnswerList)

def func4():
    ClickButton4 = ChangeImage(random.choice(L), random.choice(L), time.clock())
    ClickButton4.changeImageText()
    ClickButton4.changeImageFg()
    ClickButton4.changeClickTime()
    ClickButton4.dateCount()
    ClickAnswerList.append("Green")
    print(ClickAnswerList)

def func5():
    ClickButton5 = ChangeImage(random.choice(L), random.choice(L), time.clock())
    ClickButton5.changeImageText()
    ClickButton5.changeImageFg()
    ClickButton5.changeClickTime()
    ClickButton5.dateCount()
    ClickAnswerList.append("Cyan")
    print(ClickAnswerList)

def func6():
    ClickButton6 = ChangeImage(random.choice(L), random.choice(L), time.clock())
    ClickButton6.changeImageText()
    ClickButton6.changeImageFg()
    ClickButton6.changeClickTime()
    ClickButton6.dateCount()
    ClickAnswerList.append("Blue")
    print(ClickAnswerList)

def func7():
    ClickButton7 = ChangeImage(random.choice(L), random.choice(L), time.clock())
    ClickButton7.changeImageText()
    ClickButton7.changeImageFg()
    ClickButton7.changeClickTime()
    ClickButton7.dateCount()
    ClickAnswerList.append("Purple")
    print(ClickAnswerList)

def SubjectInformation():
    SubjectInformationList[0] = entry2.get()
    SubjectInformationList[1] = entry3.get()
    print(SubjectInformationList)

def PlotResults():
    sameCorrect = 0
    sameError = 0
    diffCorrect = 0
    diffError = 0
    sameClickTime = 0
    diffClickTime = 0
    sameNumberCount = 0
    diffNumeberCount = 0
    for n in range(len(ImageTextList)-1):
        if ImageTextList[n] == ImageFgList[n]:
            if ClickAnswerList[n+1] == ImageTextList[n]:
                sameCorrect += 1
            else:
                sameError += 1
            sameClickTime += float(ImageClickTimeList[n+1])-float(ImageClickTimeList[n])
            sameNumberCount += 1
        else:
            if ClickAnswerList[n+1] == ImageTextList[n]:
                diffCorrect += 1
            else:
                diffError += 1
            diffClickTime += float(ImageClickTimeList[n + 1]) - float(ImageClickTimeList[n])
            diffNumeberCount += 1
    if (sameCorrect+sameError) == 0:
        sameAccuracy = 0
    else:
        sameAccuracy = sameCorrect/(sameCorrect+sameError)*100
    if (diffCorrect+diffError) == 0:
        diffAccuracy = 0
    else:
        diffAccuracy = diffCorrect/(diffCorrect+diffError)*100
    if sameNumberCount == 0:
        sameClickTimeAverage = 0
    else:
        sameClickTimeAverage = sameClickTime/sameNumberCount
    if diffNumeberCount == 0:
        diffClickTimeAverage = 0
    else:
         diffClickTimeAverage = diffClickTime/diffNumeberCount
    print(int(sameAccuracy), int(diffAccuracy), sameClickTimeAverage, diffClickTimeAverage, D)
    func8 = StroopTestResult(SubjectInformationList[0], [int(sameAccuracy), int(diffAccuracy)], [sameClickTimeAverage, diffClickTimeAverage])
    func8.func()

label1 = tkinter.Label(win,
                      text="Red" ,
                      bg="white",
                      fg="Red",
                      font=("Arial", 50),
                      width=8,
                      height=3,
                      wraplength=800,
                      justify='left',
                      anchor="center"
                      )
label1.place(x=210, y=100)

label2 = tkinter.Label(win,text="SubjectName", bg="white",font=("Arial", 10))
label2.place(x=0, y=0)
e = tkinter.Variable()
entry2 = tkinter.Entry(win, textvariable=e)
entry2.place(x=90, y=0)
label3 = tkinter.Label(win,text="SubjectAge", bg="white",font=("Arial", 10))
label3.place(x=0, y=25)
e = tkinter.Variable()
entry3 = tkinter.Entry(win, textvariable=e)
entry3.place(x=90, y=25)
StartButton = Button(win, text='Start', bg="white", font=("Arial", 10) ,command=SubjectInformation)
StartButton.place(x=0, y=50)
FinishButton = Button(win, text='Finish and Plot the results', bg="white", font=("Arial", 10) ,command=PlotResults)
FinishButton.place(x=0, y=80)

b1 = Button(win, text='1', bg="Red", font=('Helvetica 10 bold'), width=6, height=2, command=func1)
b1.place(x=100, y=350)
b2 = Button(win, text='2', bg="Orange", font=('Helvetica 10 bold'), width=6, height=2, command=func2)
b2.place(x=180, y=350)
b3 = Button(win, text='3', bg="Yellow", font=('Helvetica 10 bold'), width=6, height=2, command=func3)
b3.place(x=260, y=350)
b4 = Button(win, text='4', bg="Green", font=('Helvetica 10 bold'), width=6, height=2, command=func4)
b4.place(x=340, y=350)
b5 = Button(win, text='5', bg="Cyan", font=('Helvetica 10 bold'), width=6, height=2, command=func5)
b5.place(x=420, y=350)
b6 = Button(win, text='6', bg="Blue", font=('Helvetica 10 bold'), width=6, height=2, command=func6)
b6.place(x=500, y=350)
b7 = Button(win, text='7', bg="Purple", font=('Helvetica 10 bold'), width=6, height=2, command=func7)
b7.place(x=580, y=350)

label = tkinter.Label(win,
                      text="You must respond what the colour of the word is by pressing the buttons, you must report the meaning of the word, not the colour.",
                      bg="white",
                      fg="red",
                      font=("Calibri", 20),
                      width=10,
                      height=2,
                      wraplength=800,
                      justify='left',
                      anchor="w",
                      )

label.pack(fill=tkinter.X, side=tkinter.BOTTOM)
win.mainloop()