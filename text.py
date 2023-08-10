import tkinter as tk
from gtts import gTTS
import qrcode

class SesliOkumaVeQRKoduUygulamasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Sesli Okuma ve QR Kodu Uygulaması")

        self.etiket = tk.Label(root, text="Metin:")
        self.etiket.pack()

        self.metin_alani = tk.Text(root, height=5, width=40)
        self.metin_alani.pack()

        self.sesli_oku_dugme = tk.Button(root, text="Sesli Oku", command=self.sesli_oku)
        self.sesli_oku_dugme.pack()

        self.qr_kodu_olustur_dugme = tk.Button(root, text="QR Kodu Oluştur", command=self.qr_kodu_olustur)
        self.qr_kodu_olustur_dugme.pack()

    def sesli_oku(self):
        metin = self.metin_alani.get("1.0", "end-1c")
        if metin:
            tts = gTTS(metin, lang='tr')
            tts.save('sesdosyasi.mp3')
            self.bilgi_penceresi("Ses dosyası kaydedildi: sesdosyasi.mp3")

    def qr_kodu_olustur(self):
        ses_dosyasi_adı = 'sesdosyasi.mp3'
        if ses_dosyasi_adı:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(ses_dosyasi_adı)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            img.save('qrcode.png')
            self.bilgi_penceresi("QR kodu oluşturuldu: qrcode.png")

    def bilgi_penceresi(self, mesaj):
        bilgi_penceresi = tk.Toplevel(self.root)
        bilgi_penceresi.title("Bilgi")
        bilgi_metin = tk.Label(bilgi_penceresi, text=mesaj)
        bilgi_metin.pack()

if __name__ == "__main__":
    root = tk.Tk()
    uygulama = SesliOkumaVeQRKoduUygulamasi(root)
    root.mainloop()
