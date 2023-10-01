import base64
from ocflzw_decompress.lzw import LzwDecompress

# bin = ""
with open('binary.bin', 'rb') as file:
    bin = file.read()
bin = base64.b64decode(bin)

lzw = LzwDecompress()
uncomp = lzw.decompress(bin)
uncomp_text = "".join(map(chr, uncomp)).rstrip('\x00')
print(uncomp_text)