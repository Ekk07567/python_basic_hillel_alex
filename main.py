a = int(input('Number 1:'))
b = int(input('Number 2:'))
c = int(input('Number 3:'))
if a > 10 and b > 10 and c > 10 and a % 3 == 0 and b % 3 == 0:
    print('yes')
else:
    print('no')


print(max(a,b,c))

a = input('Введите трехзначное число:')
print(int(a[::-1]))