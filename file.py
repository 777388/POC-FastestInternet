import sys
import time

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
#file, converted to binary for processing
f = open(sys.argv[1], "r")
y = ' '.join(format(x, 'b') for x in bytearray(f.read(), "utf-8"))
#store y as all zeroes then determine length of string
y.replace(" ", "")
waittime = len(y.replace("1", "00"))

print("calculation time " +str(waittime*.0000000000000000000000001) +" seconds")
print("file size " + str(len(y)) + " bytes")

for n in find(y, "1"):
    time.sleep(n*.0000000000000000000000001)
    
#CIA  6H9CHJ39