import time
import pygame

derss= 1500
dinlenmee = 300
tekrar = 1


def müzik_başlat(muzik_yolu):
    pygame.mixer.init()
    pygame.mixer.music.load(muzik_yolu)
    pygame.mixer.music.play()
try:
    with open("newmusic.txt", "r") as f:
        muzik_dosyasi = f.read().strip()
        if not muzik_dosyasi:
            muzik_dosyasi = "muzik.mp3"
except FileNotFoundError:
    muzik_dosyasi = "muzik.mp3"

def müzik_kapat():
    pygame.mixer.music.stop()

def ders(derss,dinlenmee):
    print("ders başladı")
    müzik_başlat(muzik_dosyasi)
    while True:
        print("""
        [1] müziği kapat""")
        kapat = int(input("seçiminiz:"))
        if kapat == 1:
            müzik_kapat()
            break
    print("ders başladı")
    for zaman in range(derss, 0, -1):
        dakika = zaman // 60
        saniye = zaman % 60
        print(f"{dakika} dakika {saniye} saniye kaldı")
        time.sleep(1)
    print("dinlenme zamanı geldi")
    müzik_başlat(muzik_dosyasi)
    while True:
        print("""
        [1] müziği kapat""")
        kapat = int(input("seçiminiz:"))
        if kapat == 1:
            müzik_kapat()
            break
    dinlenme(dinlenmee)

def dinlenme(dinlen):
    for zaman in range(dinlen,0,-1):
        dakika = zaman // 60
        saniye = zaman % 60
        print(f"{dakika} dakika {saniye} saniye kaldı")
        time.sleep(1)

print("Pomodoro uygulaması başlatılıyor...")
while True:
    if dinlenmee >= 60 and derss <=60  :   
        print(f""" 
    [1] Pomodoroyu başlat.
    [2] Ders süresini değiştir seçilen:{(derss)}sn
    [3] Dinlenme süresini değiştir seçilen:{(dinlenmee/60)}dk
    [4] kaç defa tekrar edileceğini değiştir seçilen:{tekrar}
    [5] alarm sesi ekle
    """)
    
    elif dinlenmee <=60 and derss >= 60:  
        print(f""" 
    [1] Pomodoroyu başlat.
    [2] Ders süresini değiştir seçilen:{(derss/60)}dk
    [3] Dinlenme süresini değiştir seçilen:{(dinlenmee)}sn
    [4] kaç defa tekrar edileceğini değiştir seçilen:{tekrar}
    [5] alarm sesi ekle
    """)

    elif dinlenmee <60 and derss <=60:
        print(f""" 
    [1] Pomodoroyu başlat.
    [2] Ders süresini değiştir seçilen:{(derss)}sn
    [3] Dinlenme süresini değiştir seçilen:{(dinlenmee)}sn
    [4] kaç defa tekrar edileceğini değiştir seçilen:{tekrar}
    [5] alarm sesi ekle
    """)

    else:                
        print(f""" 
    [1] Pomodoroyu başlat.
    [2] Ders süresini değiştir seçilen:{(derss/60)}dk
    [3] Dinlenme süresini değiştir seçilen:{(dinlenmee/60)}dk
    [4] kaç defa tekrar edileceğini değiştir seçilen:{tekrar}
    [5] alarm sesi Değiştir
    """)

    seç = int(input("seçiminiz:"))
    if seç == 1:
        for tekrarr in range(tekrar):
            ders(derss,dinlenmee)
    elif seç == 2:
        sderss = int(input("Yeni Ders süresi(dk cinsinden):"))
        derss = sderss*60

    elif seç == 3:
        sdinlenme = int(input("Yeni Dinleme süresi:"))
        dinlenmee = sdinlenme*60

    elif seç == 4:
        tekrar = int(input("yeni tekrar sayısı:"))
    
    elif seç == 5:
        yeni_muzik = input("Yeni müzik dosyasının tam yolunu giriniz: ")
        try:
            with open("newmusic.txt", "w") as f:
                f.write(yeni_muzik)
            muzik_dosyasi = yeni_muzik
            print("Yeni müzik başarıyla kaydedildi.")
        except Exception as e:
            print(f"Hata oluştu: {e}")

    else:
        print("hatalı girdi")