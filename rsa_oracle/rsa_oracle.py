from pwn import *

#context.log_level='critical'
p = remote("titan.picoctf.net", 52567)

p.recvuntil(b"decrypt.")

with open("password.enc") as file:
    c = int(file.read())

p.sendline(b"E")
p.recvuntil(b"keysize): ")
p.sendline(b"\x02")
p.recvuntil(b"mod n) ")

c_a = int(p.recvline())

p.sendline(b"D")
p.recvuntil(b"decrypt: ")
p.sendline(str(c_a*c).encode())
p.recvuntil(b"mod n): ")

password = int(p.recvline(), 16) // 2 # đổi từ hex về int
length = (password.bit_length() + 7) // 8 # ép thêm 7 bit để tính đc số byte đủ
password = password.to_bytes(length, "big").decode("utf-8")
# ép về dãy byte kiểu big_endian và giải thành txt utd-8

print("Password:", password)