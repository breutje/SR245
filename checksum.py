import struct
import zlib
import sys
import os

rom = sys.argv[1]

if not os.path.exists(rom):
    print(f"Error: {rom} does not exists")
    exit(0)
    
data = open(rom, "rb").read()

# 1. Standard 16-bit byte sum (Data I/O, Minato, XGecu, etc.)
sum16 = sum(data) & 0xFFFF

# 2. 16-bit big-endian word sum
words_be = struct.unpack(f">{len(data)//2}H", data)
wsum_be = sum(words_be) & 0xFFFF

# 3. 16-bit little-endian word sum
words_le = struct.unpack(f"<{len(data)//2}H", data)
wsum_le = sum(words_le) & 0xFFFF

print(f"Byte SUM16 : {sum16:04X}")
print(f"Word BE    : {wsum_be:04X}")
print(f"Word LE    : {wsum_le:04X}")
print(f"Negated    : {(-sum16) & 0xFFFF:04X}")