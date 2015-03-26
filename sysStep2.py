f_res=open('result.res','rb')
for line in f_res.readlines():
    data=line.strip().split()

f_res.close()
if float(data[4])>-1.2:
    print "he is a non native speakeryy"
else :
    print "he is a native speakeryy"
