import string
from itertools import product
# min_len=int(input("Enter minimum length of PASSWORD :"))
# max_len=int(input("Enter maximum length of PASSWORD :"))

F_nme=input(" Enter First name :")
L_nme=input(" Enter Last name :")
p_nme=input(" Enter pet's name :")
ph=input(" Enter  Phone number :")
ph2=input(" Enter First 4 digit of Phone number :")
ph1=input(" Enter last 4 digit of Phone number :")
Dob=input(" Enter DOY :")
Data = []
Data.append(F_nme)
Data.append(L_nme)
Data.append(p_nme)
Data.append(ph1)
Data.append(ph)
Data.append(Dob)

def extra_info():
    opt = input("Do you Want to ADD more info ? [Y/N]")
    if opt == 'Y' or opt == 'y':
        data = []

        while opt == 'Y' or opt == 'y':

            val = input("Enter info :")

            data.append(val)
            opt = input("Do you Want to ADD more info ? [Y/N]")

    elif opt == 'N' or opt == 'n':
        data=[]
    else:
        print(' wrong input ')

    return (data)


val = extra_info()

Data=Data+val

# Data1=list(string.ascii_uppercase + string.ascii_lowercase + string.digits)
Data2=['@','#','$','*','&','_','-']
Data=Data+Data2
counter=0

file_open = open("Wordlist.txt",'w')    
for i in range(1,4):
    for j in product(Data,repeat=i):
       list="".join(j)
       file_open.write(list)
       file_open.write('\n')
       
       counter +=1

print(f'WORDLIST WITH {counter} PASSWORDS GENERATED')



