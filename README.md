# 🕵️‍♂️ Steganography Toolkit

A powerful and beginner-friendly **Steganography and Encryption Toolkit** built with [Streamlit](https://streamlit.io/). This app allows you to hide encrypted text inside images or embed one image inside another using simple LSB (Least Significant Bit) techniques.

---

## 🔐 Features

- **Text Encryption with Random Salt** using `Fernet` and `PBKDF2HMAC`
- **Text-in-Image Hiding** (encrypt + embed message into an image)
- **Image-in-Image Hiding** (embed one image inside another)
- **Message Extraction & Decryption**
- **Image Extraction from Stego Images**
- **No server-side storage** – All operations are done locally in your browser

---

## 🧪 Technologies Used

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- [Pillow (PIL)](https://pypi.org/project/Pillow/)
- [NumPy](https://numpy.org/)
- [cryptography](https://cryptography.io/)

---

## 🚀 Getting Started

### 🔧 Setup Locally

```bash
git clone https://github.com/your-username/steganography-toolkit.git
cd steganography-toolkit
pip install -r requirements.txt
streamlit run stego_app.py
```
## 🖥️ How to Use

### 🔐 Tab 1: Text Encryption + Hiding

#### 🔸 Embed Message:
- Upload a **cover image**.
- Enter a **password** (used to derive a strong encryption key).
- Enter your **secret message**.
- Click **Embed** and download the generated image with hidden data.

#### 🔸 Extract Message:
- Upload the **stego image**.
- Enter the **same password** used during embedding.
- Click **Extract** to reveal the hidden message.

> 💡 **Random salt** is used per message, ensuring stronger cryptographic security. Salt is safely stored inside the image along with the encrypted message.

---

### 🖼️ Tab 2: Image-in-Image Hiding

#### 🔸 Embed Image:
- Upload a **cover image**.
- Upload the **secret image** to hide.
- Click **Hide Image** and download the result.

#### 🔸 Extract Image:
- Upload the **stego image**.
- Click **Reveal Hidden Image** to view and download the hidden image.

---

## 🔐 Security Notes

- Messages are encrypted using `Fernet` with keys derived from passwords via `PBKDF2HMAC` + **random salt**.
- Salt is securely **prepended to the ciphertext** and extracted automatically during decryption.
- While this tool provides basic encryption and steganography,  
  **do not use it for high-risk or government-level secure communications**.
