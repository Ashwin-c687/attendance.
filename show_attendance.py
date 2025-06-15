import pandas as pd
from glob import glob
import os
import tkinter as tk
from tkinter import *
import csv
import tkinter

def subjectchoose(text_to_speech):
    def calculate_attendance():
        Subject = tx.get()

        if Subject == "":
            t = 'Please enter the subject name.'
            text_to_speech(t)
            return

        os.chdir(
            f"C:\\Users\\danie\\Project\\p1\\Attendence\\{Subject}"
        )
        filenames = glob(
            f"C:\\Users\\danie\\Project\\p1\\Attendence\\{Subject}\\{Subject}*.csv"
        )
        df = [pd.read_csv(f) for f in filenames]
        newdf = df[0]
        for i in range(1, len(df)):
            newdf = newdf.merge(df[i], how="outer")
        newdf.fillna(0, inplace=True)
        newdf["Attendance"] = 0
        for i in range(len(newdf)):
            newdf.loc[i, "Attendance"] = round(newdf.iloc[i, 2:-1].mean() * 100, 2)
        newdf.to_csv("attendance.csv", index=False)

        root = Tk()
        root.title("Attendance of "+Subject)
        root.configure(background="#212121")
        cs = f"C:\\Users\\danie\\Project\\p1\\Attendence\\{Subject}\\attendance.csv"

        # Get the maximum length of names in the dataset
        max_name_length = max(len(str(name)) for name in newdf['Name'])

        with open(cs) as file:
            reader = csv.reader(file)
            r = 0
            for col in reader:
                c = 0
                for row in col:
                    # Set a fixed width for the name labels
                    if c == 1:  # Assuming Name column is the second column (index 1)
                        label_width = 25  # Adjust width as needed
                    else:
                        label_width = 15  # Set default width for other columns

                    label = tkinter.Label(
                        root,
                        width=label_width,
                        height=1,
                        fg="white",
                        font=("Arial", 15, "bold"),
                        bg="#212121",
                        text=row,
                        relief=tkinter.RIDGE,
                    )
                    label.grid(row=r, column=c)
                    c += 1
                r += 1
        root.mainloop()

    subject = Tk()
    subject.title("Subject...")
    subject.geometry("580x320")
    subject.resizable(True, True)  # Resizable window
    subject.configure(background="#212121")

    titl = tk.Label(subject, bg="#212121", relief=RIDGE, bd=10, font=("Arial", 30))
    titl.pack(fill=X)
    titl = tk.Label(
        subject,
        text="Which Subject of Attendance?",
        bg="#212121",
        fg="#4CAF50",
        font=("Arial", 25),
    )
    titl.place(x=50, y=20)

    def Attf():
        sub = tx.get()
        if sub == "":
            t = "Please enter the subject name!!!"
            text_to_speech(t)
        else:
            folder_path = f"C:\\Users\\danie\\Project\\p1\\Attendence\\{sub}"
            if os.path.exists(folder_path):
                os.startfile(folder_path)
            else:
                t = "No attendance folder found for the entered subject."
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
        width=15,
        relief=RIDGE,
    )
    attf.place(x=60, y=150)

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
    sub.place(x=50, y=90)

    tx = tk.Entry(
        subject,
        width=15,
        bd=5,
        bg="#212121",
        fg="white",
        relief=RIDGE,
        font=("Arial", 25, "bold"),
    )
    tx.place(x=210, y=90)  # Adjusted position with spacing

    fill_a = tk.Button(
        subject,
        text="View Attendance",
        command=calculate_attendance,
        bd=7,
        font=("Arial", 15),
        bg="#212121",
        fg="white",
        height=2,
        width=12,
        relief=RIDGE,
    )
    fill_a.place(x=222, y=150)  # Adjusted button position with spacing
    subject.mainloop()
