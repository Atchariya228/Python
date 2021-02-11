#แบบฝึกหัด 3.2 Loop
i = 1
a = 0
x = int(input('กรุณากรอกจำนวนครั้งการรับค่า \n'))
while(i <= x ) :
    number = int(input('กรอกตัวเลข : '))
    a+=number
    i+=1
print('ผลรวมที่รับค่าเข้ามาทั้งหมด = %d'%a)
