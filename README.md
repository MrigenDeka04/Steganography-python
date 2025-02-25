# Steganography-python
Overview
This project demonstrates an image steganography tool implemented in Python. It allows users to securely hide and retrieve messages within images using a passcode for encryption and decryption. The application provides a user-friendly Graphical User Interface (GUI) built with tkinter and uses OpenCV for image manipulation. This tool supports standard image formats like .jpg and .png.

Features
Encrypt and Decrypt Messages: Hide and retrieve secret messages inside images.
Passcode Protection: Secure encryption and decryption using a passcode.
GUI Interface: Simple and intuitive interface built with Python's tkinter.
Cross-Platform: Works on Windows, macOS, and Linux.
Image File Support: Supports .jpg, .png, .jpeg formats for encryption.
Real-Time Status: Displays status messages for encryption and decryption.
Technologies Used
Programming Language: Python 3.x
Libraries:
tkinter for the GUI
opencv-python (cv2) for image manipulation
Pillow for handling image display in the GUI
Platform Compatibility: Windows, macOS, Linux
Development Environment: Any Python IDE or text editor (VS Code, PyCharm, etc.)


Screenshots
![Screenshot 2025-02-25 160322](https://github.com/user-attachments/assets/c8eec382-cbb5-44dc-8052-90069d650574)

![Screenshot 2025-02-25 160358](https://github.com/user-attachments/assets/461e64c9-e122-4d72-abeb-26467015faf3)

![Screenshot 2025-02-25 160408](https://github.com/user-attachments/assets/b5ef7c82-7762-4cdb-87c7-f8dd202ba5d9)

![Screenshot 2025-02-25 160443](https://github.com/user-attachments/assets/bf563207-7d9c-432e-be25-49845e296cb7)



Usage
Encrypting a Message
Click "Open Image" to load an image from your computer.
Enter your secret message in the "Enter Secret Message" field.
Enter a passcode for encryption in the "Enter Passcode" field.
Click "Encrypt Message" to hide the message in the image.
Decrypting a Message
Load the encrypted image by clicking "Open Image".
Enter the passcode used during encryption in the "Enter Passcode" field.
Click "Decrypt Message" to reveal the hidden message.
Note:
The image file must be in a supported format (.jpg, .png, .jpeg).
The passcode entered during encryption is required for decryption to ensure security.
