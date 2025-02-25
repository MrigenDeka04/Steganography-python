# **Image Steganography with GUI in Python**

## **Overview**
This project demonstrates an image steganography tool implemented in Python. It allows users to securely hide and retrieve messages within images using a passcode for encryption and decryption. The application provides a user-friendly Graphical User Interface (GUI) built with `tkinter` and uses `OpenCV` for image manipulation. This tool supports standard image formats like `.jpg` and `.png`.

## **Features**
- **Encrypt and Decrypt Messages**: Hide and retrieve secret messages inside images.
- **Passcode Protection**: Secure encryption and decryption using a passcode.
- **GUI Interface**: Simple and intuitive interface built with Python's `tkinter`.
- **Cross-Platform**: Works on Windows, macOS, and Linux.
- **Image File Support**: Supports `.jpg`, `.png`, `.jpeg` formats for encryption.
- **Real-Time Status**: Displays status messages for encryption and decryption.

## **Technologies Used**
- **Programming Language**: Python 3.x
- **Libraries**:
  - `tkinter` for the GUI
  - `opencv-python` (`cv2`) for image manipulation
  - `Pillow` for handling image display in the GUI
- **Platform Compatibility**: Windows, macOS, Linux
- **Development Environment**: Any Python IDE or text editor (VS Code, PyCharm, etc.)

## **Installation**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MrigenDeka04/Steganography-python.git



## **Screenshots**

![Screenshot 2025-02-25 160322](https://github.com/user-attachments/assets/c8eec382-cbb5-44dc-8052-90069d650574)

![Screenshot 2025-02-25 160358](https://github.com/user-attachments/assets/461e64c9-e122-4d72-abeb-26467015faf3)

![Screenshot 2025-02-25 160408](https://github.com/user-attachments/assets/b5ef7c82-7762-4cdb-87c7-f8dd202ba5d9)

![Screenshot 2025-02-25 160443](https://github.com/user-attachments/assets/bf563207-7d9c-432e-be25-49845e296cb7)



## **Usage**

### **Encrypting a Message**
1. **Click "Open Image"** to load an image from your computer. This will open a file dialog allowing you to select an image (JPG, PNG, JPEG formats are supported).
2. **Enter your secret message** in the **"Enter Secret Message"** text field.
3. **Enter a passcode** for encryption in the **"Enter Passcode"** text field. This passcode will be required later for decryption.
4. **Click "Encrypt Message"** to hide the message inside the image. The encrypted image will be saved as `encryptedImage.jpg` and displayed in the GUI.

### **Decrypting a Message**
1. **Click "Open Image"** to load the encrypted image (the one generated after encryption).
2. **Enter the same passcode** used during encryption in the **"Enter Passcode"** text field.
3. **Click "Decrypt Message"** to reveal the hidden message. If the passcode matches, the decrypted message will be shown in a popup. If the passcode does not match, an error message will be shown.

### **Important Notes:**
- The image file must be in a supported format (.jpg, .png, .jpeg).
- The **passcode** you enter during encryption **must** be the same passcode used for decryption, ensuring security.
- You can open and decrypt multiple images, but the passcode must match for each one to retrieve the correct hidden message.


## **Contributing**
- If you want to contribute to this project, feel free to fork it and submit a pull request. Make sure to follow best practices and ensure your code is well-documented.

## **License**
- This project is open-source and available under the MIT License.
