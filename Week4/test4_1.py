#แบบฝึกหัดที่ 4.1 โปรแกรมขายของ สินค้า แสดงราคาสินค้า
'''
shop_list = []
amount = [0,0,0,0,0]
price = [100,550,255,1000,150]
def out_item() :
    n = 0
    while(True):
        print("\tสินค้าในตะกร้ามีดังนี้")
        for i in shop_list :
            n += 1
            print("\t" + str(n) + "."+i)
        n = 0
        c = int(input("เลือกลำดับสินค้าที่จะหยิบออก หรือพิมพ์ -1 เพื่อออก: "))
        try :
            if c <= len(shop_list) and c != -1 :
                shop_list.pop(c-1)
            elif c == 0 and c <= len(shop_list) and c != -1 :
                shop_list.pop(c)
            elif c == -1 :
                break
        except : 
            print("กรุณากรอกระดับสินค้าให้ถูกต้อง")
def list_item() :
    print("\tรายการสินค้า") 
    print("-"*25)
    print("\t1.เรือดำน้ำ ราคา 155 บาท")
    print("\t2.บั้งไฟ ราคา 255 บาท")
    print("\t3.รถถัง ราคา 455 บาท")
    print("\t4.เครื่องบิน ราคา 655 บาท")
    print("\t5.รถจิ๊บ ราคา 955 บาท")
def pick_item():
    c=0
    while(True):
        print("\t1.เรือดำน้ำ")
        print("\t2.บั้งไฟ")    
        print("\t3.รถ")    
        print("\t4.เครื่องบิน")    
        print("\t5.รถจิ๊บ")    
        print("\t6.ออกจากฟังก์ชั่น")
        c=(input("เลือกหยิบสินค้าหมายเลข: "))
        try:
            if int(c)==1 or c=="1":
                shop_list.append("เรือดำน้ำ")
            elif int(c)==2 or c=="2":
                shop_list.append("บั้งไฟ")
            elif int(c)==3 or c=="3":
                shop_list.append("รถถัง")     
            elif int(c)==4 or c=="4":
                shop_list.append("เครื่องบิน")     
            elif int(c)==5 or c=="5":
                shop_list.append("รถจิ๊บ")     
            elif int(c)==6 or c=="6":
                break
            else:
                print('กรุณากรอกหมายเลขให้ถูกต้อง')
        except:
            print('กรุณากรอกหมายเลขให้ถูกต้อง')
            pass
def show_item():
    for i in shop_list:
        if i == 'ยาดม':
            amount[0]+=1
        elif i == 'น้ำเปล่า':
            amount[1]+=1
        elif i == 'มาม่า':
            amount[2]+=1
        elif i == 'สบู่':
            amount[3]+=1
        elif i == 'แปรงสีฟัน':
            amount[4]+=1
    amounttt=amount[0]+amount[1]+amount[2]+amount[3]+amount[4]
    pricett=amount[0]*15+amount[1]*10+amount[2]*20+amount[3]*30+amount[4]*25
    print('')
    print('{0:_<10}{1}{0:_<10}'.format('','สินค้าที่คุณได้หยิบไปมีดังนี้'))
    print('{0:.<6}{1}{0:.<6}{0:.<6}{3}{0:.<7}'.format('','สินค้า','จำนวน','ราคา'))
    print('{0:_<38}'.format(''))
    if amount[0]!=0
        print('{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format('','ยาดม',str(amount[0],str(amount[0]*15)))
    if amount[1]!=0
        print('{0:.<4}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format('','น้ำเปล่า',str(amount[1],str(amount[1]*10)))
    if amount[2]!=0
        print('{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format('','มาม่า',str(amount[2],str(amount[2]*20)))
    if amount[3]!
        print('{0:.<6}{1}{0:.<8}{2}{0:.<9}{3}{0:.<10}'.format('','สบู่',str(amount[3],str(amount[3]*30)))
    if amouont[4]!=0:
        print('{0:.<16}{1}{0:.<9}{3}{0:.<10}'.format("","แปรงสีฟัน",str(amount[4])))
    print("{0:_<38}".format(""))
    print('{0:.<6}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format("","รวม",str(amounttt),str(pricett)))
    print("")
print("\tโปรแกรมร้านค้าออนไลน์")
print("-----------------------------------")
while(True):
    print('1. แสดงรายการสินค้า')
    print('2. หยิบสินค้าเข้าตะกร้า')
    print('3. แสดงรายจำนวนและราคาของสินค้าที่หยิบ')
    print('4. หยิบสินค้าออกจากตะกร้า')
    print('5. ปิดโปรแกรม')
    print('')
    ch=input("กรุณาเลือกทำรายการ")
    if ch =="1":
        list_item()
    elif ch=="2":
        pick_item()
    elif ch=="3":
        show_item()
    elif ch=="4":
        out_item()
    elif ch=="5":
        ch=input("ต้องการออกจากโปนแกรมใช่หรือไม่ y/n:")
        if ch == 'y':
            break
        elif ch == 'n':
            continue        except:
            print('กรุณากรอกหมายเลขให้ถูกต้อง')
            pass
def show_item():
    for i in shop_list:
        if i == 'ยาดม':
            amount[0]+=1
        elif i == 'น้ำเปล่า':
            amount[1]+=1
        elif i == 'มาม่า':
            amount[2]+=1
        elif i == 'สบู่':
            amount[3]+=1
        elif i == 'แปรงสีฟัน':
            amount[4]+=1
    amounttt=amount[0]+amount[1]+amount[2]+amount[3]+amount[4]
    pricett=amount[0]*15+amount[1]*10+amount[2]*20+amount[3]*30+amount[4]*25
    print('')
    print('{0:_<10}{1}{0:_<10}'.format('','สินค้าที่คุณได้หยิบไปมีดังนี้'))
    print('{0:.<6}{1}{0:.<6}{0:.<6}{3}{0:.<7}'.format('','สินค้า','จำนวน','ราคา'))
    print('{0:_<38}'.format(''))
    if amount[0]!=0
        print('{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format('','ยาดม',str(amount[0],str(amount[0]*15)))
    if amount[1]!=0
        print('{0:.<4}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format('','น้ำเปล่า',str(amount[1],str(amount[1]*10)))
    if amount[2]!=0
        print('{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format('','มาม่า',str(amount[2],str(amount[2]*20)))
    if amount[3]!
        print('{0:.<6}{1}{0:.<8}{2}{0:.<9}{3}{0:.<10}'.format('','สบู่',str(amount[3],str(amount[3]*30)))
    if amouont[4]!=0:
        print('{0:.<16}{1}{0:.<9}{3}{0:.<10}'.format("","แปรงสีฟัน",str(amount[4])))
    print("{0:_<38}".format(""))
    print('{0:.<6}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format("","รวม",str(amounttt),str(pricett)))
    print("")
print("\tโปรแกรมร้านค้าออนไลน์")
print("-----------------------------------")
while(True):
    print('1. แสดงรายการสินค้า')
    print('2. หยิบสินค้าเข้าตะกร้า')
    print('3. แสดงรายจำนวนและราคาของสินค้าที่หยิบ')
    print('4. หยิบสินค้าออกจากตะกร้า')
    print('5. ปิดโปรแกรม')
    print('')
    ch=input("กรุณาเลือกทำรายการ")
    if ch =="1":
        list_item()
    elif ch=="2":
        pick_item()
    elif ch=="3":
        show_item()
    elif ch=="4":
        out_item()
    elif ch=="5":
        ch=input("ต้องการออกจากโปนแกรมใช่หรือไม่ y/n:")
        if ch == 'y':
            break
        elif ch == 'n':
            continue  

'''
#4.1 วิธีที่ 2
import os
choice = 0
listcoffee = [0,0,0,0,0,]
pick = 0
def menu():
    global choice
    print('\tโปรแกรมสินค้าอัจฉริยะ IT\n','1.แสดงรายการสินค้า\n 2.หยิบสินค้าเข้าตะกร้า\n 3.แสดงรายจำนวนและราคาของสินค้าที่หยิบ\n 4.หยิบสินค้าออกจากตะกร้า\n 5.ปิดโปรแกรม')
    choice = input('กรุณาเลือกทำรายการ : ')
    screen_clear()

def showmenu(): 
    print('\tรายการสินค้า IT')
    print('\t1.เมาส์ 990 บาท\n','\t2.แป้นพิมพ์ 3490 บาท\n','\t3.จอเเสดงผล 5900 บาท\n','\t4.หูฟัง 2980 บาท\n','\t5.ไมคโครโฟน 750 บาท')

def pickmenu():
    global pick
    print('\tรายการสินค้า\n 1.เมาส์\n 2.แป้นพิมพ์\n 3.จอแสดงผล\n 4.หูฟัง\n 5.ไมคโครโฟน')
    pick = int(input('เลือกหยิบสินค้าหมายเลข :'))
    if pick == 1:
        listcoffee[0] += 1
    elif pick == 2:
        listcoffee[1] += 1
    elif pick == 3:
        listcoffee[2] += 1
    elif pick == 4:
        listcoffee[3] += 1
    elif pick == 5:
        listcoffee[4] += 1
    screen_clear()

def showuserpick():
    list_score = ['เมาส์','แป้นพิมพ์','จอแสดงผล','หูฟัง','ไมคโครโฟน']
    list_price = [990,3490,5900,2980,750]
    print('{0:-<13}{1:-<13}{2:-<13}{3}'.format('สินค้า','ราคา','จำนวน','ราคารวม'))
    for i in range(0,5):
        print('{0:-<13}{1:-<13}{2:-<13}{3}'.format(list_score[i],list_price[i],listcoffee[i],listcoffee[i]*list_price[i]))

def deletuserpick():
    print('\t\nรายการสินค้า\n 1.เมาส์\n 2.แป้นพิมพ์\n 3.จอแสดงผล\n 4.หูฟัง\n 5.ไมคโครโฟน')
    depick = int(input('เลือกลำดับสินค้าที่จะหยิบออก หรือพิมพ์ -1 เพื่อออก'))
    if depick == 1:
        listcoffee[0] -= 1
    elif depick == 2:
        listcoffee[1] -= 1
    elif depick == 3:
        listcoffee[2] -= 1
    elif depick == 4:
        listcoffee[3] -= 1
    elif depick == 5:
        listcoffee[4] -= 1

def screen_clear():
    clearscreen = os.system('cls')

while True:
    menu()
    if choice == '1':
        screen_clear()
        showmenu()
    elif choice == '2':
        screen_clear()
        pickmenu()
    elif choice == '3':
        screen_clear()
        showuserpick()
    elif choice == '4':
        deletuserpick()
        screen_clear()
    elif choice == '5':
        c = input('ต้องการใช้โปรแกรมต่อหรือไม่ y/n: ')
        if c.lower() == 'y':
            screen_clear()
        elif c.lower() == 'n':
            screen_clear()
            break