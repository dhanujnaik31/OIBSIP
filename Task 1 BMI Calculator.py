import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x300")
root.resizable(0, 0)
root.configure(bg='blue')

# Add title label
title_label = tk.Label(root, text="BMI CALCULATOR", bg='#f0f0f0', font=('Arial', 16, 'bold'))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Add labels for weight and height
tk.Label(root, text="Weight (kg):", bg='#f0f0f0', font=('Arial', 14)).grid(row=1, column=0, padx=10, pady=(10, 5), sticky='e')
tk.Label(root, text="Height (m):", bg='#f0f0f0', font=('Arial', 14)).grid(row=2, column=0, padx=10, pady=(5, 10), sticky='e')

# Add entry widgets for weight and height
weight_entry = tk.Entry(root, font=('Arial', 14))
height_entry = tk.Entry(root, font=('Arial', 14))
weight_entry.grid(row=1, column=1, padx=10, pady=(10, 5))
height_entry.grid(row=2, column=1, padx=10, pady=(5, 10))

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight / (height ** 2)
        
        if bmi < 18.5:
            category = "Underweight"
            color = '#66b3ff'
            advice = "You need to gain weight!"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
            color = '#99ff99'
            advice = "You are healthy!"
        elif 25 <= bmi < 30:
            category = "Overweight"
            color = '#ffcc66'
            advice = "You need to lose weight!"
        else:
            category = "Obesity"
            color = '#ff6666'
            advice = "You are obese... Need to burn out a lot!"
        
        bmi_result.set(f"BMI: {bmi:.2f}\nCategory: {category}\n{advice}")
        result_label.config(fg=color)
    except ValueError:
        bmi_result.set("Please enter valid numbers")
        result_label.config(fg='red')

# Function to reset the entries and result
def reset():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    bmi_result.set("")
    result_label.config(fg='black')

# Add buttons for calculate and reset
button_frame = tk.Frame(root, bg='#f0f0f0')
button_frame.grid(row=3, column=0, columnspan=2, pady=20)
calculate_button = tk.Button(button_frame, text="Calculate", command=calculate_bmi, width=10, font=('Arial', 14))
calculate_button.grid(row=0, column=0, padx=5)
reset_button = tk.Button(button_frame, text="Reset", command=reset, width=10, font=('Arial', 14))
reset_button.grid(row=0, column=1, padx=5)

# Add a label to display the BMI result
bmi_result = tk.StringVar()
result_label = tk.Label(root, textvariable=bmi_result, bg='white', font=('Arial', 16, 'bold'))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the main loop
root.mainloop()
