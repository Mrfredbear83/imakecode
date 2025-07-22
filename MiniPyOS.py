import tkinter as tk
from tkinter import messagebox, filedialog

# Create desktop window
root = tk.Tk()
root.title("MiniPy OS")
root.geometry("600x400")
root.config(bg="skyblue")

# Fake window dragging
def start_move(event):
    root.x = event.x
    root.y = event.y

def stop_move(event):
    root.x = None
    root.y = None

def do_move(event):
    deltax = event.x - root.x
    deltay = event.y - root.y
    x = root.winfo_x() + deltax
    y = root.winfo_y() + deltay
    root.geometry(f"+{x}+{y}")

# Notepad app
def open_notepad():
    note = tk.Toplevel(root)
    note.title("Notepad")
    text = tk.Text(note, width=50, height=20)
    text.pack()

    def save_text():
        content = text.get("1.0", tk.END)
        file = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text Files", "*.txt")])
        if file:
            with open(file, "w") as f:
                f.write(content)
            messagebox.showinfo("Saved", f"File saved:\n{file}")

    save_button = tk.Button(note, text="Save", command=save_text)
    save_button.pack()

# Info app
def show_info():
    messagebox.showinfo("About", "MiniPy OS\nMade with Python + Tkinter")

# File Explorer app
def open_file_explorer():
    file = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
    if file:
        messagebox.showinfo("File Chosen", f"You opened:\n{file}")

# Desktop icons
tk.Button(root, text=" Notepad", command=open_notepad).place(x=50, y=50)
tk.Button(root, text=" Info", command=show_info).place(x=50, y=120)
tk.Button(root, text=" Files", command=open_file_explorer).place(x=50, y=190)

# Allow window drag
root.bind("<Button-1>", start_move)
root.bind("<ButtonRelease-1>", stop_move)
root.bind("<B1-Motion>", do_move)

# Start desktop
root.mainloop()
