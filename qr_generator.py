import qrcode
from PIL import Image

# Function to generate a QR code
def generate_qr(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Example usage
if __name__ == '__main__':
    data_to_encode = 'https://www.example.com'
    filename = 'qrcode.png'
    generate_qr(data_to_encode, filename)
    print(f'QR code saved as {filename}')