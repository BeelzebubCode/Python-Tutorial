import qrcode
import qrcode.constants
import crcmod.predefined

def generate_crc16(data):
    """Generate CRC-16 checksum."""
    crc16 = crcmod.predefined.mkCrcFun('crc-ccitt-false')
    crc = crc16(data.encode('utf-8'))
    return '{:04X}'.format(crc)

def format_amount(amount):
    """Format amount to fit QR code specification."""
    return f'54{len(f"{amount:.2f}"):02d}{amount:.2f}'

def create_prommptpay_qr_code(phone_number, amount, filename):
    phone_number = '0066' + phone_number[1:]

    # QR Code payload fields
    payload_format = "000201"
    point_of_initiation_method = "010211"
    merchant_name = "2937" # Name of the merchant
    promptPay_identify = "0016A000000677010111"
    promptPay_id = f"0113{phone_number}"
    country_code = "5802TH"
    transaction_currency = "5303764" # THB
    transaction_amount = format_amount(amount)
    crc_placeholder = "6304"

    # Combine all data into QR code data
    qr_data = (
        payload_format + 
        point_of_initiation_method +
        merchant_name +
        promptPay_identify +
        promptPay_id +
        transaction_currency + 
        country_code +
        transaction_amount + 
        crc_placeholder 
    )
    print(qr_data)

    # Calculate CRC
    crc = generate_crc16(qr_data)
    qr_data += crc

    # Create QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(qr_data)
    qr.make(fit=True)

    # Create QR Code image
    img = qr.make_image(fill='black', back_color='white')

    # Define the path and filename
    path = 'C:/Python/projectPython/QR_Code_PromptPay/images/'
    full_filename = path + filename

    # Save QR Code image
    img.save(full_filename)
    print(f"QR Code saved as {full_filename}")

if __name__ == "__main__":
    phone_number = input("Enter PromptPay phone number (0812345678): ")
    amount = float(input("Enter amount to receive: "))
    filename = f"promptpay_qrcode_{amount:.2f}baht.png"

    create_prommptpay_qr_code(phone_number, amount, filename)