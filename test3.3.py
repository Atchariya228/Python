#แบบฝึกหัด 3.3 Control Statements
print('ป้อนชื่ออาหารสุดโปรดของคุณ หรือ exit เพื่อออกจากโปรแกรม')
food = []
i = 0
while(True) :
    i = i + 1
    print('อาหารสุดโปรอันดับที่ ',i,end='')
    choose = input(' คือ\t')
    food.append(choose)
    if( choose == 'exit') :
        break
print('อาหารสุดโปรดของคุณมีดังนี้',end=' ')
for x in range(1,i) :
    print(x,'.',food[x-1],end='    ')
