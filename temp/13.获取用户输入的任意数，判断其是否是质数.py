num = int(input('请输入任意一个大于1的整数：'))
i = 2
flag = True
while i < num:
    if num % i == 0:
        flag = False
    i += 1
if flag:
    print(f'{num}是质数')
else:
    print(f'{num}不是质数')
