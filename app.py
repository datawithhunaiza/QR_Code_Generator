
import streamlit as st
import qrcode
from io import BytesIO

# Page configuration
st.set_page_config(
    page_title="QR Code Generator",
    page_icon="📱",
    layout="centered"
)

# Application heading
st.title("📱 QR Code Generator")
st.write("Generate QR codes for your text or URLs instantly!")

# User input
data = st.text_input(
    "Enter your text or URL:",
    placeholder="https://www.google.com"
)

# Generate QR Code
if st.button("Generate QR Code", type="primary"):

    if data.strip():

        # Create QR code
        qr = qrcode.QRCode(
            box_size=10,
            border=4
        )

        qr.add_data(data.strip())
        qr.make(fit=True)

        # Generate image
        img = qr.make_image(
            fill_color="black",
            back_color="white"
        )

        # Convert image into bytes
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        qr_bytes = buffer.getvalue()

        # Display QR code
        st.success("QR Code generated successfully!")

        st.image(qr_bytes, caption="Your QR Code", width=250)

        # Download button
        st.download_button(
            label="⬇️ Download QR Code",
            data=qr_bytes,
            file_name="my_qrcode.png",
            mime="image/png"
        )

    else:
        st.warning("Please enter some text or a URL first.")

st.divider()
st.caption("Built by Hunaiza Sultan")
