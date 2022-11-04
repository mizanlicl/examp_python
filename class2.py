a = 10
b = 20
if a == b:
    print("equal")
else:
    print("not equal")


for num in range(50,100):
    if num%2 !=0:
      print(num)
 
n = int(input("Enter number"))     
numm = 0
for num in range(1,n + 1, 1):
   
    numm = numm + num
    avg = numm / n
    mulitply = numm * avg
    minus = mulitply - numm
    Modulus = numm % n
    floor = numm // n
print("Sum of 1 to ", n , "numbers is: ", numm)
print("Avarage of 1 to ", n, "numbers is: ",numm/n)
print("Multiply of ", numm , "*", avg ," is: ", mulitply)
print("Minus of ", mulitply , "*", numm ," is: ", minus)
print("Modulus of ", numm , "%", n ," is: ", Modulus)
print("Floor of ", numm , "//", n ," is: ", floor)




""" n = int(input("Enter number"))
sum = 0
# loop from 1 to n
for num in range(1, n + 1, 1):
    sum = sum + num
print("Sum of first ", n, "numbers is: ", sum)
average = sum / n
print("Average of ", n, "numbers is: ", average) """