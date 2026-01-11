import tkinter as tk
from tkinter import messagebox
import csv
import matplotlib.pyplot as plt

FILE_NAME = "bmi_data.csv"

def calculate_bmi():
    try:
        name = name_entry.get()
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            raise ValueError

        bmi = round(weight / (height ** 2), 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"BMI: {bmi} ({category})")

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, weight, height, bmi])

    except:
        messagebox.showerror("Error", "Please enter valid inputs")

def show_graph():
    bmis = []
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                bmis.append(float(row[3]))

        plt.plot(bmis)
        plt.xlabel("Entry Number")
        plt.ylabel("BMI Value")
        plt.title("BMI Trend")
        plt.show()

    except:
        messagebox.showerror("Error", "No data available")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("BMI Calculator")

# Window size & center
root.geometry("400x350")
root.eval('tk::PlaceWindow . center')

# Main frame (center content)
frame = tk.Frame(root)
frame.pack(expand=True)

# Labels & Entries (wide boxes)
tk.Label(frame, text="Name").grid(row=0, column=0, pady=8, sticky="w")
name_entry = tk.Entry(frame, width=30)
name_entry.grid(row=0, column=1, pady=8)

tk.Label(frame, text="Weight (kg)").grid(row=1, column=0, pady=8, sticky="w")
weight_entry = tk.Entry(frame, width=30)
weight_entry.grid(row=1, column=1, pady=8)

tk.Label(frame, text="Height (m)").grid(row=2, column=0, pady=8, sticky="w")
height_entry = tk.Entry(frame, width=30)
height_entry.grid(row=2, column=1, pady=8)

# Buttons
tk.Button(frame, text="Calculate BMI", width=25, command=calculate_bmi)\
    .grid(row=3, column=0, columnspan=2, pady=12)

tk.Button(frame, text="Show BMI Trend", width=25, command=show_graph)\
    .grid(row=4, column=0, columnspan=2)

# Result
result_label = tk.Label(frame, text="", font=("Arial", 11, "bold"))
result_label.grid(row=5, column=0, columnspan=2, pady=12)

root.mainloop()
