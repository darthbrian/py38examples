
while (inrange := input("Enter a value range: ")) != 'quit':
    output = [(square:=x**2, square + 1) for x in range(int(inrange))]
    print(output)

