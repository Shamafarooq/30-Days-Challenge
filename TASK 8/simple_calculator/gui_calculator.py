import tkinter as tk
from tkinter import messagebox
from calculator import add, subtract, multiply, divide

# --- 1. Calculation Logic Function ---
# This function is called when the "Calculate" button is pressed.
def calculate():
    """Reads input, performs the chosen calculation, and displays the result."""
    try:
        # Get numbers from the entry fields and convert to float
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        op = operation_var.get()
        result = None

        # Determine which function to call based on the dropdown selection
        if op == "Add":
            result = add(num1, num2)
        elif op == "Subtract":
            result = subtract(num1, num2)
        elif op == "Multiply":
            result = multiply(num1, num2)
        elif op == "Divide":
            # Your divide function already handles the ZeroDivisionError by raising a ValueError
            result = divide(num1, num2)

        # Update the result label with the final value (rounded for cleanliness)
        result_var.set(f"The result is: {round(result, 4)}")
        result_label.config(fg="green") # Set text color to green for success

    except ValueError as e:
        # This catches:
        # 1. Non-numeric input in the entry fields (e.g., typing "abc")
        # 2. The "Cannot divide by zero!" error from your calculator.py's divide function
        result_var.set(f"Error: {e}")
        result_label.config(fg="red") # Set text color to red for errors
    except Exception as e:
        # Catch any unexpected errors
        result_var.set(f"An unexpected error occurred: {e}")
        result_label.config(fg="red")

# --- 2. Setup the Main Window ---
root = tk.Tk()
root.title("Simple Calculator")

# Optional: Set a fixed size for the window
# root.geometry("400x300")

# --- 3. Setup Variables ---
operation_var = tk.StringVar(root)
operation_var.set("Add") # Set default operation
result_var = tk.StringVar(root)
result_var.set("Ready to calculate.")

# --- 4. Create and Place Widgets using grid() ---

# --- Title Label ---
tk.Label(root, text="Simple Calculator", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

# --- First Number Input ---
tk.Label(root, text="Enter the first number:").grid(row=1, column=0, padx=10, pady=5, sticky='w')
num1_entry = tk.Entry(root, width=25)
num1_entry.grid(row=1, column=1, padx=10, pady=5)

# --- Second Number Input ---
tk.Label(root, text="Enter the second number:").grid(row=2, column=0, padx=10, pady=5, sticky='w')
num2_entry = tk.Entry(root, width=25)
num2_entry.grid(row=2, column=1, padx=10, pady=5)

# --- Operation Dropdown Menu ---
operations = ["Add", "Subtract", "Multiply", "Divide"]
tk.Label(root, text="Select an operation:").grid(row=3, column=0, padx=10, pady=5, sticky='w')
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.grid(row=3, column=1, padx=10, pady=5, sticky='ew') # 'ew' stretches it horizontally

# --- Calculate Button ---
calculate_button = tk.Button(root, text="Calculate", command=calculate, bg="red", fg="white", font=("Arial", 10, "bold"))
calculate_button.grid(row=4, column=0, columnspan=2, pady=15, sticky='ew', padx=10)

# --- Result Display Label ---
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 12), pady=10, relief=tk.SUNKEN, width=40)
result_label.grid(row=5, column=0, columnspan=2, pady=10, padx=10, sticky='ew')

# --- 5. Start the GUI Event Loop ---
root.mainloop()