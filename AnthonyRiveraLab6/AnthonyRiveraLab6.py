#Anthony Rivera
#CIS-117-OLH-CRN95943
#Lab Assignment 6
#10/10/2017

p = 0
while p < 5:
    error = 0
print("Please enter the file name:")
file = raw_input()
with open(file, "r") as fin:
    for line in fin:
        totalline = line.split(" ")

try:
    n = int(totalline[0])
except ValueError:
    print('Error: file contents invalid.')
    error = 1
    p = p + 1
    #continue or pass doesn't work
length = len(totalline)
if n != length-1:
    print('Error: file invalid length')
    error = 1
    p = p + 1
    #continue or pass doesn't work =(
total = 0
for i in range(n):
    try:
        total += int(totalline[i + 1])
    except ValueError:
        print('Error: file contents invalid.')
        error = 1
        break
        if error == 0:
                print('Total is :', format(total))
p = p + 1

#i tried for 3 hours, it was running but can't open .dat files
