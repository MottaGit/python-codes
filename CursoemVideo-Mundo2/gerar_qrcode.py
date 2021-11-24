import qrcode

imagem = qrcode.make("github.com/e-Power-UFRGS")
imagem.save("qrcode.jpg")