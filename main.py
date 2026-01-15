def range(number):
    i=0
    while i < number:
        yield i
        i+=1

    yield from range(number)

for i in range(700):
    print(i)
    if i == 699:
        print("0")




