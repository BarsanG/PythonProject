import tkinter as tk
from tkinter import filedialog
from PIL import Image


def upload_click():
    global selected_image
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    if file_path:
        selected_image = Image.open(file_path)
        label.config(text=f"Selected Image: {file_path}")


def execute_click():
    if 'selected_image' in globals():
        sra3_width, sra3_height = 1260, 1780  # SRA3 page size
        top_margin, bottom_margin = 9, 9  # Top and bottom margins (in mm)
        left_margin, right_margin = 16, 16  # Left and right margins (in mm)
        column_margin = 3  # Margin between columns (in mm)

        printable_width = sra3_width - (left_margin + right_margin)
        printable_height = sra3_height - (top_margin + bottom_margin)

        if selected_image:
            img_width, img_height = selected_image.size

            num_cols = printable_width // (img_width + column_margin)
            num_rows = printable_height // img_height

            sra3_image = Image.new("RGB", (sra3_width, sra3_height), "white")  # Initialize the SRA3 canvas

            for x in range(left_margin, left_margin + num_cols * (img_width + column_margin), img_width + column_margin):
                for y in range(top_margin, top_margin + num_rows * img_height, img_height):
                    sra3_image.paste(selected_image, (x, y))

            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
            if file_path:
                sra3_image.save(file_path)
                label.config(text=f"Image saved to {file_path}")
            else:
                label.config(text="No file selected")
        else:
            label.config(text="No image to save")
    else:
        label.config(text="No image selected")


window = tk.Tk()
window.title("Business Card Replication")

button1 = tk.Button(window, text="Select Image", command=upload_click)
button3 = tk.Button(window, text="Image Replication and Download", command=execute_click)

label = tk.Label(window, text="")

button1.pack()
button3.pack()
label.pack()

window.mainloop()
