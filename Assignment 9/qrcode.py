import segno
micro_qrcode = segno.make('email:mohamad.nematizadehhh@gmail.com', error='q')
micro_qrcode.save('qrcode.png', scale=4, dark='steelblue')