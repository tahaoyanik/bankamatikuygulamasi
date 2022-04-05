print("""
*********************************
    BANKAMATİK UYGULAMASI
    
    İşlemler;
    
    1- Para Çekme
    2- Para Yatırma
    3- Bakiye Sorgulama
    4- Şifre Değiştirme
    5- Para Gönderme
*********************************
""")

şifre=250917
bakiye=2500

while True:
    işlem=int(input("işlem seçiniz:"))
    if işlem==1:
        tutar=int(input("tutar giriniz:"))
        bakiye-=tutar
        print("Paranızı Alabilirsiniz.")

    elif işlem==2:
        y_tutar=int(input("Yatırılacak Tutar:"))
        bakiye+=y_tutar
        print("Paranız yatırılmıştır")



    elif işlem==3:
        print("Güncel bakiyeniz: {}".format(bakiye))

    elif işlem==4:
        mevcut_şifre=int(input("mevcut şigreniz:"))
        yeni_şifreniz=int(input("yeni şifreniz:"))
        mevcut_şifre=yeni_şifreniz
        print("şifreniz başarı ile güncellenmiştir. Yeni şifreniz {}".format(yeni_şifreniz))


    elif işlem==5:
        g_tutar=int(input("Gönderilecek Tutar:"))
        bakiye-=g_tutar
        print("Gönderme işleminiz tamamlanmıştır.")

    else:
        ("Geçersiz işlem.")
