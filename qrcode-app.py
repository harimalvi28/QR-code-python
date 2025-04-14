import qrcode
from PIL import Image

def generate_qr_with_logo(data, filename="qrcode_with_logo.png", logo_path="logo.png", size=10, border=4):
    # Create QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction to handle logo overlay
        box_size=size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create the QR code image
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    # Load the logo
    try:
        logo = Image.open(logo_path)

        # Calculate size and position
        qr_width, qr_height = qr_img.size
        logo_size = qr_width // 4  # Resize logo to 1/4 of QR code
        logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

        pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
        qr_img.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)

    except FileNotFoundError:
        print(f"Logo file '{logo_path}' not found. Generating QR without logo.")

    qr_img.save(filename)
    print(f"QR Code saved as '{filename}'.")

# Example usage
if __name__ == "__main__":
    text = input("Enter the text or URL to encode: ")
    logo_path = input("Enter path to logo image (e.g., logo.png): ")
    generate_qr_with_logo(text, logo_path=logo_path)
