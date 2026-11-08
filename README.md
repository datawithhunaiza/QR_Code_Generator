# QR Code Generator 

A simple and user-friendly **QR Code Generator** built with Python and Streamlit. This application allows users to generate QR codes from text or URLs and download them as PNG images.

##  Features

- Generate QR codes from text or URLs.
- Simple and interactive user interface using Streamlit.
- Download generated QR codes as PNG images.
- Easy to use and beginner-friendly.

##  Technologies Used

- **Python** – Core programming language.
- **Streamlit** – User interface.
- **qrcode** – QR code generation.
- **Pillow (PIL)** – Image processing.

##  Project Structure

```text
qr_code_generator/
│
├── app.py              # Main application
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
└── .gitignore          # Ignored files
```

##  Installation & Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone <your-repository-link>
```

### 2. Navigate to the Project Directory

```bash
cd qr_code_generator
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

Alternatively:

```bash
pip install streamlit qrcode[pil]
```

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser.

##  How to Use

1. Open the QR Code Generator application.
2. Enter the text or URL you want to convert into a QR code.
3. Generate your QR code.
4. Download the generated PNG image.

##  Project Purpose

This project was developed to strengthen my Python programming skills and gain practical experience with Python libraries, image generation and building interactive applications using Streamlit.

##  Author

**Hunaiza Sultan**

Computer Systems Engineering Student | Python & AI/ML Enthusiast

---

⭐ If you find this project useful, feel free to star the repository!
