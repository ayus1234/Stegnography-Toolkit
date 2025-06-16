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
streamlit run steganography_toolkit_random_salt.py
