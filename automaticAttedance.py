import tkinter as tk
from tkinter import *
import os
import cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.ttk as tkk
import tkinter.font as font
import subprocess

def subjectChoose(text_to_speech):
    def FillAttendance():
        sub = tx.get()
        now = time.time()
        future = now + 30  
        print(now)
        print(future)
        if sub == "":
            t = "Please enter the subject name!!!"
            text_to_speech(t)
            return

        try:
            recognizer = cv2.face.LBPHFaceRecognizer_create()
            try:
                recognizer.read(trainimagelabel_path)
            except:
                e = "Model not found, please train model"
                Notifica.configure(
                    text=e,
                    bg="#212121",
                    fg="white",
                    width=33,
                    font=("Arial", 15, "bold"),
                )
                Notifica.place(x=20, y=250)
                text_to_speech(e)

            facecasCade = cv2.CascadeClassifier(haarcasecade_path)
            df = pd.read_csv(studentdetail_path)
            cam = cv2.VideoCapture(0)
            font = cv2.FONT_HERSHEY_SIMPLEX
            col_names = ["Enrollment", "Name"]
            attendance = pd.DataFrame(columns=col_names)

            while True:
                ___, im = cam.read()
                gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                faces = facecasCade.detectMultiScale(gray, 1.2, 5)
                for (x, y, w, h) in faces:
                    global Id

                    Id, conf = recognizer.predict(gray[y: y + h, x: x + w])
                    if conf < 99: 
                        print(conf)
                        global Subject
                        global aa
                        global date
                        global timeStamp
                        Subject = tx.get()
                        ts = time.time()
                        date = datetime.datetime.fromtimestamp(ts).strftime(
                            "%Y-%m-%d"
                        )
                        timeStamp = datetime.datetime.fromtimestamp(ts).strftime(
                            "%H:%M:%S"
                        )
                        aa = df.loc[df["Enrollment"] == Id]["Name"].values
                        global tt
                        tt = str(Id) + "-" + aa

                        attendance.loc[len(attendance)] = [
                            Id,
                            aa,
                        ]
                        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 4)
                        cv2.putText(
                            im,
                            str(tt),
                            (x + h, y),
                            font,
                            1,
                            (255, 255, 0,),
                            4
                        )
                    else:
                        Id = "Student Face Not Recognized"
                        tt = str(Id)
                        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
                        cv2.putText(
                            im,
                            str(tt),
                            (x + h, y),
                            font,
                            1,
                            (0, 25, 255),
                            4
                        )

                if time.time() > future:
                    break

                attendance = attendance.drop_duplicates(
                    ["Enrollment"], keep="first"
                )

                window_width = 800
                window_height = 600
                cv2.namedWindow("Filling Attendance...", cv2.WINDOW_NORMAL)
                cv2.resizeWindow("Filling Attendance...", window_width, window_height)
                cv2.imshow("Filling Attendance...", im)
                key = cv2.waitKey(30) & 0xFF
                if key == 27:
                    break

            ts = time.time()
            attendance[date] = 1
            date = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
            timeStamp = datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S")
            Hour, Minute, Second = timeStamp.split(":")
            path = os.path.join(attendance_path, Subject)
            fileName = (
                f"{path}/"
                + Subject
                + "_"
                + date
                + "_"
                + Hour
                + "-"
                + Minute
                + "-"
                + Second
                + ".csv"
            )
            attendance = attendance.drop_duplicates(["Enrollment"], keep="first")
            print(attendance)
            attendance.to_csv(fileName, index=False)

            m = "Attendance Filled Successfully of " + Subject
            Notifica.configure(
                text=m,
                bg="#212121",
                fg="white",
                width=33,
                relief=RIDGE,
                bd=5,
                font=("Arial", 15, "bold"),
            )
            text_to_speech(m)

            Notifica.place(x=20, y=250)

            cam.release()
            cv2.destroyAllWindows()

            import csv
            import tkinter

            root = tkinter.Tk()
            root.title("Attendance of " + Subject)
            root.configure(background="#212121")
            window_width = 600
            window_height = 500
            root.geometry(f"{window_width}x{window_height}")
            cs = os.path.join(path, fileName)
            print(cs)
            with open(cs, newline="") as file:
                reader = csv.reader(file)
                r = 0
                for col in reader:
                    c = 0
                    for row in col:
                        label = tkinter.Label(
                            root,
                            width=10,
                            height=1,
                            fg="white",
                            font=("Arial", 15, " bold "),
                            bg="#212121",
                            text=row,
                            relief=tkinter.RIDGE,
                        )
                        label.grid(row=r, column=c)
                        c += 1
                    r += 1
            root.mainloop()
            print(attendance)

        except:
            f = "No Face found for attendance"
            text_to_speech(f)
            cv2.destroyAllWindows()

    subject = Tk()
    subject.title("Subject...")
    subject.geometry("600x300")
    subject.resizable(1, 1)  
    subject.configure(background="#212121")

    titl = tk.Label(subject, bg="#212121", relief=RIDGE, bd=10, font=("Arial", 30))
    titl.pack(fill=X)

    titl = tk.Label(
        subject,
        text="Enter the Subject Name",
        bg="#212121",
        fg="#4CAF50",
        font=("Arial", 25),
    )
    titl.place(x=100, y=20)

    Notifica = tk.Label(
        subject,
        text="Attendance filled Successfully",
        bg="yellow",
        fg="#212121",
        width=33,
        height=2,
        font=("Arial", 15, "bold"),
    )

    def Attf():
        sub = tx.get()
        if sub == "":
            t = "Please enter the subject name!!!"
            text_to_speech(t)
        else:
            file_path = os.path.join("\\Attendence", sub)
            if os.path.exists(file_path):
                os.startfile(file_path)
            else:
                t = "No attendance sheet found for the entered subject."
                text_to_speech(t)

    attf = tk.Button(
        subject,
        text="Check Sheets",
        command=Attf,
        bd=7,
        font=("Arial", 15),
        bg="#212121",
        fg="white",
        height=2,
        width=12,  # Adjust button width here
        relief=RIDGE,
    )
    attf.place(x=360, y=170)  # Adjust button position here

    sub = tk.Label(
        subject,
        text="Enter Subject",
        width=10,
        height=2,
        bg="#212121",
        fg="white",
        bd=5,
        relief=RIDGE,
        font=("Arial", 15),
    )
    sub.place(x=50, y=100)

    tx = tk.Entry(
        subject,
        width=15,
        bd=5,
        bg="#212121",
        fg="white",
        relief=RIDGE,
        font=("Arial", 25, "bold"),
    )
    tx.place(x=210, y=100)

    fill_a = tk.Button(
        subject,
        text="Fill Attendance",
        command=FillAttendance,
        bd=7,
        font=("Arial", 15),
        bg="#212121",
        fg="white",
        height=2,
        width=12,  # Adjust button width here
        relief=RIDGE,
    )
    fill_a.place(x=180, y=170)  # Adjust button position here

    subject.mainloop()

# Paths
haarcasecade_path = "haarcascade_frontalface_alt.xml"
trainimagelabel_path = "TrainingImageLabel/Trainner.yml"
trainimage_path = "TrainingImage"
studentdetail_path = "StudentDetails/studentdetails.csv"
attendance_path = "Attendance"

# Sample call for subjectChoose function
# subjectChoose(text_to_speech)  # Pass your text_to_speech function here
