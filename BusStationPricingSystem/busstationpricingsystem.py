
print("\t menü \t \n 1.otobüs \n 2.taksi \n  \n ")

araba=int(input("giriş yapacağınız arabanın türünü giriniz:"))

while True:
    if araba==1:
        print("otobüs ile giriş yapıldı ")
        saat=int(input("otobüsünüz kaç saat kalacak? :"))
        if 0<saat<=3:
            ucret = (saat * 1.5)
            print(f"{saat} için ücret:{ucret} TL'dir ")
            break
        elif 3<saat<=6:
            ucret=(saat*2)
            print(f"{saat} için ücret:{ucret} TL'dir ")
            break
        else:
            ucret=(saat*3)
            print(f"{saat} için ücret:{ucret} TL'dir ")
            break
    elif araba==2:
        print("Taksi ile giriş yapıldı")
        saat = int(input("Taksiniz kaç saat kalacak? :"))
        break
        if 0<saat<=4:
            print(f"{saat} için ücret:{saat} TL'dir ")
            break
        elif 4<saat<=8:
            ucret=(saat*2)
            print(f"{saat} için ücret:{ucret} TL'dir ")
            break
        else:
            ucret=(saat*4)
            print(f"{saat} için ücret:{ucret} TL'dir ")
            break