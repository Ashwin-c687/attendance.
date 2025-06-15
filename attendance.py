import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import pyttsx3
import takeImage
import trainImage
import automaticAttedance
import show_attendance

haar_cascade_path = "haarcascade_frontalface_alt.xml"
trainer_label_path = "TrainingImageLabel/Trainner.yml"
train_image_path = "TrainingImage"
student_detail_path = "StudentDetails/studentdetails.csv"
attendance_path = "Attendance"

def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()

def error_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry("400x110")
    sc1.title("Warning!!")
    sc1.configure(background="#333333")
    sc1.resizable(0, 0)
    tk.Label(
        sc1,
        text="Enrollment & Name required!!!",
        fg="#CCCCCC",
        bg="#333333",
        font=("Arial", 20, "bold"),
    ).pack()
    tk.Button(
        sc1,
        text="OK",
        command=sc1.destroy,
        fg="#CCCCCC",
        bg="#333333",
        width=25,
        height=2,
        activebackground="#FF1744",
        font=("Arial", 15, "bold"),
    ).place(x=110, y=50)

def test_val(inStr, acttyp):
    if acttyp == "1":  # insert
        if not inStr.isdigit():
            return False
    return True

window = Tk()
window.title("Attendence System Using AI")
window.geometry("1920x1080") #adjust the main window size here
window.configure(background="#212121")

logo = Image.open("UI_Image/0001.png")
logo = logo.resize((50, 47), Image.BICUBIC)
logo1 = ImageTk.PhotoImage(logo)
title_label = tk.Label(window, bg="#212121", relief=RIDGE, bd=10, font=("Arial", 35))
title_label.pack(fill=X)
l1 = tk.Label(window, image=logo1, bg="#212121")
l1.place(x=500, y=10)

title_label = tk.Label(
    window, text="Automated Attendance System", bg="#212121", fg="#4CAF50", font=("Arial", 27),
)
title_label.place(x=560, y=12)

a = tk.Label(
    window,
    text="Automated Attendance System\nBased on Face Recognition",
    bg="#212121",
    fg="#CCCCCC",
    bd=10,
    font=("Arial", 35),
)
a.pack()

ri = Image.open("UI_Image/register.png")
r = ImageTk.PhotoImage(ri)
label1 = Label(window, image=r)
label1.image = r
label1.place(x=100, y=270)

ai = Image.open("UI_Image/attendance.png")
a = ImageTk.PhotoImage(ai)
label2 = Label(window, image=a)
label2.image = a
label2.place(x=1110, y=270)

vi = Image.open("UI_Image/verifyy.png")
v = ImageTk.PhotoImage(vi)
label3 = Label(window, image=v)
label3.image = v
label3.place(x=600, y=270)

def take_image_ui():
    ImageUI = Tk()
    ImageUI.title("Take Student Image..")
    ImageUI.geometry("780x480")
    ImageUI.configure(background="#212121")
    ImageUI.resizable(0, 0)
    titl = tk.Label(ImageUI, bg="#212121", relief=RIDGE, bd=10, font=("Arial", 35))
    titl.pack(fill=X)
    titl = tk.Label(
        ImageUI, text="Register Your Face", bg="#212121", fg="#4CAF50", font=("Arial", 30),
    )
    titl.place(x=270, y=12)
    a = tk.Label(
        ImageUI,
        text="Enter the details",
        bg="#212121",
        fg="#CCCCCC",
        bd=10,
        font=("Arial", 24),
    )
    a.place(x=280, y=75)
    lbl1 = tk.Label(
        ImageUI,
        text="Enrollment No",
        width=10,
        height=2,
        bg="#212121",
        fg="#CCCCCC",
        bd=5,
        relief=RIDGE,
        font=("Arial", 12),
    )
    lbl1.place(x=120, y=130)
    txt1 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        validate="key",
        bg="#212121",
        fg="#CCCCCC",
        relief=RIDGE,
        font=("Arial", 25, "bold"),
    )
    txt1.place(x=250, y=130)
    txt1["validatecommand"] = (txt1.register(test_val), "%P", "%d")
    lbl2 = tk.Label(
        ImageUI,
        text="Name",
        width=10,
        height=2,
        bg="#212121",
        fg="#CCCCCC",
        bd=5,
        relief=RIDGE,
        font=("Arial", 12),
    )
    lbl2.place(x=120, y=200)
    txt2 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        bg="#212121",
        fg="#CCCCCC",
        relief=RIDGE,
        font=("Arial", 25, "bold"),
    )
    txt2.place(x=250, y=200)
    lbl3 = tk.Label(
        ImageUI,
        text="Notification",
        width=10,
        height=2,
        bg="#212121",
        fg="#CCCCCC",
        bd=5,
        relief=RIDGE,
        font=("Arial", 12),
    )
    lbl3.place(x=120, y=270)
    message = tk.Label(
        ImageUI,
        text="",
        width=32,
        height=2,
        bd=5,
        bg="#212121",
        fg="#CCCCCC",
        relief=RIDGE,
        font=("Arial", 12, "bold"),
    )
    message.place(x=250, y=270)

    def take_image():
        l1 = txt1.get()
        l2 = txt2.get()
        takeImage.TakeImage(
            l1,
            l2,
            haar_cascade_path,
            train_image_path,
            message,
            error_screen,
            text_to_speech,
        )
        txt1.delete(0, "end")
        txt2.delete(0, "end")

    takeImg = tk.Button(
        ImageUI,
        text="Take Image",
        command=take_image,
        bd=10,
        font=("Arial", 18),
        bg="#212121",
        fg="#CCCCCC",
        height=2,
        width=12,
        relief=RIDGE,
    )
    takeImg.place(x=130, y=350)

    def train_image():
        trainImage.TrainImage(
            haar_cascade_path,
            train_image_path,
            trainer_label_path,
            message,
            text_to_speech,
        )

    trainImg = tk.Button(
        ImageUI,
        text="Train Image",
        command=train_image,
        bd=10,
        font=("Arial", 18),
        bg="#212121",
        fg="#CCCCCC",
        height=2,
        width=12,
        relief=RIDGE,
    )
    trainImg.place(x=360, y=350)

r1 = tk.Button(
    window,
    text="Register a new student",
    command=take_image_ui,
    bd=10,
    font=("Arial", 16),
    bg="#212121",
    fg="#CCCCCC",
    height=2,
    width=17,
)
r1.place(x=100, y=520)

def automatic_attendance():
    automaticAttedance.subjectChoose(text_to_speech)

r2 = tk.Button(
    window,
    text="Take Attendance",
    command=automatic_attendance,
    bd=10,
    font=("Arial", 16),
    bg="#212121",
    fg="#CCCCCC",
    height=2,
    width=17,
)
r2.place(x=600, y=520)

def view_attendance():
    show_attendance.subjectchoose(text_to_speech)

r3 = tk.Button(
    window,
    text="View Attendance",
    command=view_attendance,
    bd=10,
    font=("Arial", 16),
    bg="#212121",
    fg="#CCCCCC",
    height=2,
    width=17,
)
r3.place(x=1100, y=520)

r4 = tk.Button(
    window,
    text="EXIT",
    bd=10,
    command=quit,
    font=("Arial", 16),
    bg="#212121",
    fg="#CCCCCC",
    height=2,
    width=17,
)
r4.place(x=600, y=660)

window.mainloop()
