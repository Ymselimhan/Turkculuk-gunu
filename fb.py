import turtle
import re
import docx  # pip install python-docx

# 📄 .docx dosyasının tam yolu
source_path = r"C:\Users\ymsel\Desktop\python\3mayıs\ganesh.docx"

# 🔧 Ölçekleme ve pozisyon ayarı
scale = 0.4
offset_x = -20   # biraz sola kaydırıldı
offset_y = -50  # daha yukarıya alındı (önce 80’di)

# Docx'ten veri çekme
data = docx.Document(source_path)
coordinates = []
colours = []

for i in data.paragraphs:
    try:
        coord_stg_tup = re.findall(r'\([-+]?\d*\.\d*(?:[eE][-+]?\d+)? ?\, ?[-+]?\d*\.\d*(?:[eE][-+]?\d+)?\)', i.text)
        coord_num_tup = []

        color_stg_tup = re.findall(r'\([-+]?\d*\.\d*(?:[eE][-+]?\d+)? ?\, ?[-+]?\d*\.\d*(?:[eE][-+]?\d+)? ?\, ?[-+]?\d*\.\d*(?:[eE][-+]?\d+)?\)', i.text)
        color_val = re.findall(r'[-+]?\d*\.\d*', color_stg_tup[0])
        color_val_lst = [float(k) for k in color_val]
        colours.append(tuple(color_val_lst))

        for j in coord_stg_tup:
            coord_pos = re.findall(r'[-+]?\d*\.\d*', j)
            # Ölçek uygulanıyor + pozisyon kaydırma
            x = float(coord_pos[0]) * scale + offset_x
            y = float(coord_pos[1]) * scale + offset_y
            coord_num_tup.append((x, y))

        coordinates.append(coord_num_tup)
    except:
        pass

# 🖥️ Ekran ayarları
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")  # Arka planı kırmızı yapıyoruz

# 🐺 Kurt çizimi kalemi
pen = turtle.Turtle()
pen.speed(10)
pen.hideturtle()
turtle.tracer(2)

# Kurt figürü çizimi
for i in range(len(coordinates)):
    draw = True
    path = coordinates[i]
    col = colours[i]

    # Beyaz olan yerleri kırmızı yapalım
    if col == (1.0, 1.0, 1.0):  # Beyaz renk
        col = (1.0, 0.0, 0.0)  # Kırmızıya çevir

    pen.color(col)
    pen.begin_fill()
    for order_pair in path:
        x, y = order_pair
        y = -1 * y  # Y ekseni yansı
        if draw:
            pen.up()
            pen.goto(x, y)
            pen.down()
            draw = False
        else:
            pen.goto(x, y)
    pen.end_fill()

# 🏺 Göktürk harfleri
gokturk_harfleri = ['𐱅', '𐰇', '𐰼', '𐰚']
gokturk_pen = turtle.Turtle()
gokturk_pen.hideturtle()
gokturk_pen.speed(3)
gokturk_pen.penup()

# Yazının konumu (biraz yukarıda, ortalı)
gokturk_pen.goto(-130, -200)

for harf in gokturk_harfleri:
    gokturk_pen.write(harf, font=("Arial", 50, "normal"))
    gokturk_pen.forward(60)

# Ekranı açık tut
turtle.done()
