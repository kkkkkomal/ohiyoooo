a=int(input("enter a number:"))
if a%2==0:
    print("even")
else:
     print("odd")

#largest among 3 no.s
e,f,g=int(input("Enter 3 numbers:")),int(input("Enter 3 numbers:")),int(input("Enter 3 numbers:"))
if e>f and e>g:
     print(a)
elif f>e and f>g:
     print(f)
else:
     print(g)
#leap year
year=int(input("enter the year:"))
if year%4==0:
     print("It is a leap year")
else:
     print("Not a leap year")
#update dictionary
dict1={1:"applie"}
dict1.update({3:"mango"})
print(dict1)
#

#merge 2 dictionaries 
dict01={1:36,2:34}
dict02={3:45}
dict01.update(dict02)
print(dict01)