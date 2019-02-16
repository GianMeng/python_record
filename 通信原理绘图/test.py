import re
input_lines = input()
len_input_lines = len(input_lines)

match=True
# pattern1 = re.compile('[0-9]+')
# pattern2 = re.compile('[a-z]+')
# pattern3 = re.compile('[A-Z]+')
# match = pattern1.findall(input_lines) and pattern2.findall(input_lines) or pattern3.findall(input_lines)
for i in input_lines:
    if not(i.isalpha()) and not(i.isalnum()):
        match=False
    # if i.isspace():
    #     match=False
a=0
exit_flag=0

if len_input_lines>=6:
    # if input_lines.isalnum() == True:
    if match:
        for i in range(len_input_lines-2):
            a += 1
            # print("test")
            if input_lines[len_input_lines-a]==input_lines[len_input_lines-(a+1)]==input_lines[len_input_lines-(a+2)]:
                # print("code")
                exit_flag=1
        if exit_flag==1:
            print("invalid")
            print(0)
        else:
            print(1)
            print("valid")

    else:
        print("invalid")
        print(2)
else:
    print("invalid")
    print(3)