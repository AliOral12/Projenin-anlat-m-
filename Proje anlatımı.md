# Projenin-anlat-m-
Projeyi yaparken ilk başta ubuntu üzerinde yukleme yaptık fakat ubuntunun yavaşlığı yüzünden aynı editör olan python editörü kullandık 
aynı şey sonuçta python editörü öğrenmek 1 ayda öğrenmek tanımak diğer editörlerle aynı olmadığı kesin proje gelişmeye muhtaç bilgisayara 
bazı şeyleri anlatamadım tabı gelecekte buraya daha güzel bir python alam saati yuklerim arkadaşlar 
#sql bağlantısı
#modullerin belirtilmesi veya yuklenmesi
#python tkinter yuklenmesi
#Ve sonuç olarak deneme yanılma ile sonuç geliştirilmesi
1.Kullanılan kutuphaneler
import winsound (Bu kütüphane alarm çaldığı zaman bize yardımcı olacak windwsun beep sesi için geçerlidir
from tkinter import font as tkfont (bu kütüphane sayfa rengi ve sayfa özlleikleri için bize lazım
from tkinter import *(tkinter kutuphanesi bize görsel bir arayüz yapmamız için geçerli
from tkinter import messagebox (görsel bir mesaj oluşturmaya yarar yani direk ekrana yazmak yerine daha iyi bir görsellik oluşturur
import time (zaman kütüphanesi genellikle saat ile ilgili işlem yapmak için kullanılır
import datetime(Bu da time dan farklı olrak ayrıntılı bilgi istiyorsak zamanla ilgili bu kutuphaneyi kullanırız
import math(matematik kütüphanesi mtematiksel fonkiyonlar için kullanılır
#Şimdi sıra geldi buda ne yaptık anlatmaya
root = Tk()............ (tkinter penceresini rahat kullana bilmek için her zaman işimize yarayacak root kullandık.....
root.geometry("640x480").......(Sayanın buyukluğünü ayarladık uzunluğu 640 genişlik 480 oldu
root.frame = Frame(root)  .....(frame yani pencere oluşturuyoruz
root.frame.pack(fill = "both")   (pencereyi pack komutu ile etkinleştirdik
label = Label(root, text= "Welcome", bg = "green", fg = "white", font=("Times", 100)) ekrana wilcem yazıyor ve renk yeşil oluyo font=("Times", 100)) welcome mesajınının buyukluğunu belirledik.
label.pack(side= "top", fill = "both", expand = 1)  ....(expand yanı genişliği 1 olacak
root.title_font = tkfont.Font(family = "Times", size = 100, weight = "bold", slant = "italic") .......burda ise yazı tipi ve buyukluğunu ve italic 
root.title("alarm saati uygulama")           ekranın en üst sol köşesinde alarm saati uygulaması yazacak



#veri tabanı bağlantısı

import sqlite3 sqlite modulunu kullanmak için tanımlama yaptıkkkkkkk 
baglanti = sqlite3.connect('veriler.db')  veriler adında veri tabanına bağlandık yoksa 0 değeri döndürecek ve çalışmayacak
if(baglanti): 
    print('Baglanti Başarılı!')
else:
    print('Bağlantı Başarısız!')
 

a = baglanti.cursor() ...........sqliteyi daha rahat kullanabilmek için a değerine atama yaptık maksat daha rahat kullanmak

a.execute('''INSERT INTO alarmuygulaması(saat,dakika,saniye,açıklama) VALUES ('12','13','15','bugun ders var')''')  burda ise veri tabanına inser komutu ile ekleme yaptık
baglanti.commit() .......commit ile veriler işlendi
baglanti.close()...........close ile sayfa kapatıldı
def alarm():
    şimdikizaman = tick() ..................tick fonksiyonunu çağırdık tick fonksiyonun gittiği yer altta buda root.after komutu ileher 500 milisaniyede yenilenecek ve biz bu değeri şimdik zaman değerine atayacaz
   
    wake_entry_button = Button(root, text="Set Alarm",bg='Blue') ......alarm butonu renk mavi ....
    wake_entry_button.pack(side = BOTTOM).............alarm butonuna bastığımızdametin texi oluşturuyo..
  ...
    wake = time.strftime("%I:%M:S") ....şimdiki  saat dakika saniye değeri alınıyor
    
    #girilen textleri saat dakika ve saniye değerine atama

etiket=Label(text='Saat değerini girin',bg='green')  ............saat değeri için bilgi girişi yapılıyor
saat=Entry(root)..................girilen değer saat değişkenine atanıyor..........

etiket.pack()............etiket aktifleştirme işlemi yapılıyor


frame1 = Frame(padx=20,pady=20)       .............frame ile texin özellikleri belirleniyor........
frame1.pack()...............bu komut olmadan etkinleşmezzzzzzz


giris =Entry(width=20).....girilen değerler giris diye bir kısal oluşuyor
giris.pack()...............etkinleştirme
etiket=Label(text='Dakika değerini girin',bg='green') ........dakika değeri ekranayazılıyo

dakika=Entry(root)........girilen değer dakika değişkenine atandı
etiket.pack().............etkinleştirme...........yaz maz sanız ekranda hiçbir şey gözükmez


frame1 = Frame(padx=20,pady=20) ............2.inci pencere dakika penceresi
frame1.pack().................etkin olması çin yapılan komut

giris=Entry(width=20)........giris değişkeni hafızada buna bir şey yapmak için yol diyebiliriz
giris.pack()....................giris ile aktif etme 
etiket=Label(text='Saniye değerini girin',bg='green') ........saniye değerini gir
saniye=Entry(root)..............saniye değişkenine atama yapılıyor
etiket.pack()


frame1 = Frame(padx=20,pady=20)................20 ye 20 frame pencersi  olusuyoooo
frame1.pack().............aktif etttttt

giris =Entry(width=20).............giris ile yol 
giris.pack()..............aktif et
etiket=Label(text='Açıklama',bg='green')............renk yeşil ve tect metimn girilecek
açıklama=Entry(root)................açıklama diğişkenine atama yapıldı
etiket.pack()................aktif edildi


frame1 = Frame(padx=20,pady=20).................pencere oluştuuuuuuu
frame1.pack()...........aktif edildi


giris=Entry(width=20)............giriş değerine atadık
giris.pack().................aktif ettik
ment = StringVar()

button_alarm = Button(text = "Alarm",bg='Blue') ...........alarm butonu oluştu ve tenk maviiiiiiii
button_alarm.config(command = alarm)........bu alarm tusuna bastığımızda alarm fonksiyonunu çağıracak ve çalışmaya başlayacak kodmuz
button_alarm.pack()..........alarmı pencerede etkinleştirdik

a=saat.get()...................saat değerini getirmesini istedik ama getirmedi kodun bu kısmı çalışsa çok daha rahat olurdu
b=dakika.get()...................b değerine atadık   aynı a daki gibi
c=saniye.get()   .................c değerine atadık aynı a daki gibiiiiiiiiiii



an = datetime.datetime.now().............şimdiki zamanı an değerine atadık localtime kullanmaya gerek yokmuş bu komut aynı işi yapıyomuşşş.

time1=an.hour)*3600+int(an.minute)*60+int(an.second) ..........saat 3600 değeriyle çarptık dakikayı 60 saniyeyi 1 ile ve topladık
bubun nedeni atıyorum saat 12 kullanıcı 13 deüğerini girdi arada 3600 saniye fark var ve her saniye sayma işlemi yapılacak geri sayım gibi
ve eşit olunca alarm ötecek(Keşke :D bilgisayara bunu yaptıramadım ama güzel uygulamaydı doğrusu)
time2=int(a)+int(b)+int(c)
time=time2-time1; aradaki fark time değerine atandı ve time değeri countdown komutu ile geri sayıma geçtiiii..

countdown(time)...
     
def countdown(count): 
    
    seconds=math.floor(fark%60)...........saniye 60 bölünüyor malum saniye 60 tan fazla olamaz
    minutes=math.floor((fark/60)%60).......bu kısacası dakikayı bulmaya yarıyor ....
    hours=math.floor((fark/3600))............buda saati bulmaya yarıyor
    #label['text'] ="Saat: "+ str(an.hour)+ " Dakika:  " +str(an.minute)+ " Saniye: " +str(an.second) " sonra alarm çalacak"
    label['text'] = "Saat: "+ str(hours)

    if count >= 0:
        label.after(1000, countdown,count-1)..........count yada time değeri 0 dan buyukse alarm zaman gelmedi tekrar countdown fonksiyonuna git demek...
    else:
        for x in range(3):   ................eğer 0 olmuşsa range fonksiyonu ile 3 defa dönecekkk windowsun beep sesini çıkaracakkkk
         winsound.Beep(1000,1000)...........ses çıkarma 
        label['text']="Zaman doldu!"   ...............pythonda ekrana zaman doldu yazısı çıkar......
      
         


def tick(time1 = ""):..........bu fonksiyonu çağırmıştık yukarda bize her 500ms de saat değerini guncelleştirecek

    time2 = time.strftime("%I:%M:%S") ............saat ,dakika ve saniye değerini time2 değişkenine atayacak
    if time2 != time1:...................eşit değilse 1 önceki saati her saniye güncelleştirme yapmamız içim kontrol ediyozzz
        time1 = time2...................eşit değilse yeni zaman değerini ataaaaaa
        label.config(text = time1)..........yeni saat değerini yaz
    label.after(500, tick).........500ms bekle sobra tick fonksiyonuna giittttttttttttttt
    return time1..........yeni zaman değerini döndürrr

tick().............fonksiyon
root.mainloop()................ana pencere
