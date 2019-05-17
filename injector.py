import binascii
import sys
import json
args = sys.argv 

sigs = json.load(open("sigs.json","r"))

if len(args) == 2 and args[1].lower() == "list":
    for key in sigs:
        print(key)
    sys.exit(0)

if len(args) != 3:
    print(f"Usage: {args[0]} FILE FILETYPE")
    sys.exit(1)

file = args[1]
fileType = args[2].lower()

if not fileType in sigs:
    print(f"Filetype not supported. Check '{args[0]} list' for supported filetypes.")
    sys.exit(1)


toAdd = sigs[fileType]
toAddBytes = [binascii.unhexlify(x) for x in toAdd.split(" ")]

fileContents = open(file, "rb").read()

out = open(file + "." + fileType,"wb")
for b in toAddBytes:
    out.write(b)
out.write(fileContents)
out.close()
