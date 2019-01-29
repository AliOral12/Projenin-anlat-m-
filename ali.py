import sqlite3
baglanti = sqlite3.connect('veriler.db')
if(baglanti):
    print('Baglanti Başarılı!')
else:
    print('Bağlantı Başarısız!')
 

a = baglanti.cursor()

a.execute('''INSERT INTO alarmuygulaması(saat,dakika,saniye,açıklama) VALUES ('12','13','15','bugun ders var')''')
baglanti.commit()
baglanti.close()





import winsound
from tkinter import font as tkfont
from tkinter import *
from tkinter import messagebox
import time
import datetime
import math




#import localtime

root = Tk()
root.geometry("640x480")
root.frame = Frame(root)
root.frame.pack(fill = "both")
label = Label(root, text= "Welcome", bg = "green", fg = "white", font=("Times", 100))
label.pack(side= "top", fill = "both", expand = 1)
root.title_font = tkfont.Font(family = "Times", size = 100, weight = "bold", slant = "italic")
root.title("Clock")


def alarm():
    şimdikizaman = tick()
    wake_entry = Entry(root)
    wake_entry.pack()
    wake_entry_button = Button(root, text="Set Alarm",bg='Blue')
    wake_entry_button.pack(side = BOTTOM)
    wake = wake_entry.get()
    wake = time.strftime("%I:%M:S")
    
    #girilen textleri saat dakika ve saniye değerine atama

etiket=Label(text='Saat değerini girin',bg='green')
saat=Entry(root)

etiket.pack()


frame1 = Frame(padx=20,pady=20)
frame1.pack()

giris =Entry(width=20)
giris.pack()
etiket=Label(text='Dakika değerini girin',bg='green')

dakika=Entry(root)
etiket.pack()


frame1 = Frame(padx=20,pady=20)
frame1.pack()

giris=Entry(width=20)
giris.pack()
etiket=Label(text='Saniye değerini girin',bg='green')
saniye=Entry(root)
etiket.pack()


frame1 = Frame(padx=20,pady=20)
frame1.pack()

giris =Entry(width=20)
giris.pack()
etiket=Label(text='Açıklama',bg='green')
açıklama=Entry(root)
etiket.pack()


frame1 = Frame(padx=20,pady=20)
frame1.pack()


giris=Entry(width=20)
giris.pack()
ment = StringVar()

button_alarm = Button(text = "Alarm",bg='Blue')
button_alarm.config(command = alarm)
button_alarm.pack()

a=saat.get()
b=dakika.get()
c=saniye.get()



an = datetime.datetime.now()
time=int(an.hour)*3600+int(an.minute)*60+int(an.second)

countdown(time)
     
def countdown(count): 
    
    seconds=math.floor(fark%60)
    minutes=math.floor((fark/60)%60)
    hours=math.floor((fark/3600))
    #label['text'] ="Saat: "+ str(an.hour)+ " Dakika:  " +str(an.minute)+ " Saniye: " +str(an.second) " sonra alarm çalacak"
    label['text'] = "Saat: "+ str(hours)

    if count >= 0:
        label.after(1000, countdown,count-1)
    else:
        for x in range(3):
         winsound.Beep(1000,1000)
        label['text']="Zaman doldu!"     
      
        ment=StringVar()    


def tick(time1 = ""):

    time2 = time.strftime("%I:%M:%S")
    if time2 != time1:
        time1 = time2
        label.config(text = time1)
    label.after(500, tick)
    return time1

tick()
root.mainloop()
