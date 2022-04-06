# 20010011076 DOGUKAN BICI
import random
import sys
while True:
    print("---------------MAYIN TARLASI OYUNU---------------")
    mayin=[]
    mayintarlasi = []
    while True:
        ekranboyut = int(input("Oyun boyutunu giriniz(oyundan cikmak icin 0 tusunu kullanabilirsiniz)..."))
        if ekranboyut < 10:
            if ekranboyut == 0:
                sys.exit()
            print("Oyun alani en az 10 olacak sekilde giriniz")
        else:
            break
    for i in range(ekranboyut):
        mayintarlasi.append(["?"]*ekranboyut)
            # mayintarlasi.append([i,j,"?"])
    def oyunAlaniYazdir(mayintarlasi):
        for satir in mayintarlasi:
            print(" ".join(satir))
    def mayinRastgele(mayintarlasi):
        x = random.randint(0, len(mayintarlasi[0]) - 1)
        y = random.randint(0, len(mayintarlasi[1]) - 1)
        #mayin çakışması kontrolü
        durum = True
        for j in range(len(mayin)):
            if mayin[j] == [x, y]:
                durum = False
        if (durum):
            mayin.append([x, y])
        else:
            mayinRastgele(mayintarlasi)
    def mayinOlustur():
        for i in range(int((ekranboyut * ekranboyut) * 0.30)):
            mayinRastgele(mayintarlasi)
    mayinOlustur()
    def mayinDedektor(x,y):
        if (x > 0):
            x1=x-1
        else:
            x1=x
        if (y > 0):
            y1=y-1
        else:
            y1 = y
        if (x < ekranboyut):
            x2 = x + 1
        else:
            x2 = x
        if (y < ekranboyut ):
            y2 = y + 1
        else:
            y2 = y
        mayinSyc=0
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                try:
                    mayin.index([i, j])
                    mayinSyc=mayinSyc+1
                    if([i,j]==[x,y]):
                        return -1
                except:
                    None
        return mayinSyc
    def oyunAlani():
        print("Oyunu oynamak istediginiz modu seciniz... \n 1-Gizli Mod 2-Acik Mod")
        secim = input("secim: ")
        if (secim=="1"):
            None
        elif(secim=="2"):
            for j in range(len(mayin)):
                mayintarlasi[mayin[j][0]][mayin[j][1]] = "X"
        else:
            print("Yanlis secim yaptiniz.")
            oyunAlani()
        oyunAlaniYazdir(mayintarlasi)
        syc = 0
        while ekranboyut * ekranboyut - syc > len(mayin):
            satir = int(input("satir: ")) - 1
            sutun = int(input("sutun: ")) - 1
            if (str(mayintarlasi[satir][sutun]) == "?" or str(mayintarlasi[satir][sutun]) == "X"):
               mayinAdet = mayinDedektor(satir, sutun)
               if (mayinAdet == -1):
                    print("Mayina bastiniz")
                    for j in range(len(mayin)):
                        mayintarlasi[mayin[j][0]][mayin[j][1]] = "X"
                    oyunAlaniYazdir(mayintarlasi)
                    print("kaybettiniz puaniniz : {}".format(syc))
                    break
               else:
                    mayintarlasi[satir][sutun] = str(mayinAdet)
                    print("Siradaki tahmininiz")
                    oyunAlaniYazdir(mayintarlasi)
                    syc = syc + 1
                    if ekranboyut * ekranboyut - syc <= len(mayin):
                        print("kazandiniz puaniniz : {}".format(syc))
            else:
                print("Ayni Noktayi Secemezsiniz")
        print("Oyun Bitti")
    oyunAlani()





