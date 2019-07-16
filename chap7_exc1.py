fhand = open('small_txtfile.txt', 'r')

for line in fhand:
    print_line = line
    print(print_line.rstrip().upper())
