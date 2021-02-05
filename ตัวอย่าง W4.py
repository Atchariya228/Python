#ตัวอย่างเปิดโปรแกรม จากไฟล์(Notepad&Calculator)
'''
import os 
choice = 0
filename = '' 
def menu(): 
    global choice 
    print('Menu\n 1.0pen Calculator\n 2.0pen Notepad\n 3.Exit ')
    choice = input('Select Menu :')  
    
def opennotepad(): 
    filename = 'C:\\Windows\\SysWOW64\\notepad.exe'
    print('Memorandum writing %s' %filename)
    os.system(filename)

def opencalculator():
    filename = 'C:\\Windows\\SysWOW64\\calc.exe'
    print('Calculate Number %s' %filename) 
    os. system(filename) 

while True: 
    menu()
    if choice == '1': 
        opencalculator() 
    elif choice == '2': 
        opennotepad()
    else: 
        break
'''

#ตัวอย่าง Keyword Argument Function
'''
def Introduce(arg1, arg2 = 'com' , arg3 = 'ed' , arg4 = 'kku' ) :
    print('Hello, I am '+arg1+', '+arg2+' '+arg3+' '+arg4)

Introduce('Python')
Introduce(arg1 = 'Python')
Introduce(arg1 = 'Python' , arg3 = 'Sci')
Introduce('Python', arg4 = 'CMU')
'''

