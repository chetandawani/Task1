''''''
import tkinter as tk
def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "Clear":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Main application window
root = tk.Tk()
root.title("Simple Calculator By MR.CHETAN DAWANI")
root.geometry("500x600")

# Entry widget to display the calculations and results
entry = tk.Entry(root, font=("Book Antiqua", 24), justify="right")
entry.pack(fill=tk.BOTH, expand=True)

# Buttons for operands {numbers}  and operators
buttons = [
        ("1", "2", "3", "+"),
        ("4", "5", "6", "-"),
        ("7", "8", "9", "*"),
        ("0", ".", "=", "/"),
        ("Clear",)
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    for button_text in row:
        button = tk.Button(frame, text=button_text, font=("Book Antiqua", 24),justify="right", relief=tk.GROOVE)
        button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        button.bind("<Button-1>", on_click)

root.mainloop()