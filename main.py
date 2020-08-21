import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()
ROOT.minsize(600,200)

input_n = simpledialog.askfloat(title = "Area",
prompt = "Enter a number")

input_x = simpledialog.askfloat(title = "Area",
prompt = "Enter a number")

def area_circle(d):
  area = (3.14 * d * d) / 4
  return area

def area_square(a):
  area = a * a
  return area


print("Area of Circle is :", area_circle(input_n))
print("Area of Square is :" , area_square(input_x))
