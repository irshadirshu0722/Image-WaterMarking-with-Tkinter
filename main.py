import tkinter
from tkinter import Tk, Entry, Button, Label, filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

def open_img():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")])
    try:
        if file_path:
            image = Image.open(file_path)


            global displayed_image
            displayed_image = image
            label_text.config(text="Image loaded successfully!")
    except Exception as e:
        label_text.config(text=f"Error: {e}")

def add_company_name():
    global displayed_image
    if 'displayed_image' in globals():
        try:
            company_name = entry.get()
            if company_name:
                draw = ImageDraw.Draw(displayed_image)
                font = ImageFont.load_default()
                text = f"{company_name}"
                draw.text((10, 10), text, fill="black", font=font)

                label_text.config(text="Company name added successfully!")
        except Exception as e:
            label_text.config(text=f"Error: {e}")

def save_img():
    if 'displayed_image' in globals():
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        try:
            if file_path:
                displayed_image.save(file_path)
                label_text.config(text="Image saved successfully!")
        except Exception as e:
            label_text.config(text=f"Error: {e}")

window = Tk()
window.title("Image water marking")
window.geometry("250x300")
window.configure(bg="white")

label_text = Label(window, text="", fg="green")
label_text.grid(column=1, row=0, pady=10)



entry = Entry(width=40)
entry.grid(column=1, row=2, padx=10, pady=10)

open_button = Button(text="Open image", command=open_img, bg="red", fg="white", width=20, height=2)
open_button.grid(column=1, row=3, padx=10, pady=10)

add_text_button = Button(text="Add Company Name", command=add_company_name, bg="black", fg="white", width=20, height=2)
add_text_button.grid(column=1, row=4, padx=10, pady=10)
save_button = Button(text="Save image", command=save_img, bg="green", fg="white", width=20, height=2)
save_button.grid(column=1, row=5, padx=10, pady=10)

window.mainloop()
