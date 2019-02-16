# import re
# n=input()#行数
# print(n.isalpha())
# print(n[len(n)-1])
# print(''.join([s for s in n if s.isalpha()]))
# for j in range(ord(n)):
#     input_lines = input()
# print(input_lines)
    # for each in input_lines[j]:
    #     print('test')

n=ord(input("输入行数:\n"))

stopword = ''
str_line = ''
for line in iter(input, stopword):
    str_line += line + '\n'
a = str_line.split("\n")
for i in range(len(a)):
    # print(a[i].isalpha())
    # print(''.join([s for s in a[i] if s.isalpha()]))
    # print(''.join([s for s in a[i] if s.isalnum()]))
    # print (a[i] + ": " + str(i+1))
    num=''.join([s for s in a[i] if s.isdigit()])
    name=''.join([s for s in a[i] if s.isalpha()])
    # print(num)
    if num=='3':
        print(name)
    # print(''.join([s for s in a[i] if s.isdigit()]))


#
# line = """qqq
# sss
# fff"""
# a = line.split("\n")
# for i in range(len(a)):
#     print (a[i] + ": " + str(i))

# a=input().lower()
# b=input().lower()
# print(a.count(b))

# input_lines = input()
# print(input_lines[0::2])