import qrcode

data_url = "https://www.w3schools.com/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data_url)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')

img.save("qrcode.png")