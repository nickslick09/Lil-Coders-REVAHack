file_object = open('currentuserdetails.txt', 'r')
Lines = file_object.readlines() 
x=[]
for line in Lines:
    y=line.split()
    x.append(y)
uname=str(x[0])
pw=str(x[1])
emailid=str(x[2])
print(uname)
print(pw)
print(emailid)
file_object.close()