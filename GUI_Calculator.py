import tkinter as tk
from tkinter import messagebox

def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

def divide():
    try:
        if float(entry2.get()) == 0:
            messagebox.showerror("Math Error", "Cannot divide by zero")
        else:
            result = float(entry1.get()) / float(entry2.get())
            result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create input fields
entry1 = tk.Entry(root, width=10)
entry2 = tk.Entry(root, width=10)
entry1.grid(row=0, column=1, padx=10, pady=10)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Create labels
label1 = tk.Label(root, text="Enter first number:")
label2 = tk.Label(root, text="Enter second number:")
label1.grid(row=0, column=0, padx=10, pady=10)
label2.grid(row=1, column=0, padx=10, pady=10)

# Create buttons for operations
add_button = tk.Button(root, text="Add", command=add)
subtract_button = tk.Button(root, text="Subtract", command=subtract)
multiply_button = tk.Button(root, text="Multiply", command=multiply)
divide_button = tk.Button(root, text="Divide", command=divide)

add_button.grid(row=2, column=0, padx=10, pady=10)
subtract_button.grid(row=2, column=1, padx=10, pady=10)
multiply_button.grid(row=3, column=0, padx=10, pady=10)
divide_button.grid(row=3, column=1, padx=10, pady=10)

# Create a label for displaying the result
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
