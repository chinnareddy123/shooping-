file1 = open("29.07.txt","w") 
file1.close()
file1=open("29.07.txt","a")
file1.write("studentname= vardhan \n")
file1.write("mobileno=9502277098\n")
file1.write("bday=23-10-2001 \n")
file1.write("erpno=210303125008\n") 
file1.write("semester=3\n")
file1 = open("29.07.txt", "r")
print("Output  after appending")
print(file1.read())
print()
file1.close()