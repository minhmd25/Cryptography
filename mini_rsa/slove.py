import gmpy2

n = int(input())

e = 3

c = int(input())

for i in range(10000):
    m, check = gmpy2.iroot(i*n + c, e)
    if check:
        print(i)
        length = (m.bit_length() + 7) // 8 # xử lí padding
        plaintext = m.to_bytes(length, "big").decode("utf-8")
        print(plaintext)
        break
    else:
        print(i)
        

        