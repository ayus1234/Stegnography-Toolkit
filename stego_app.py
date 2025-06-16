import streamlit as st
from PIL import Image
import numpy as np
import io
from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

st.set_page_config(page_title="Steganography Toolkit", layout="centered")

# ---------- Encryption Helpers (With Random Salt) ----------
def generate_key(password: str, salt: bytes) -> bytes:
    password_bytes = password.encode()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password_bytes))

def encrypt_message(message: str, password: str) -> bytes:
    salt = os.urandom(16)  # Generate 128-bit salt
    key = generate_key(password, salt)
    fernet = Fernet(key)
    encrypted = fernet.encrypt(message.encode())
    return salt + encrypted  # Salt is prepended

def decrypt_message(token: bytes, password: str) -> str:
    salt = token[:16]
    encrypted = token[16:]
    key = generate_key(password, salt)
    fernet = Fernet(key)
    return fernet.decrypt(encrypted).decode()

# ---------- Steganography ----------
def embed_text_in_image(image: Image.Image, text: bytes) -> Image.Image:
    img = np.array(image.convert("RGB"))
    flat_img = img.flatten()

    binary_text = ''.join(format(byte, '08b') for byte in text)
    binary_len = format(len(binary_text), '032b')  # 32 bits for length

    data = binary_len + binary_text
    if len(data) > len(flat_img):
        raise ValueError("Message too long to embed in image.")

    for i in range(len(data)):
        flat_img[i] = (flat_img[i] & ~1) | int(data[i])  # Set LSB

    new_img = np.reshape(flat_img, img.shape)
    return Image.fromarray(new_img)

def extract_text_from_image(image: Image.Image) -> bytes:
    img = np.array(image.convert("RGB")).flatten()
    length_bits = ''.join(str(img[i] & 1) for i in range(32))
    msg_len = int(length_bits, 2)

    data_bits = ''.join(str(img[32 + i] & 1) for i in range(msg_len))
    byte_data = [data_bits[i:i+8] for i in range(0, len(data_bits), 8)]
    return bytes([int(b, 2) for b in byte_data])

# ---------- Image-In-Image Steganography ----------
def embed_image_in_image(cover: Image.Image, secret: Image.Image) -> Image.Image:
    cover = cover.convert("RGB")
    secret = secret.convert("RGB").resize(cover.size)

    cover_arr = np.array(cover)
    secret_arr = np.array(secret)

    stego_arr = (cover_arr & 0b11111100) | (secret_arr >> 6)
    return Image.fromarray(stego_arr.astype('uint8'))

def extract_image_from_image(stego_img: Image.Image) -> Image.Image:
    stego_arr = np.array(stego_img.convert("RGB"))
    secret_arr = (stego_arr & 0b00000011) << 6
    return Image.fromarray(secret_arr.astype('uint8'))

# ---------- Streamlit App ----------
st.title("🕵️‍♂️ Steganography Toolkit (Random Salt Enhanced)")

tab1, tab2 = st.tabs(["🔐 Text Encryption + Hiding", "🖼️ Hide Image Inside Image"])

# ---------- Tab 1: Text Hiding ----------
with tab1:
    st.header("🔒 Embed & Extract Encrypted Text")

    mode = st.radio("Choose Mode", ["Embed Message", "Extract Message"], horizontal=True)

    if mode == "Embed Message":
        cover_file = st.file_uploader("Upload Cover Image", type=["png", "jpg", "jpeg"])
        password = st.text_input("Enter Password", type="password")
        secret_text = st.text_area("Secret Message")

        if st.button("Embed"):
            if not (cover_file and password and secret_text):
                st.warning("Please upload an image, enter a password, and write a message.")
            else:
                image = Image.open(cover_file)
                try:
                    encrypted = encrypt_message(secret_text, password)
                    stego_image = embed_text_in_image(image, encrypted)

                    st.image(stego_image, caption="Image with Hidden Message")

                    buf = io.BytesIO()
                    stego_image.save(buf, format="PNG")
                    byte_im = buf.getvalue()
                    st.download_button("Download Stego Image", byte_im, "stego_image.png", "image/png")

                except Exception as e:
                    st.error(f"Error embedding message: {e}")

    elif mode == "Extract Message":
        stego_file = st.file_uploader("Upload Image with Hidden Message", type=["png", "jpg", "jpeg"])
        password = st.text_input("Enter Password", type="password")

        if st.button("Extract"):
            if not (stego_file and password):
                st.warning("Please upload a stego image and enter the password.")
            else:
                image = Image.open(stego_file)
                try:
                    hidden_bytes = extract_text_from_image(image)
                    decrypted = decrypt_message(hidden_bytes, password)
                    st.success("Decrypted Message:")
                    st.code(decrypted)
                except Exception as e:
                    st.error(f"Error extracting message: {e}")

# ---------- Tab 2: Image-In-Image Hiding ----------
with tab2:
    st.header("🖼️ Hide Image Inside Another Image")

    mode2 = st.radio("Choose Mode", ["Embed Image", "Extract Image"], horizontal=True)

    if mode2 == "Embed Image":
        cover = st.file_uploader("Upload Cover Image", type=["png", "jpg", "jpeg"], key="cover")
        secret = st.file_uploader("Upload Secret Image to Hide", type=["png", "jpg", "jpeg"], key="secret")

        if st.button("Hide Image"):
            if not (cover and secret):
                st.warning("Please upload both a cover image and a secret image.")
            else:
                cover_img = Image.open(cover)
                secret_img = Image.open(secret)

                try:
                    stego_img = embed_image_in_image(cover_img, secret_img)
                    st.image(stego_img, caption="Image with Hidden Image")

                    buf = io.BytesIO()
                    stego_img.save(buf, format="PNG")
                    byte_im = buf.getvalue()
                    st.download_button("Download Stego Image", byte_im, "hidden_image.png", "image/png")

                except Exception as e:
                    st.error(f"Error hiding image: {e}")

    elif mode2 == "Extract Image":
        stego = st.file_uploader("Upload Stego Image", type=["png", "jpg", "jpeg"], key="extract")

        if st.button("Reveal Hidden Image"):
            if not stego:
                st.warning("Please upload the stego image.")
            else:
                stego_img = Image.open(stego)

                try:
                    extracted = extract_image_from_image(stego_img)
                    st.image(extracted, caption="Extracted Hidden Image")

                    buf = io.BytesIO()
                    extracted.save(buf, format="PNG")
                    byte_im = buf.getvalue()
                    st.download_button("Download Extracted Image", byte_im, "extracted_image.png", "image/png")

                except Exception as e:
                    st.error(f"Error extracting image: {e}")