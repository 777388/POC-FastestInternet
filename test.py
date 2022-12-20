import sys
import time

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
#string, converted to binary for processing
st = sys.argv[1]
y = ' '.join(format(x, 'b') for x in bytearray(st, 'utf-8'))
#store y as all zeroes then determine length of string
y.replace(" ", "")
waittime = len(y.replace("1", "00"))

print("calculation time " +str(waittime*.0000000000000000000000001) +" seconds")
print("data sent" + y)

for n in find(y, "1"):
    time.sleep(n*.0000000000000000000000001)