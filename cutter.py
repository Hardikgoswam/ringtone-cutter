# Mp3 & Mp4 cutter (Ringtone cutter) program by using _PYTHON_ programming :

InputFile = input("Please Enter File Name: ")
f = open(InputFile,"rb")  # open connection current input file 
no_parts = int(input("Enter The Number of parts:"))
# for _ in range(no_parts):
print("Enter the {} file name: ".format(no_parts))
i = 0
filenames = []
while i != no_parts:
    x = input("Enter {} file name :".format(i+1))+".mp3" 
    filenames.append(x)
    i += 1
# print(filenames)
Inputdata = f.read()
part_len = len(Inputdata)
seek_number = part_len//no_parts
f.seek(0)
for list in filenames:
    data = f.read(seek_number)
    f1 = open(list,"wb")
    f1.write(data)
    f1.close()
# print(data)
f.close()
print("Number of {} File creates SUCCESSFULLY".format(no_parts))