

""" def student():
    print('This is Python Function')

student() """

def student(name,id,course_name):
    return name,id,course_name
mizan = student('mizan','1000','python')
print (mizan)

def teacher(name,designation,salary):
    print(name + ' / ' + designation + ' / ' + salary)

teacher('Ahamed','professor','4000000')

def productsum(*args):
    total=0
    for sumproduct in args:
        total = sumproduct+total
    return total
print(productsum(100,200,300,400,500,100,200,300,400,500)) 



""" ef shopkeeper(*args):
    total = 0
    for total_price in args:
        total += total_price

    return total


    
print(shopkeeper(10,10,10,10,10,10,100,10,10,10))




 """

shopdict = {
  "chal": 60,
  "dal": 140,
  "tel": 185
  
}
sum=0
for info in shopdict:

    sum +=shopdict[info]
print(sum)

shopdict = {
  "chal": 60,
  "dal": 140,
  "tel": 185
}
sum=0
for info in shopdict:

    sum +=shopdict[info]
print(sum)

