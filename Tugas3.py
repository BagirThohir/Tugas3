from PIL import Image, ImageDraw, ImageFont
import PIL




# Buka gambar sumber
img = Image.open('zoro.jpg')
width, height = img.size  # lebar dan tinggi untuk kalkulasi koordinat teks

# menambahkan elemen 2d ke gambar yang sudah ada
draw = ImageDraw.Draw(img)

text = '53417914' # ganti dengan npm mu...

# mendefinisikan font baru, lengkap dengan ukurannya
font = ImageFont.truetype('arial.ttf', 100)
# hitung lebar dan tinggi font relatif terhadap gambar utama
textwidth, textheight = draw.textsize(text, font)

# hitung koordinat x, y teks
margin = 15
x = width - textwidth - margin
y = height - textheight - margin

# terapkan watermark
draw.text((x, y), text, font=font)
img.show()

# Simpan gambar
img.save('watermark.png')