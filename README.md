# 🕵️‍♂️ Steganography Toolkit

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-red?logo=streamlit)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Made With ❤️](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)

A powerful and beginner-friendly **Steganography and Encryption Toolkit** built with [Streamlit](https://streamlit.io/). This web app allows you to hide encrypted text inside images or embed one image inside another using simple LSB (Least Significant Bit) techniques — all directly in your browser.

🚀 **[Live Demo](https://stegnography-toolkit-lladwds8paxcwnkbfucv4t.streamlit.app/)** — Try it instantly on Streamlit Cloud!

---

## 📚 Table of Contents

- [✨ Features](#-features)
- [🧪 Tech Stack](#-tech-stack)
- [🖥️ How to Use](#-how-to-use)
- [🖼️ Demo Screenshots](#-demo-screenshots)
- [🔐 Security Notes](#-security-notes)
- [⚙️ Setup Instructions](#-setup-instructions)
- [📄 License](#-license)

---

## ✨ Features

- 🔐 **Text Encryption with Random Salt** using `Fernet` + `PBKDF2HMAC`
- 📝 **Text-in-Image Hiding** (encrypt + embed message into an image)
- 🖼️ **Image-in-Image Hiding** (embed one image inside another)
- 🔍 **Message Extraction & Decryption**
- 🎯 **Image Extraction from Stego Images**
- 🛡️ **Privacy First** — All operations are client-side in your browser

---

## 🧪 Tech Stack

- [Streamlit](https://streamlit.io/) – UI framework
- [Python 3.8+](https://www.python.org/) – Core logic
- [Pillow (PIL)](https://pypi.org/project/Pillow/) – Image manipulation
- [NumPy](https://numpy.org/) – Data operations
- [cryptography](https://cryptography.io/) – Secure encryption

---

## 🖥️ How to Use

### 🔐 Tab 1: Text Encryption + Hiding

#### 🔸 Embed Message:
- Upload a **cover image**
- Enter a **password** (used to derive the encryption key)
- Enter your **secret message**
- Click **Embed** and download the stego image

#### 🔸 Extract Message:
- Upload the **stego image**
- Enter the **same password**
- Click **Extract** to reveal your secret message

> 💡 A **random salt** is automatically generated per message for stronger security. It's securely embedded in the image.

---

### 🖼️ Tab 2: Image-in-Image Hiding

#### 🔸 Embed Image:
- Upload a **cover image**
- Upload a **secret image**
- Click **Hide Image** to download the result

#### 🔸 Extract Image:
- Upload the **stego image**
- Click **Reveal Hidden Image** to extract and view it

---

## 🖼️ Demo Screenshots

| Text Hiding Tab | Image-in-Image Tab |
|-----------------|--------------------|
| ![Screenshot 2025-06-16 015904](https://github.com/user-attachments/assets/74e22b1d-b075-4f30-afc3-7cb9f0c80ae1)<br>![Screenshot 2025-06-16 210201](https://github.com/user-attachments/assets/b86964d3-4ff1-4c72-9a6e-90f80c8278dc) | ![Screenshot 2025-06-16 210408](https://github.com/user-attachments/assets/2c7a9caf-4ac3-4fde-aae1-3887e6e59469)<br>![Screenshot 2025-06-16 210509](https://github.com/user-attachments/assets/59b043e0-3398-407a-8ade-f00b1d6aba6b) |


---

## 🔐 Security Notes

- Messages are encrypted using **Fernet symmetric encryption**
- Keys are derived from your password using **PBKDF2HMAC** with a **random salt**
- Salt is **prepended to the ciphertext** and securely embedded in the image
- ❗ While secure for casual use, **not intended for high-risk or military-grade security**

---

## ⚙️ Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/your-username/steganography-toolkit.git
cd steganography-toolkit

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run steganography_toolkit_random_salt.py
```

---

## 📄 License

📘 This project is open-source and available under the **MIT License**. See the full [LICENSE](LICENSE) file for complete details.

You are free to use, modify, and distribute this software in both personal and commercial projects, as long as you include the original license.
