# import tkinter as tk

# def create_checkbutton(frame, row, var, limit_var):
#     checkbutton = tk.Checkbutton(frame, variable=var, command=lambda: check_limit(limit_var))
#     checkbutton.grid(row=row, column=1)
#     return checkbutton

# def check_limit(limit_var):
#     # Callback function to enforce the limit
#     checked_buttons = [var.get() for var in limit_var]
#     if sum(checked_buttons) > 2:
#         # If more than 3 buttons are checked, uncheck the last one
#         last_checked_index = checked_buttons[::-1].index(1)
#         limit_var[-(last_checked_index + 1)].set(0)

# root = tk.Tk()
# root.title("Limited Checkbuttons")

# frame = tk.Frame(root)
# frame.pack(padx=10, pady=10)

# label_frames = []
# checkbuttons = []
# limit_vars = []

# # Create three LabelFrames
# for i in range(3):
#     label_frame = tk.LabelFrame(frame, text=f'LabelFrame {i+1}')
#     label_frame.grid(row=0, column=i, padx=10, pady=10)
#     label_frames.append(label_frame)

#     # Add three labels and independent Checkbutton to each LabelFrame
#     limit_var = [tk.IntVar() for _ in range(3)]
#     limit_vars.extend(limit_var)

#     for j in range(3):
#         label = tk.Label(label_frame, text=f'Label {j+1}')
#         label.grid(row=j, column=0)

#         checkbutton = create_checkbutton(label_frame, row=j, var=limit_var[j], limit_var=limit_var)
#         checkbuttons.append(checkbutton)

# root.mainloop()
import tkinter as tk

def update_body():
    # Get the current content of the Text widget
    content = text_widget.get("1.0", "end-1c")
    
    # Split the content into lines
    lines = content.split('\n')

    # Update the body lines with alternating fonts and colors
    for i in range(1, min(6, len(lines))):
        line = lines[i]
        if i % 2 == 0:
            # Even lines (2, 4, etc.) - set font to smaller and color to red
            text_widget.tag_add("small_red", f"{i + 1}.0", f"{i + 1}.end")
        else:
            # Odd lines (1, 3, etc.) - set font to smaller and color to black
            text_widget.tag_add("small_black", f"{i + 1}.0", f"{i + 1}.end")

    # Apply the tags to the Text widget
    text_widget.tag_config("small_red", font=("Helvetica", 10), foreground="red")
    text_widget.tag_config("small_black", font=("Helvetica", 10), foreground="black")

# Create the main window
root = tk.Tk()
root.title("Text Widget Example")

# Create a Text widget
text_widget = tk.Text(root, wrap="word", height=10, width=40)

# Insert the Header and Body lines into the Text widget
text_widget.insert("1.0", "Header\n")
text_widget.insert("2.0", "Body line 1\n")
text_widget.insert("3.0", "Body line 2\n")
text_widget.insert("4.0", "Body line 3\n")
text_widget.insert("5.0", "Body line 4\n")
text_widget.insert("6.0", "Body line 5\n")

# Call the update_body function to apply font and color styles
update_body()

# Pack the Text widget and start the main loop
text_widget.pack()
root.mainloop()
