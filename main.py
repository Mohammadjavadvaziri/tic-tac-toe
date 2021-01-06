# MohammadJavad Vaziri

from tkinter import *
import tkinter.messagebox
import random

blue = {
    "btnBgDefault": "#4fc3f7",
    "btnBgO": "#0093c4",
    "btnBgX": "#8bf6ff",
    "rootBg": "#29b6f6",
    "rootBgWin": "#64b5f6"}
red = {
    "btnBgDefault": "#ff6e40",
    "btnBgO": "#c53d13",
    "btnBgX": "#ffa06d",
    "rootBg": "#ff3d00",
    "rootBgWin": "#ffab40"}
yellow = {
    "btnBgDefault": "#ffff00",
    "btnBgO": "#c7cc00",
    "btnBgX": "#ffff5a",
    "rootBg": "#ffea00",
    "rootBgWin": "#ffd600"}
green = {
    "btnBgDefault": "#69f0ae",
    "btnBgO": "#2bbd7e",
    "btnBgX": "#9fffe0",
    "rootBg": "#00e676",
    "rootBgWin": "#64ffda"}
purple = {
    "btnBgDefault": "#7c4dff",
    "btnBgO": "#3f1dcb",
    "btnBgX": "#b47cff",
    "rootBg": "#651fff",
    "rootBgWin": "#e040fb"}
bgColorList = [red, green, blue, purple, yellow]

f = open("setting.txt", "r")
colorSetting = f.read()
if colorSetting[0] == "0":
    bgColorList.remove(red)
if colorSetting[1] == "0":
    bgColorList.remove(green)
if colorSetting[2] == "0":
    bgColorList.remove(blue)
if colorSetting[3] == "0":
    bgColorList.remove(purple)
if colorSetting[4] == "0":
    bgColorList.remove(yellow)

color = random.choice(bgColorList)
root = Tk()
root.geometry("600x700")
root.resizable(False, False)
root.title("MohammadJavad Vaziri")
root.config(bg=color["rootBg"])


def clickSetting():
    settingWindow = Toplevel()
    settingWindow.geometry("450x200")

    def clickSave():
        global bgColorList
        newSetting = str(redVar.get()) + str(greenVar.get()) + str(blueVar.get()) + str(purpleVar.get()) + str(
            yellowVar.get())
        f = open("setting.txt", "w")
        f.write(newSetting)
        if newSetting[0] == "0" and red in bgColorList:
            bgColorList.remove(red)
        if newSetting[1] == "0" and green in bgColorList:
            bgColorList.remove(green)
        if newSetting[2] == "0" and blue in bgColorList:
            bgColorList.remove(blue)
        if newSetting[3] == "0" and purple in bgColorList:
            bgColorList.remove(purple)
        if newSetting[4] == "0" and yellow in bgColorList:
            bgColorList.remove(yellow)

        if newSetting[0] == "1" and red not in bgColorList:
            bgColorList.append(red)
        if newSetting[1] == "1" and green not in bgColorList:
            bgColorList.append(green)
        if newSetting[2] == "1" and blue not in bgColorList:
            bgColorList.append(blue)
        if newSetting[3] == "1" and purple not in bgColorList:
            bgColorList.append(purple)
        if newSetting[4] == "1" and yellow not in bgColorList:
            bgColorList.append(yellow)
        settingWindow.destroy()

    f = open("setting.txt", "r")
    data = f.read()
    settingWindow.config(bg=color["rootBg"])
    redVar = IntVar()
    redVar.set(data[0])
    greenVar = IntVar()
    greenVar.set(data[1])
    blueVar = IntVar()
    blueVar.set(data[2])
    purpleVar = IntVar()
    purpleVar.set(data[3])
    yellowVar = IntVar()
    yellowVar.set(data[4])
    lblColor = Label(settingWindow, text="Themes : ", font="Calibri 12", bg=color["rootBg"])
    lblColor.place(x=20, y=60)

    redCheckBox = Checkbutton(settingWindow, text="Red", bg=color["rootBg"], variable=redVar)
    redCheckBox.place(x=100, y=60)
    greenCheckBox = Checkbutton(settingWindow, text="Green", bg=color["rootBg"], variable=greenVar)
    greenCheckBox.place(x=170, y=60)
    blueCheckBox = Checkbutton(settingWindow, text="Blue", bg=color["rootBg"], variable=blueVar)
    blueCheckBox.place(x=240, y=60)
    purpleCheckBox = Checkbutton(settingWindow, text="Purple", bg=color["rootBg"], variable=purpleVar)
    purpleCheckBox.place(x=310, y=60)
    yellowCheckBox = Checkbutton(settingWindow, text="Yellow", bg=color["rootBg"], variable=yellowVar)
    yellowCheckBox.place(x=380, y=60)
    btnSave = Button(settingWindow, text="Save", command=clickSave, bg=color["btnBgDefault"], borderwidth=0.7)
    btnSave.place(x=350, y=150, height=30, width=65)
    settingWindow.mainloop()


def btnBg(btnIndex1, btnIndex2, btnIndex3):
    btnIndex1.config(bg=color["rootBgWin"])
    btnIndex2.config(bg=color["rootBgWin"])
    btnIndex3.config(bg=color["rootBgWin"])


def endBtn():
    global color
    canvas = Canvas(root, width=600, height=700, bg=color["rootBg"])
    canvas.pack()
    color = random.choice(bgColorList)
    resetBtn = Button(root, font=("Calibri", 70), bg="#ff9999", text="Reset", borderwidth=0,
                      command=lambda: [reset(), resetBtn.destroy(), quitBtn.destroy(), canvas.destroy()])
    resetBtn.place(x=150, y=20, width=300, height=100)
    quitBtn = Button(root, bg="#99e6ff", command=exit, borderwidth=0, text="Quit", font=("Calibri", 70))
    quitBtn.place(x=150, y=580, width=300, height=100)


def reset():
    global a
    for i in btnList:
        i.config(text="", state=NORMAL, bg=color["btnBgDefault"])
    root.config(bg=color["rootBg"])
    btnSetting.config(bg=color["btnBgDefault"])
    lblScoreX.config(bg=color["rootBg"])
    lblScoreO.config(bg=color["rootBg"])
    btnQuit.config(bg=color["btnBgDefault"])
    a = 0


btnList = []
a = 0
ScoreX = 0
ScoreO = 0


def Win(btnIndex1, btnIndex2, btnIndex3, xOro):
    btnBg(btnList[btnIndex1], btnList[btnIndex2], btnList[btnIndex3])
    if xOro == "X":
        tkinter.messagebox.showinfo("X", "X Win")
        newScore("X")
    elif xOro == "O":
        tkinter.messagebox.showinfo("O", "O Win")
        newScore("O")
    endBtn()


def clicked(Btn):
    global a
    if a == 0:
        Btn.config(text="O", bg=color["btnBgO"])
        a = 1
        Btn.configure(state=DISABLED)
        checkForWin()

    elif a == 1:
        Btn.config(text="X", bg=color["btnBgX"])
        a = 0
        Btn.configure(state=DISABLED)
        checkForWin()


def newScore(xORo):
    global ScoreO, ScoreX
    if xORo == "X":
        ScoreX += 1
        lblScoreX.config(text=f"X : {ScoreX}")
    elif xORo == "O":
        ScoreO += 1
        lblScoreO.config(text=f"O : {ScoreO}")


def checkForWin():
    if btnList[0]["text"] == "X" and btnList[1]["text"] == "X" and btnList[2]["text"] == "X":
        Win(0, 1, 2, "X")
    elif btnList[0]["text"] == "X" and btnList[3]["text"] == "X" and btnList[6]["text"] == "X":
        Win(0, 3, 6, "X")
    elif btnList[0]["text"] == "X" and btnList[4]["text"] == "X" and btnList[8]["text"] == "X":
        Win(0, 4, 8, "X")
    elif btnList[1]["text"] == "X" and btnList[4]["text"] == "X" and btnList[7]["text"] == "X":
        Win(1, 4, 7, "X")
    elif btnList[2]["text"] == "X" and btnList[5]["text"] == "X" and btnList[8]["text"] == "X":
        Win(2, 5, 8, "X")
    elif btnList[2]["text"] == "X" and btnList[4]["text"] == "X" and btnList[6]["text"] == "X":
        Win(2, 4, 6, "X")
    elif btnList[6]["text"] == "X" and btnList[7]["text"] == "X" and btnList[8]["text"] == "X":
        Win(6, 7, 8, "X")
    elif btnList[3]["text"] == "X" and btnList[4]["text"] == "X" and btnList[5]["text"] == "X":
        Win(3, 4, 5, "X")
    # -------------------------------------------------------------------------------------------------------
    elif btnList[0]["text"] == "O" and btnList[1]["text"] == "O" and btnList[2]["text"] == "O":
        Win(0, 1, 2, "O")
    elif btnList[0]["text"] == "O" and btnList[3]["text"] == "O" and btnList[6]["text"] == "O":
        Win(0, 3, 6, "O")
    elif btnList[0]["text"] == "O" and btnList[4]["text"] == "O" and btnList[8]["text"] == "O":
        Win(0, 4, 8, "O")
    elif btnList[1]["text"] == "O" and btnList[4]["text"] == "O" and btnList[7]["text"] == "O":
        Win(1, 4, 7, "O")
    elif btnList[2]["text"] == "O" and btnList[5]["text"] == "O" and btnList[8]["text"] == "O":
        Win(2, 5, 8, "O")
    elif btnList[2]["text"] == "O" and btnList[4]["text"] == "O" and btnList[6]["text"] == "O":
        Win(2, 4, 6, "O")
    elif btnList[6]["text"] == "O" and btnList[7]["text"] == "O" and btnList[8]["text"] == "O":
        Win(6, 7, 8, "O")
    elif btnList[3]["text"] == "O" and btnList[4]["text"] == "O" and btnList[5]["text"] == "O":
        Win(3, 4, 5, "O")
    elif btnList[0]["text"] != "" and btnList[1]["text"] != "" and btnList[2]["text"] != "" and btnList[3][
        "text"] != "" and btnList[4]["text"] != "" and btnList[5]["text"] != "" and btnList[6]["text"] != "" and \
            btnList[7]["text"] != "" and btnList[8]["text"] != "":
        tkinter.messagebox.showinfo("equal", "equal")
        endBtn()


for i in range(0, 600, 200):
    for j in range(0, 600, 200):
        btn = Button(root, borderwidth=0.7, text="", font="Calibri 100", bg=color["btnBgDefault"])
        btn.config(command=lambda btn=btn: clicked(btn))
        btn.place(x=i, y=j, width=200, height=200)
        btnList.append(btn)


btnSetting = Button(root, borderwidth=0.5, text="Setting", font="Calibri 30", bg=color["btnBgDefault"],
                    command=clickSetting)
btnSetting.place(x=10, y=620, width=150, height=60)
btnQuit = Button(root, borderwidth=0.5, text="Quit", font="Calibri 30", bg=color["btnBgDefault"], command=exit)
btnQuit.place(x=180, y=620, width=150, height=60)
lblScoreO = Label(root, text="O : 0 ", bg=color["rootBg"], font="Lato 30")
lblScoreO.place(x=370, y=620)
lblScoreX = Label(root, text="X : 0 ", bg=color["rootBg"], font="Lato 30")
lblScoreX.place(x=500, y=620)
root.mainloop()
