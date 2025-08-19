from math import prod
import gmpy2
import socket, json

def crt(Cipher, arrN):
    N = prod(arrN)
    x = 0
    for ci,ni in zip(Cipher, arrN):
        Ni = N // ni
        inv = pow(Ni, -1, ni) 
        x += ci*Ni*inv
    x = x % N
    return x

HOST = "94.237.61.242"
PORT = 53983
Cipher = []
arrN = []

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    for _ in range (0,5):
        data = s.recv(4096).decode()
        s.sendall(b"Y")
        data = s.recv(4096).decode().strip()
        capsule = json.loads(data)
        c = int(capsule["time_capsule"], 16)
        n = int(capsule["pubkey"][0], 16)
        Cipher.append(c)
        arrN.append(n)
        

x = crt(Cipher, arrN)
res, ex = gmpy2.iroot(x, 5)
res = int(res)
flag = res.to_bytes((res.bit_length()+7)//8, "big")
print(flag.decode())