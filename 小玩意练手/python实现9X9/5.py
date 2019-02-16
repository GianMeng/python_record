#建立表头
print('  |', end = '')
for k in range(1,10):
   #不自动换行，只留空格符
    print('{0:3d}'.format(k), end ='')
print() #换行
print('-'* 32)

#第一重 for/in
for one in range(1,10):
    print()  # 换行
    print(one,'|',end = '')
    # 第二重 for/in
    for two in range(1,10):
        print('{0:3d}'.format(one*two),end='')

