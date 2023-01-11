import qrcode as qrcode

code = qrcode.QRCode(
    version=1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 50,
    border=10
)

code.add_data("https://www.linkedin.com/in/eda-nur-yardım-9a474a202/")
code.make(fit=True)

image = code.make_image(fill_color="white",back_color="black")
image.save("vol1.png")
