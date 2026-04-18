import qrcode as qr 
from PIL import Image

# Create a QR code
qr = qr.QRCode(version=1, box_size=10, border=5)
input_data = input("Enter the data to encode in the QR code: ")
qr.add_data(input_data)
qr.make(fit=True)

# Generate the image
img = qr.make_image(fill='black', back_color='white')
img.save('qrcode.png')