# Make-Your-Own-QR-Code

A simple Python script that generates a QR code image from user input.

## Requirements

- Python 3
- `qrcode` package
- `Pillow` package

## Setup

1. Create and activate your virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install qrcode pillow
```

## Usage

Run the script and enter the text or URL you want encoded in the QR code:

```powershell
python main.py
```

The script will save the generated image as `qrcode.png` in the project folder.

## How it works

- Prompts the user for data to encode
- Builds a QR code object with `qrcode.QRCode`
- Generates an image using `PIL`
- Saves the final QR code image as `qrcode.png`
