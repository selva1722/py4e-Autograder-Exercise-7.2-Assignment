fname = input("Enter file name: ")
fh = open(fname)
temp=0
count=0
total=0
avg=0
for line in fh:
    if not line.startswith ("X-DSPAM-Confidence:") : 
        continue
    x= line.find('0')
    y =line[x:]
    temp= float(y)
    # print(temp)- for debug purpose
    total= total+ temp
    count= count + 1
avg=total/count
print('Average spam confidence:', avg)
