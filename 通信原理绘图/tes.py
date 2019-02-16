import re
input_lines = input()
len_input_lines = len(input_lines)

match = True
for i in input_lines:
    if not(i.isalpha()) and not(i.isalnum()):
        match=False
a=0
exit_flag=0

if len_input_lines>=6:
    if match:
        for i in range(len_input_lines-2):
            a += 1
            if input_lines[len_input_lines-a]==input_lines[len_input_lines-(a+1)]==input_lines[len_input_lines-(a+2)]:
                exit_flag=1
        if exit_flag==1:
            print("invalid")
        else:
            print("valid")

    else:
        print("invalid")
else:
    print("invalid")