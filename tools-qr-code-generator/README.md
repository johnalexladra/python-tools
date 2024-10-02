# tools-qr-code-generator
A simple QR Code generator using Python

### 1. Install Required Libraries

First, you need to install the `qrcode` library and `Pillow`, which is used for image processing. You can install these using pip:

```bash
pip install qrcode[pil]
```

### 2. Running the Script

Save the script to a file, for example, `index.py`, and run it using Python:

```bash
python index.py
```

After running the script, you should see a file named `qrcode.png` in the same directory, containing the generated QR code.

### 3. Customization

You can customize the QR code by modifying parameters like:

- `version`: Controls the size of the QR code. The higher the version, the more data it can store.
- `error_correction`: Controls the error correction level. Higher levels allow for more data recovery but make the QR code denser.
- `box_size`: Controls the size of each box in pixels.
- `border`: Controls the thickness of the border (minimum is 4).

Feel free to adjust these settings to fit your needs!