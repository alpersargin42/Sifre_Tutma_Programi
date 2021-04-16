from tkinter import *
import os
from shutil import copyfile
import sqlite3
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog

Profile = {1:""}

def ana_ekran():
    global ana_ekran
    ana_ekran = Tk()
    ana_ekran.geometry("600x600")
    ana_ekran.title("Hesaplarınızı Koruyun")
    Label(ana_ekran,text="Hesaplarınızı görmek için giriş yapınız." ,font=("Calibri", 11)).pack()
    Button(ana_ekran,text="Giriş Yap",height="2",bg="Red", width="30",command=giris).pack()
    if session_control()==False:
        Button(ana_ekran, text="Kayıt", height="2", bg="Red", width="30",command=kayit).pack()

    ana_ekran.mainloop()
######################################################################
def kayit():
    global kayit_ekrani
    kayit_ekrani=Toplevel(ana_ekran)
    kayit_ekrani.title("Kayıt Ekranı")
    kayit_ekrani.geometry("600x600")


    global kullanici_adi
    global sifre
    global kullanici_adi_giris
    global sifre_giris
    kullanici_adi = StringVar()
    sifre = StringVar()

    Label(kayit_ekrani,text="Lütfen Kullanıcı Adı ve Şifre Belirleyiniz").pack()
    kullanici_adi_lable=Label(kayit_ekrani,text="Kullanıcı Adı *").pack()
    kullanici_adi_giris=Entry(kayit_ekrani,textvariable=kullanici_adi).pack()
    sifre_lable=Label(kayit_ekrani,text="Şifre *").pack()
    sifre_giris= Entry(kayit_ekrani,textvariable=sifre,show="*").pack()
    Button(kayit_ekrani,text="Kayıt Ol",width=10,height=1,bg="yellow",command=kayit_olma).pack()

def kayit_olma():
    kullanici_adi_bilgisi= kullanici_adi.get()
    sifre_bilgisi= sifre.get()

    file=open("kullanici","w")
    file.write(kullanici_adi_bilgisi+"\n")
    file.write(sifre_bilgisi)
    file.close()

    Label(kayit_ekrani,text="Kayıt Başarılı").pack()
########################################################################
def giris():
    global giris_ekrani
    giris_ekrani=Toplevel(ana_ekran)
    giris_ekrani.title("Giriş Ekranı")
    giris_ekrani.geometry("600x600")
    Label(giris_ekrani,text="Lütfen Bilgilerinizi giriniz.").pack()

    global kullanici_adi_bilgisi
    global sifre_bilgisi

    kullanici_adi_bilgisi = StringVar()
    sifre_bilgisi = StringVar()

    global kullanici_giris_ekrani_g
    global sifre_giris_ekrani_g

    Label(giris_ekrani,text="Kullanıcı Adı * ").pack()
    kullanici_giris_ekrani_g = Entry(giris_ekrani,textvariable=kullanici_adi_bilgisi).pack()
    Label(giris_ekrani,text="Şifre * ").pack()
    sifre_giris_ekrani_g = Entry(giris_ekrani,textvariable = sifre_bilgisi,show="*").pack()
    Button(giris_ekrani,text="Giriş Yap",bg="Yellow",width=10,height=1,command=giris_bilgisi).pack()

def giris_bilgisi():
    kullanici_adi= kullanici_adi_bilgisi.get()
    sifre = sifre_bilgisi.get()

    dosya_listesi=os.listdir()
    if "kullanici" in dosya_listesi:
        file=open("kullanici","r")
        bilgi=file.read().splitlines()
        if sifre in bilgi:
            #Label(giris_ekrani,text="Giriş Başarılı",fg="green").pack()
            giris_basarili()
        else:
            Label(giris_ekrani, text="Şifre Hatalıdır.", fg="red").pack()
    else:
        Label(giris_ekrani, text="Kullanıcı Bulunamadı", fg="red").pack()

def session_control():
    dosya_listesi = os.listdir()
    if "kullanici" in dosya_listesi:
        return True

    else:
        return False

def giris_basarili():
    global giris_basarili
    giris_ekrani.destroy()
    giris_basarili=Tk()
    giris_basarili.title("Giriş Başarılı")
    giris_basarili.geometry("300x300")
    Label(giris_basarili,text="Giriş Başarılı").pack()
    Button(giris_basarili,text="Tamam",bg="green",command=secim_ekrani).pack()

    giris_basarili.mainloop()

def secim_ekrani():
    global secim_ekrani
    giris_basarili.destroy()
    secim_ekrani=Tk()
    secim_ekrani.title("Seçim Ekranı")
    secim_ekrani.geometry("600x600")
    Label(secim_ekrani,text="Lütfen Seçim yapınız.").pack()
    Button(secim_ekrani,text="Hesap Ekle",bg="turquoise",height="10",width="50",command=Hesap_ekle).pack()
    Button(secim_ekrani, text="Hesap Görüntüle",bg="turquoise",height="10",width="50",command=Hesap_goruntule).pack()

    secim_ekrani.mainloop()
def Hesap_ekle():
    global hesap_ekle
    secim_ekrani.destroy()
    hesap_ekle = Tk()
    hesap_ekle.title("HESAP EKLE")
    hesap_ekle.geometry("900x650")

    uygulama = Frame(hesap_ekle)
    uygulama.grid()

    def hesapp_ekle():
        kullanici_adi = entryKullanici_adi.get()
        sifre = entrySifre.get()

        # Create connection
        conn = sqlite3.connect('sifre_tut.db')
        cur = conn.cursor()
        # Insert data
        cur.execute('''INSERT INTO sifre_tut (`kullanici_adi` , `sifre`) VALUES (?,?)''', (kullanici_adi, sifre))
        # commit connection
        conn.commit()
        conn = sqlite3.connect('sifre_tut.db')
        cur = conn.cursor()
        select = cur.execute("SELECT*FROM sifre_tut order by id desc")
        select = list(select)

        conn.close()

    lblName = Label(hesap_ekle, text="Kullanıcı Adınız:",fg="white",bg="gray")
    lblName.place(x=5, y=50, width=155)
    entryKullanici_adi = Entry(hesap_ekle)
    entryKullanici_adi.place(x=170, y=50, width=380)

    lblSifre = Label(hesap_ekle, text="Şifre :",fg="white",bg="gray")
    lblSifre.place(x=5, y=80, width=155)
    entrySifre = Entry(hesap_ekle)
    entrySifre.place(x=170, y=80, width=380)

    bAdd = Button(hesap_ekle, text="Kullanıcı Ekle",fg="black",bg="lightblue", command=hesapp_ekle)
    bAdd.place(x=450, y=120, width=155)

    bHesap = Button(hesap_ekle, text="Hesap Görüntüle", fg="black",bg="lightblue", command=Hesap_goruntule)
    bHesap.place(x=450, y=150, width=155)


    hesap_ekle.mainloop()

def Hesap_goruntule():
    global hesap_goruntule
    hesap_goruntule=Tk()
    hesap_goruntule.title("Hesaplarınız")
    hesap_goruntule.geometry("950x600")


    def hesapp_sil():
        idSelect = tree.item(tree.selection())['values'][0]
        conn = sqlite3.connect("sifre_tut.db")
        cur = conn.cursor()
        delete = cur.execute("delete from sifre_tut where id = {}".format(idSelect))
        conn.commit()
        conn.close()
        tree.delete(tree.selection())

    bSil = Button(hesap_goruntule, text="Hesap Sil", fg="black", bg="lightblue", command=hesapp_sil)
    bSil.place(x=5, y=205, width=155)

    def treeActionSelect(event):

        idSelect = tree.item(tree.selection())['values'][0]
        kullanici_adiSelect = tree.item(tree.selection())['values'][1]
        sifreSelect = tree.item(tree.selection())['values'][2]

        lid = Label(hesap_goruntule, text="  ID : " + str(idSelect))
        lid.place(x=110, y=350, width=150)
        lkullanici_adi = Label(hesap_goruntule, text=" Kullanıcı Adı: " + kullanici_adiSelect)
        lkullanici_adi.place(x=110, y=380, width=150)
        lsifre = Label(hesap_goruntule, text=" Şifre : " + str(sifreSelect))
        lsifre.place(x=110, y=410, width=150)

    # Add Treeview
    tree = ttk.Treeview(hesap_goruntule, columns=(1, 2, 3), height=5, show="headings")
    tree.place(x=170, y=170, width=400, height=175)
    tree.bind("<<TreeviewSelect>>", treeActionSelect)
    # Add scrollbar
    vsb = ttk.Scrollbar(hesap_goruntule, orient="vertical", command=tree.yview)
    vsb.place(x=530, y=200, height=120)
    tree.configure(yscrollcommand=vsb.set)

    # Add headings
    tree.heading(1, text="ID")
    tree.heading(2, text="Kullanıcı Adı")
    tree.heading(3, text="Sifre")
    # Define column width
    tree.column(1, width=100)
    tree.column(2, width=100)
    tree.column(3, width=100)
    # Display data in treeview object
    conn = sqlite3.connect('sifre_tut.db')
    cur = conn.cursor()
    select = cur.execute("select*from sifre_tut")
    for row in select:
        tree.insert('', END, values=row)


    hesap_goruntule.mainloop()

ana_ekran()