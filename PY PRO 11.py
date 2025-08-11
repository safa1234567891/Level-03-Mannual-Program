print("TAKSHAHILA UNIVERSITY")
print("ONGUR TINDIVANAM")
print("----------------")
print("Student make list")
m1=int(input("Enter python mark:"))
m2=int(input("Enter dbms mark:"))
m3=int(input("Enter accounting mark:"))
total=m1+m2+m3
print("Total mark:",total)
avg=total/3
print("Average marek:",avg)
if m1>=40 and m2>=40 and m3>=40:
    print("resutl:pass")
if total>=250:
    print("grade:O grade*")
elif total>=200:
    print("grade:A+ grade*")
elif total>=150:
    print("grade:A grade*")
else:
    print("grade:B grade*")
    print("result:fail")
    print("grade no grade(failed")
