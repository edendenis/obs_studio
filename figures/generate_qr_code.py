import qrcode

# URL para a qual o QR Code deve redirecionar
url = 'https://www.edftechnology.com'

# Gera o QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Cria uma imagem do QR Code gerado
img = qr.make_image(fill_color="black", back_color="white")

# Salva a imagem em um arquivo
img.save('edf_qr.png')
