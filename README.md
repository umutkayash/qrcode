
# QR Code Generator

This Python script generates QR codes based on input data. It utilizes the `qrcode` library to create QR codes that can be used for various purposes, including URLs, text messages, or other data that needs to be easily accessible via a QR scan.

## Features

- Generate high-quality QR codes with customizable file names.
- High error correction capability.

## Prerequisites

Before running this script, you need to install the `qrcode` library. You can install it using pip:

```bash
pip install qrcode[pil]
```

## Usage

To use this script, you need to provide the data you want to encode in the QR code as a command-line argument. Optionally, you can also specify a custom file name for the output image.

```bash
python qrcode.py "Your data here" [output_file.png]
```

If you do not specify an output file, the QR code will be saved as `qrcode.png` by default.

### Examples

Generate a QR code with default settings:

```bash
python qrcode.py "Hello, World!"
```

Generate a QR code with a custom file name:

```bash
python qrcode.py "https://www.example.com" "custom_qrcode.png"
```

## Contributing

Feel free to fork this project and submit a pull request if you have suggestions or improvements.

## License

This script is released under the MIT License. See the LICENSE file for more details.
