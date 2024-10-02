import qrcode
import os

def generate_qr_code():
    """
    Prompts the user for a file name to read QR code data from or asks for manual input if the file is not found or is empty.
    Generates a QR code from the obtained data and saves it as 'qrcode.png'.
    """
    def get_data_from_file(file_path):
        """Reads data from the specified file. Returns None if file is empty or doesn't exist."""
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                data = file.read().strip()
            if data:
                return data
        return None

    def get_data():
        """Gets data either from a user-specified file or by user input."""
        file_path = input("Enter the file name (including extension) to read QR code data from: ").strip()
        
        # Try to get data from the specified file
        data = get_data_from_file(file_path)
        
        if data:
            return data
        else:
            print(f"File '{file_path}' not found or is empty.")
            return input("Enter the data to encode in the QR code: ")

    # Get the data for the QR code
    data = get_data()

    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Controls the error correction used for the QR Code
        box_size=10,  # Controls how many pixels each box of the QR code is
        border=4,  # Controls how many boxes thick the border should be
    )

    # Add data to the QR code object
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save the image
    img.save("qrcode.png")

    print("QR code generated and saved as 'qrcode.png'")

# Call the function to generate the QR code
generate_qr_code()
