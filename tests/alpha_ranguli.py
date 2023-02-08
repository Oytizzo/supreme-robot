def print_rangoli(size):
    # your code goes here
    # length of the rangoli is 2*size - 1
    # width of rangoli is 2*((2*size)-1) -1
    # 2(2n-1)-1
    # 4n -3
    # width is (4*size - 1)
    length = 2*size - 1
    width = 4*size - 3
    for i in range(length):
        # loop through the full length
        num = i
        if i > length//2:
            num = (length-1) - i
        ch = chr(ord('a') + length//2)

        if num == 0:
            print(ch.center(width, '-'))
        else:
            # print("hello")
            ch_list = []
            j = 0
            for j in range(num+1):
                ch_list.append(chr(ord(ch)-j))
            j -= 1
            while j >= 0:
                ch_list.append(chr(ord(ch)-j))
                j -= 1
            print('-'.join(ch_list).center(width, '-'))

print(print_rangoli(24))
