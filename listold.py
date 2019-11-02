
inrange = input("Enter a value range: ")
while inrange != 'quit':
    output = [(x**2, x**2 + 1) for x in range(int(inrange))]
    print(output)
    inrange = input("Enter a value range: ")
