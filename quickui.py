import tkinter as tk

def update_label_text():
    new_text = entry.get()
    label.config(text=new_text)

root = tk.Tk()
root.title("Dynamic Label Text")

label_frame = tk.LabelFrame(root, text="Label Frame")
label_frame.pack(padx=10, pady=10)

label = tk.Label(label_frame, text="Dynamic Text", wraplength=150,width=2)
label.pack(padx=10, pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

update_button = tk.Button(root, text="Update Label Text", command=update_label_text)
update_button.pack(pady=10)

root.mainloop()
