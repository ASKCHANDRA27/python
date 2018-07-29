value=eval(input('enter the value:'))
print(end=' ')
for row in range(1,value+1):
    print(end='   %2i' %row)
print()
print(end=' +')

print()
for row in range(1, value+1):
    print(end='-----')
print()
for row in  range(1,value+1):
    print(end=' %2i' %row)
    print(end='  ')
    for column in range(1,11):
        product=row*column
        print(end='%3i ' %product)
    print()