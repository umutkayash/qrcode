import sys
import qrcode

def generate_qr_code(data, file_name="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)
    print("QR code saved as", file_name)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_qr.py <data> [output_file.png]")
        sys.exit(1)

    data = sys.argv[1]

    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    else:
        output_file = "qrcode.png"

    generate_qr_code(data, output_file)
