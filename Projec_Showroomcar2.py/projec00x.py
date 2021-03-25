#โปรเจค โปรแกรมโชว์รูมรถมือสอง
import sqlite3
import datetime
from os import system,name
import datetime
da = datetime.date.today()
Ttime= str(da)
conn = sqlite3.connect(r'D:\Atchariya_python\Projec_Showroomcar2.py\projec00x.db')
c = conn.cursor()
# สร้างข้อมูลใน DB
# c.execute('''CREATE TABLE salename (NO integer PRIMARY KEY AUTOINCREMENT,
#     sname varchar(100) NOT NULL,
#     Ttime  varchar(100) NOT NULL,
#     scar varchar(100) NOT NULL,
#     Sellto varchar(100) NOT NULL,
#     Commission varchar(100) NOT NULL,
#     Carcolor varchar(100) NOT NULL, 
#     condition varchar(100) NOT NULL, 
#     Registration varchar(100) NOT NULL,
#     Mileage varchar(100) NOT NULL, 
#     price varchar(100) NOT NULL)''') 
# c.execute('''CREATE TABLE showcar (NO integer PRIMARY KEY AUTOINCREMENT,
#     Carname varchar(100) NOT NULL,
#     Carbrand varchar(100) NOT NULL,
#     Cartype varchar(100) NOT NULL,
#     Carcolor varchar(100) NOT NULL,
#     condition varchar(100) NOT NULL,
#     Registration varchar(100) NOT NULL,
#     Mileage varchar(100) NOT NULL,
#     price varchar(100) NOT NULL)''')
conn.commit()
conn.close()
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def menu(): #เป็นฟังชันก์เมนู กำหนดตัวแปล menu ขึ้นมา
    global choice
    print('🚗'*5,'🚘'*5,'เบนซ์วงแสวงคาร์','🚘'*5,'🚗'*5)
    print('============ ข้อมูลรถในโชว์รูม ============')
    print('🟢 แสดงรายการรถยนต์ทั้งหมดในโชว์รูม  [1]') 
    print('✅ เพิ่มรายการรถยนต์               [2]')
    print('🔧 แก้ไขข้อมูลรถยนต์                [3]')
    print('⛔ รถที่คุณต้องการซื้อ                [4]')
    print('========== ข้อมูลการซื้อ-ขายรถยนต์ ==========')
    print('🟩 แสดงข้อมูลการขายรถ             [5]')
    print('📵 ออกจากระบบ                   [0]')
    choice = input('เลือกทำรายการ : ')

def names01(): #1 เป็น def ที่ใช้สำหรับรับค่าที่ต้องการจะเพิ่มข้อมูลลงใน DB
    global Carname,Carbrand,Cartype,Carcolor,condition,Registration,Mileage,price
    Carname = input('ชื่อรถ :\t')
    Carbrand = input('ยี่ห้อรถ :\t')
    Cartype = input ('ประเภทรถ :\t')
    Carcolor = input('สีรถ :\t')
    condition = input('สภาพ :\t')
    Registration = input('ทะเบียนรถยนต์ :\t')
    Mileage = input('เลขไมล์ :\t')
    price = input('ราคารถ :\t')

def insert_showcar (Carname,Carbrand,Cartype,Carcolor,condition,Registration,Mileage,price) : #1 นำข้อมูลลงบน DB
    try :
        conn = sqlite3.connect (r'D:\Atchariya_python\Projec_Showroomcar2.py\projec00x.db')
        c = conn.cursor()
        sql = '''INSERT INTO showcar (Carname,Carbrand,Cartype,Carcolor,condition,Registration,Mileage,price) VALUES (?,?,?,?,?,?,?,?)'''
        data = (Carname,Carbrand,Cartype,Carcolor,condition,Registration,Mileage,price,)
        c.execute(sql,data)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print('Failed to insert : ',e)
    finally :
        if conn :
            conn.close ()


def show_showcar():#1 showtable showcar
    conn = sqlite3.connect (r'D:\Atchariya_python\Projec_Showroomcar2.py\projec00x.db')
    c = conn.cursor()
    print(' '*65,' ****** โชว์รูมรถยนต์ ******')
    print('-'*161)
    print('{0:<10}{1:<30}{2:<25}{3:<25}{4:<18}{5:<16}{6:<23}{7:<14}{8}'.format('ลำดับ','ชื่อรถยนต์','ยี้ห้อรถยนต์','ประเภทรถยนต์','สีรถยนต์','สภาพรถยนต์','ทะเบียนรถยนต์','เลขไมล์','ราคา'))
    print('-'*161)
    result = '''SELECT * from showcar '''
    for x in c.execute(result) :
        print('{0:<9}{1:<27}{2:<21}{3:<24}{4:<16}{5:<15}{6:<21}{7:<13}{8}'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]))

def min():# คัดลอกข้อมูลจาก DB Showcar ตามแถวที่กำหนด
    global dataman,Number,sname,Ttime,scar,Sellto,Commission,Carcolor,condition,Registration,Mileage,price
    Number = input('เลื่อกรถที่คุณจะซื้อ : ')
    conn = sqlite3.connect(r'D:\Atchariya_python\Projec_Showroomcar2.py\projec00x.db')
    data = conn.cursor()
    data.execute(""" SELECT * FROM showcar WHERE NO = ?  """,Number)
    dataman = data.fetchall()
    sname =  input(" ชื่อคนขาย : ")
    Sellto = str(input("ขายให้ : "))
    Commission = "10,000"
    aa= dataman[0][0]
    bb= dataman[0][1]
    cc= dataman[0][2]
    dd= dataman[0][3]
    ee= dataman[0][4]
    ff= dataman[0][5]
    gg= dataman[0][6]
    hh= dataman[0][7]
    ii= dataman[0][8]
    scar = bb
    Carcolor = ee
    condition = ff
    Registration = gg
    Mileage = hh 
    price = ii
    conn.commit()
    conn.close()
    
def insert_salename (sname,Ttime,scar,Sellto,Commission,Carcolor,condition,Registration,Mileage,price) : #2 นำข้อมูลลงบน DB
    try :
        conn = sqlite3.connect (r'D:\Atchariya_python\Projec_Showroomcar2.py\projec00x.db')
        c = conn.cursor()
        sql = '''INSERT INTO  salename (sname,Ttime,scar,Sellto,Commission,Carcolor,condition,Registration,Mileage,price) VALUES (?,?,?,?,?,?,?,?,?,?)'''
        data = (sname,Ttime,scar,Sellto,Commission,Carcolor,condition,Registration,Mileage,price)
        c.execute(sql,data)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print('Failed to insert : ',e)
    finally :
        if conn :
            conn.close ()


def delete():#1 ฟังก์ชันลบ
    conn = sqlite3.connect(r'D:\Atchariya_python\Projec_Showroomcar2.py\projec00x.db')
    c = conn.cursor()
    c.execute('''DELETE FROM showcar WHERE NO = ?''',Number)
    conn.commit()
    conn.close()

T= datetime.datetime.today()
Ttime= str(T.time())


def show_salename():#2 showstable datapay
    print(' '*50,' ****** ข้อมูลการซื้อขาย ******')
    conn = sqlite3.connect (r'D:\Atchariya_python\Projec_Showroomcar2.py\projec00x.db')
    c = conn.cursor()
    print('-'*167)
    print('{0:<9}{1:<25}{2:<25}{3:<25}{4:<18}{5:<16}{6:<12}{7:<10}{8:<16}{9:<10}{10}'.format('ลำดับ','ชื่อsale','เวลา','ชื่อรถ','ขายให้','commissions','สีรถ','สภาพ','เลขทะเบียนรถ','เลขไมค์','ราคารถ'))
    print('-'*167)
    show1 = '''SELECT * from salename '''
    for x in c.execute(show1):
        print('{0:<8}{1:<23}{2:<25}{3:<23}{4:<17}{5:<16}{6:<11}{7:<10}{8:<15}{9:<9}{10}'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10]))


def Edit():#1 ฟังก์ชันแก้ไข showcars
    minn = int(input('ใส่หมายเลขที่ต้องการแก้ไข : '))
    names01()
    conn = sqlite3.connect (r'D:\Atchariya_python\Projec_Showroomcar2.py\projec00x.db')
    c = conn.cursor()
    update_data = (Carname,Carbrand,Cartype,Carcolor,condition,Registration,Mileage,price,minn)
    c.execute ('''UPDATE showcar SET Carname = ?,Carbrand = ?,Cartype =?,Carcolor = ?,condition = ?,Registration = ?,Mileage = ?,price =? WHERE NO = ?''',update_data)
    conn.commit()
    conn.close()

while True:
    menu()
    try:
        if choice == '1': # แสดง
            show_showcar()
        elif choice == '2':# เพิ่ม
            names01()
            insert_showcar(Carname,Carbrand,Cartype,Carcolor,condition,Registration,Mileage,price)
        elif choice == '3':#แก้ไข
            Edit()
        elif choice == '4':# เลือกรถ
            min()
            insert_salename (sname,Ttime,scar,Sellto,Commission,Carcolor,condition,Registration,Mileage,price)
            delete()
        elif choice == '5':# แสดงรถที่เลือก
            show_salename()
        elif choice == '0': # ปิดโปรแกรม
            print('ออกจากโปรแกรม ')
            Exitt = str(input('ต้องการออกจากโปรแกรมหรือไม่ y/n :'))
            if Exitt == 'y' or Exitt == 'Y':
                clear()
                break
        else:
            print('กรุณาใส่หมายเลขให้ถูกต้อง')
    except:
        print('กรุณาใส่หมายเลขให้ถูกต้อง')