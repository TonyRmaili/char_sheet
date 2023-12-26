import tkinter as tk

def create_checkbutton(frame, row, var, limit_var):
    checkbutton = tk.Checkbutton(frame, variable=var, command=lambda: check_limit(limit_var))
    checkbutton.grid(row=row, column=1)
    return checkbutton

def check_limit(limit_var):
    # Callback function to enforce the limit
    checked_buttons = [var.get() for var in limit_var]
    if sum(checked_buttons) > 2:
        # If more than 3 buttons are checked, uncheck the last one
        last_checked_index = checked_buttons[::-1].index(1)
        limit_var[-(last_checked_index + 1)].set(0)

root = tk.Tk()
root.title("Limited Checkbuttons")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_frames = []
checkbuttons = []
limit_vars = []

# Create three LabelFrames
for i in range(3):
    label_frame = tk.LabelFrame(frame, text=f'LabelFrame {i+1}')
    label_frame.grid(row=0, column=i, padx=10, pady=10)
    label_frames.append(label_frame)

    # Add three labels and independent Checkbutton to each LabelFrame
    limit_var = [tk.IntVar() for _ in range(3)]
    limit_vars.extend(limit_var)

    for j in range(3):
        label = tk.Label(label_frame, text=f'Label {j+1}')
        label.grid(row=j, column=0)

        checkbutton = create_checkbutton(label_frame, row=j, var=limit_var[j], limit_var=limit_var)
        checkbuttons.append(checkbutton)

root.mainloop()
