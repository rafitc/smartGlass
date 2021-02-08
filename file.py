#open and read the file after the appending:
f = open("log/upload.txt", "r")
print(f.read())
count = f.read()
print(count)
print(type(count))
print(int(float(count)))
if(count == '5'):
    print("fullllll")
else:
    print("not")

f = open("log/upload.txt", "w")
f.write(count)
f.close()