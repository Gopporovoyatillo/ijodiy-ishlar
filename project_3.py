import qrcode
code=qrcode.QRCode(box_size=10,border=1)
code.add_data("""Venv moduli ixtiyoriy ravishda tizim saytlari kataloglaridan ajratilgan o'z sayt kataloglari bilan
 engil 'virtual muhit' yaratishni qo'llab -quvvatlaydi. Har bir virtual muhit o'z Python ikkilikiga ega
  (bu muhitni yaratish uchun ishlatilgan ikkilik versiyasiga to'g'ri keladi) va o'z sayt kataloglarida o'rnatilgan
   mustaqil Python paketlariga ega bo'lishi mumkin.""")
img=code.make_image(fill_color="red",back_color="yellow")
img.save("OLLIT_DEV_QR.png")