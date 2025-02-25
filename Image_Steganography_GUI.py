import cv2
import os
import string
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Global variables
img = None
encrypted_image = None
d = {}
c = {}
password = ""  # Initialize the password variable to store the passcode

# Initialize dictionary for character encoding and decoding
for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

# Function to open image
def open_image():
    global img
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
    if file_path:
        img = cv2.imread(file_path)
        show_image(file_path)

# Function to display image on the GUI
def show_image(file_path):
    image = Image.open(file_path)
    image = image.resize((400, 400), Image.Resampling.LANCZOS)  # Updated resampling method
    image = ImageTk.PhotoImage(image)
    image_label.config(image=image)
    image_label.image = image  # Keep a reference to avoid garbage collection

# Encrypt message into image
def encrypt_message():
    global img, encrypted_image, password
    if img is None:
        messagebox.showerror("Error", "Please open an image first!")
        return
    msg = message_entry.get()
    password = passcode_entry.get()  # Store the entered passcode
    if not msg or not password:
        messagebox.showerror("Error", "Please enter a message and passcode!")
        return

    # Hide the message into the image
    m, n, z = 0, 0, 0
    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    
    encrypted_image = img.copy()
    cv2.imwrite("encryptedImage.jpg", encrypted_image)
    show_image("encryptedImage.jpg")
    messagebox.showinfo("Success", "Message encrypted into image.")

# Decrypt message from image
def decrypt_message():
    global encrypted_image, password
    if encrypted_image is None:
        messagebox.showerror("Error", "Please encrypt an image first!")
        return

    pas = passcode_entry.get()  # Get passcode entered by user
    if password != pas:  # Compare with the stored password
        messagebox.showerror("Error", "Incorrect passcode!")
        return

    message = ""
    m, n, z = 0, 0, 0
    for i in range(len(message_entry.get())):
        message += c[encrypted_image[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    messagebox.showinfo("Decrypted Message", f"Decrypted message: {message}")

# Initialize main window
root = tk.Tk()
root.title("Image Steganography")

# Frame for Image
frame = tk.Frame(root)
frame.pack(pady=20)

image_label = tk.Label(frame)
image_label.grid(row=0, column=0, columnspan=2)

# Message Entry
message_label = tk.Label(root, text="Enter Secret Message:")
message_label.pack(pady=5)
message_entry = tk.Entry(root, width=40)
message_entry.pack(pady=5)

# Passcode Entry
passcode_label = tk.Label(root, text="Enter Passcode:")
passcode_label.pack(pady=5)
passcode_entry = tk.Entry(root, width=40)
passcode_entry.pack(pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

open_button = tk.Button(button_frame, text="Open Image", width=20, command=open_image)
open_button.grid(row=0, column=0, padx=10)

encrypt_button = tk.Button(button_frame, text="Encrypt Message", width=20, command=encrypt_message)
encrypt_button.grid(row=0, column=1, padx=10)

decrypt_button = tk.Button(button_frame, text="Decrypt Message", width=20, command=decrypt_message)
decrypt_button.grid(row=1, column=0, columnspan=2, pady=10)

# Run the main GUI loop
root.mainloop()
