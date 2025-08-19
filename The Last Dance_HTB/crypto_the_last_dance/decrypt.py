def hex_xor(hex1: str, hex2: str) -> str:
    if len(hex1) % 2 != 0:
        hex1 = '0' + hex1
    if len(hex2) % 2 != 0:
        hex2 = '0' + hex2

    b1 = bytes.fromhex(hex1)
    b2 = bytes.fromhex(hex2)

    min_len = min(len(b1), len(b2))
    out = bytearray()
    for i in range(0, min_len) :
        rs = b1[i] ^ b2[i]
        out.append(rs)
    return out.hex()
    
cipher_plain = b"Our counter agencies have intercepted your messages and a lot of your agent's identities have been exposed. In a matter of days all of them will be captured"
cipher_plain_hex = cipher_plain.hex()


cipher_en = '7aa34395a258f5893e3db1822139b8c1f04cfab9d757b9b9cca57e1df33d093f07c7f06e06bb6293676f9060a838ea138b6bc9f20b08afeb73120506e2ce7b9b9dcd9e4a421584cfaba2481132dfbdf4216e98e3facec9ba199ca3a97641e9ca9782868d0222a1d7c0d3119b867edaf2e72e2a6f7d344df39a14edc39cb6f960944ddac2aaef324827c36cba67dcb76b22119b43881a3f1262752990'


key_stream = hex_xor(cipher_plain_hex, cipher_en)
# print(key_stream)
flag_en = '7d8273ceb459e4d4386df4e32e1aecc1aa7aaafda50cb982f6c62623cf6b29693d86b15457aa76ac7e2eef6cf814ae3a8d39c7'
flag_plain = hex_xor(flag_en, key_stream)
flag_byte = bytes.fromhex(flag_plain)

print(flag_byte)

print(bytes.fromhex('c4a66edfe80227b4fa24d431'))