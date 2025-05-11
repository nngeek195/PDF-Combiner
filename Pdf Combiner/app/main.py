import tkinter as tk
from tkinter import filedialog, messagebox
from core import combine_pdfs
import os

def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder)


def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".pdf",
                                        filetypes=[("PDF Files", "*.pdf")])
    if file:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, file)


def run_merge():
    input_folder = folder_entry.get()
    output_file = output_entry.get()

    if not os.path.isdir(input_folder):
        messagebox.showerror("Invalid Folder", "Please select a valid folder containing PDFs.")
        return

    if not output_file.endswith(".pdf"):
        messagebox.showerror("Invalid Output", "Please provide a valid output .pdf file.")
        return

    result = combine_pdfs(input_folder, output_file)
    messagebox.showinfo("Result", result)


# GUI Setup
root = tk.Tk()
root.title("PDF Merger")
root.geometry("500x250")
root.resizable(False, False)

# Folder selection
tk.Label(root, text="Select PDF Folder:").pack(pady=5)
folder_frame = tk.Frame(root)
folder_frame.pack(pady=5)

folder_entry = tk.Entry(folder_frame, width=40)
folder_entry.pack(side=tk.LEFT, padx=5)

tk.Button(folder_frame, text="Browse", command=select_folder).pack(side=tk.LEFT)

# Output file selection
tk.Label(root, text="Save Combined PDF As:").pack(pady=5)
output_frame = tk.Frame(root)
output_frame.pack(pady=5)

output_entry = tk.Entry(output_frame, width=40)
output_entry.pack(side=tk.LEFT, padx=5)

tk.Button(output_frame, text="Save As", command=save_file).pack(side=tk.LEFT)

# Merge button
tk.Button(root, text="Merge PDFs", command=run_merge, width=20, bg="green", fg="white").pack(pady=20)

# Start GUI loop
root.mainloop()