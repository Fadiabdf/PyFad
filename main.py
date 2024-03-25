                       #BRO CODE python tuto
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# variables
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
''' 
z = 4j 
print(type(z)) --> <class 'complex'>
'' = ""
    CLASS Str :
 firstname="Bro"
 lastname="code"
 print(type(lastname)) --> shows : class <str>
 full_name = firstname +" "+ lastname --> Bro code
 print(firstname) --> Bro
 print('firstname :'+firstname)--> firstname :Bro
 
 
 
'''
import math

#import shutil

 # °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# numbers
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
 integer
  age = 21
  age += 1 --> age = 22
  print(age) --> 22
  print(type(age)) -->  can't show the datatype because it's int
  use cast to str to display a number within a string
  print("your age is: "+str(age))
  float
  height = 250.5
  print(height)
  print("your height is :"+str(height)+"cm")
  print(type(height))
'''
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# boolean
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
 human = False
 print("are you a human : "+str(human))
'''
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# multiple assignment = allows us to assign multiple variables at the same time in one line of code
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
 name = "Bro"
 age = 21
 attractive =True
 this gonna do the same thing :
 name, age, attractive = "Bro, 21, True"
 2nd exp
 A=30
 B=30
 C=30
 they have the same value how we could do it in that case
 well like this
   A=B=C=30
'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# str methods in python
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
  name="bro"
  print(len(name)) --> the length of name
  print(name.find("b")) --> finds a character position within a Str
  print(name.capitalize()) --> the char in begening of name will be capital is there any space between words it capitalize only the first char of the 1st word
  print(name.upper()) --> make  all the char of name upper
  print(name.lower()) --> make  all the char of name lower
  print(name.isdigit()) --> check if name has only digits
  print(name.isalpha()) --> check if name has only letters
  print(name.count("o"))--> return the frequency of the letter o in name
  print(name.replace("o","a"))
  print(name*3) --> print name 3 times
'''
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# type casting = convert the data type of value to another data type
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
x = 1 # int  print(x)
y = 2.0 # float print(int(y)) --> 2
z= "3" #str print(z*3) --> 333 ///print((int)z*3) --> 9
print("X = "+x) # this is uncorrect
print("X = "+str(x)) # you have to cast into str cuz we can't concatine str to an int only str to str
'''
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
#import time
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°

# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# user input
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
by default (input) name is a str
name = input("what is your name?: ")
print("hello "+name)
age = int(input("how old are you ?")) # cast to int or float ....
we can't do this age =age+1  if age is a str
print("you are"+str(age)+"years old")
'''
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# maths functions
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
import math

pi = 3.14 
n = 3.5
print(round(pi)) --> 3 
print(round(n)) --> 4
print(math.ceil(pi)) --> rounded up pi 4
print(math.floor(pi)) --> rounded down pi 3
print(abs(pi)) --> gives the absolute value
print(pow(pi,2)) --> raze pi to the power of 2
print(math.sqrt(144)) --> 12
x=1 ,y=2 , z=3
print(max(x,y,z)) --> 3
print(min(x,y,z)) --> 1
complex( real, imag )
int( x, base )
exp( x )
log( x [,base] )
log2( x )
log10( x )
sin( x )
cos( x )
tan( x )
degrees( x )
radians( x )
gcd( x, y )#Greatest Common Divisor

 
'''
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
#slicing str
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
we use slice() 
or 
indexing[start:stop:step]
name = "Bro code"
first_name = name[0:3]
print(first_name) --> Bro
funky_name= name[::2]# it means  [0:end:2] --> B d
reversed_name = name[::-1] #  it means [0:end:-1]  to reverse the name --> orB

website1 = "http://google.com"
website2 = "http://wikipedia.com"
slice(start, stop, step)
# Create a slice object that represents elements from index 2 to 6 (exclusive)
slice = slice(7,-4)
# negetive index from right to left
# positive index from left to right
# Apply the slice to the original list
print(website1[slice])
print(website2[slice])
print(slice)
--> google
    wikipedia
    slice(7, -4, None)
    
    print('I learn %s at %d.' %(subject, age))
'''
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# if statement
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
age = int(input("how old are you ?"))
if age >= 18:
    print("you are an adult !")
elif age == 100:
    print("you are a century old !")
elif age < 0:
    print("you haven't been yet !")
else:
    print("you are a child!")
'''
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# logical operators ( or, and, not ) (|,&,!,^:xor,~ :Bitwise compliment OR,<<,>> : shift )
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
temp = int(input("what is the temprature outside ?"))
if temp >= 0 and temp <=30:
    print("the tempreture is good today !")
    print("go outside")
elif not(temp <0 or temp>30) :
    print("the tempreture is bad today")
    print("stay inside")
'''
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# while loop
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
name=""
while len(name)==0:
name =None
while not name:
    name=input("enter your name: ")

print("hello "+name)
'''
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# for loop
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
for i in range(10,0,-1): # 1st nb is exclusive the 2nd is inclusive in my exp
    print(i+1)
      -->  9,8,7,6...0

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)# wait for one second

print("happy new year!")
'''
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# nested loops :  (loop in side another loop )the inner loop  inside the outer loop
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
rows=int(input("how many rowss? :"))
columns = int(input("how many clolumns? : "))
symbol = input("enter a symbol to use: ")
for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
        print()
        
    # , end="" without moving auto  to the next line
     pour sauter la ligne une fois terminer _une ligne
     NB: pay attention to the andentation 
    
'''
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# loop control statements:change a loop execution from its normal sequence
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
 break : terminate the loop entirely sortir de la boucle
 continue : skips to the next iteration
 pass : does nothing,acts as a placeholder
 
    while True:
       name= input("Enter your name: ")
       if name != "";
       break
       
    tel="123-456-7890"
    for i in tel:
       if i == "-":
         continue # skip the "-"
         print(i,end="")
         
         --> 1234567890
         
    for i in range(1,21):
        if i== 13:
          pass # won't do anything
        else:
          print(i)
          
        --> 1 # inclusif
            2 ....
            12
            14
            15...
            20
               # 21 execlusif 
         
'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# list : a variable that is used to store multiple items in a single var
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
الـ List عبارة عن مصفوفة حجمها غير ثابت و يمكنها تخزين قيم من مختلف الأنواع في وقت واحد.
food =["pizza","hambergers","hotdog","spagetti"]
food[0]="sushi"
print(food[0]) #--> sushi
print(food)#--> ['sushi', 'hambergers', 'hotdog', 'spagetti']
for x in food:
    print(x)
     #sushi
     #hambergers
     #hotdog
     #spagetti
  # هنا قمنا بتعريف مصفوفة من النصوص تتألف من 4 عناصر 
languages = [str] * 4
  # هنا قمنا بوضع قيمة في كل عنصر فيها
languages[0] = 'Arabic'
languages[1] = 'French'
languages[2] = 'English'
languages[3] = 'Spanish'

'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# function of lists
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
food.append("ice cream") #add to the list at the end
food.remove("hotdog") # remove from the list
food.pop()#remove the last element of the list
food.insert(0,"cake")# insert cake at the position of 0
food.sort()#sort the list alphabitacally
food.clear#remove all the elements to have an empty list 
'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# 2D lists= a list of list
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
drinks = ["coffe","soda","tea"]
dinner = ["pizza","hamberger","hotdog"]
dessert = ["cake","ice cream"]

food =[drinks,dinner,dessert]
print(food)
# --> [['coffe', 'soda', 'tea'], ['pizza', 'hamberger', 'hotdog'], ['cake', 'ice cream']]
print(food[0])
#--> ['coffe', 'soda', 'tea']
print(food[0][2])
#--> tea
'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# tuple: collection which is orderred and unchangeable used to group together related data
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
الـ Tuple عبارة عن مصفوفة حجمها ثابت و قيمها غير قابلة للتغيير و يمكنها تخزين قيم من مختلف الأنواع في وقت واحد.
student = ("Bro",21,"male")

print(student.count("Bro")) # --> 1  // how many times the value of Bro appears
print(student.index("male")) # --> 2 // find the index of the value male
# display valuesof the tuple student
for x in student:
    print(x)

    # Bro
    # 21
    # male

if "Bro" in student:
    print("Bro is here!")
'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# set: collection which is unordered,unindexed,No duplicate values
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
الـ Set عبارة عن مصفوفة ليس لها حجم ثابت و قيمها غير قابلة للتغيير و يمكنها تخزين قيم من مختلف الأنواع في وقت واحد.
في مصفوفات الـ Set يتم تخزين البيانات بشكل عشوائي و ليس بالترتيب كما تم إدخالهم, و السبب في أنه في هذا النوع من المصفوفات لا يتم إعطاء رقم Index خاص لكل عنصر.
لهذا السبب أيضاً, لا يمكنك الوصول لعنصر محدد في Set بشكل مباشر لأنه في الأساس لا يملك رقم Index
utensiles ={"fork","spoon","knife"}
dishes = {"bowl","plate","cup","knife"}


utensiles.add("napkin")
utensiles.remove("fork")
utensiles.clear()

dishes.update(utensiles)#add elements of utensiles to ones of dishes
# operations on set like ensemble in algerba
dinner_table =utensiles.union(dishes)
print(utensiles.difference(dishes))
print(utensiles.intersection(dishes))
'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# dictionary : a changeable,unordered collection of unique key:value pairs
# fast because they use hashing,allow us to access a value quickly
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
عند إستخدام الـ List أو Tuple فإنك تتعامل مع عناصرهم من خلال أرقام الـ Indices.
فكرة الـ Dictionary هي وضع مفتاح لكل قيمة. عندها تصل لقيمة كل عنصر موجود من خلال المفتاح الخاص فيه.
capitals = {
    'USA':'washington DC',
    'Indea':'New Dehli',
    'China':'Beijing',
    'Russia':'Moscow'
}
capitals.update({'Germany':'Berlin'})# add a new one
capitals.update({'USA':'NEWYork'}) # modifier
capitals.pop(('China'))# remove the value&key of china
capitals.clear()

print(capitals['Russia'])#-->Moscow
#print(capitals['Germany'])#-->error !exist
print(capitals.get('Germany'))#--> None
print(capitals.keys())#--> dict_keys(['USA', 'Indea', 'China', 'Russia'])
print(capitals.values())#--> display only the values
print(capitals.items())#--> display the entirely dictionnary (keys and values)

for key,value in capitals.items():
    print(key,value)
'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# index operator [] = gives access to a sequence's element(str,list,tuples)
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
name = "bro Code!"
if(name[0].islower()):
    name=name.capitalize()

first_name = name[:3].upper()
last_name = name[4:].lower()
last_char = name[-1]

print(first_name)#--> BRO
print(last_char)#--> !
print(last_name)#-->code
'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# functions: a block of code which is executed only when it is called
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
#we have to have nb matching parameters with given arguments
def hello(fname,lname,age):
    #pass# write it if you don't really know what the finction shoold do
    print("hello!"+fname+" "+lname)
    print("you are "+str(age)+" years old")
    print("have a nice day!")

my_fname = "Bro"
my_lname ="code"
a=12
hello(my_fname,my_lname,a)
hello("dude","didi",20)
'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# return statement = Functions send python values/objects back
# to the caller.
# these values /obj are known as the function's return value
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
def multiply(n1,n2):
    #result = n1*n2
    #return result
    return n1*n2
print(multiply(2,5))
'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
#  keyword arguments = arg preceded by an identifier when pass them
# to a func the order of the arg doeson't matter,unlike positional arg
# python knows the names of the arg that our func recieves
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
def hello(first,middle,last):
    print("hello "+first+" "+middle+" "+last)
# order of arg here matters
hello("code","dude","bro") #--> hello code dude bro
hello("bro","dude","code") #--> hello bro dude code
# using key words arg --> order doeson't matter
hello(last="code",middle="dude",first="bro") #--> hello bro dude code
'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# nested functions calls = function calls inside other function cals  innerlost func calls are resolved first
# returned value is used as argument for the next outer function
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
num = input("enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)

print(round(abs(float(input("enter a whole positive number: ")))))
'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# scope: the reion that a var is recognized
# a var is only available from inside the region it is  created
# a global and locally scoped versions of a var can be created
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
name ="bro" # global scope (available inside & outside functions)
def display_name():
    #name = "code" #local scope= local variable ( available only inside this function)
    print(name) #--> python xill look for a global var and displays Bro

print(name)

# python look for
  # L=local --> E=enclosing --> G=global --> B=Built-in
'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# *args = parameter that will pack all arguments into a tuple
# useful so that a function can accept  a varying amount of arguments
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
def add(n1,n2):
  return n1+n2

add(1,2,3) # a lot of arguments 3 au lieu de 2
def add(*stuff):# def add(*args):
    sum=0
    
    # stuff now is tuple (...,..,..)
    stuff = list(stuff)# cast to list so as to be able to modify"
    stuff[0]=0
    for i in args: # for i in stuff:
        sum+= i
    return sum

print(add(1,2,3,4,5,6,7))
'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# **kwargs = parameter that will pack all arguments into a dictionary
# useful so that a unction can accept a varying amount of keyword arguments
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
def hello(first,last):
    print("hello "+first +" "+last)

hello(first="bro",middle="dude",last="code")# a lot of key words argument 3 au lieu 2

def hello(**kwargs): # def hello(**names):
    #print("hello"+kwargs['first']+' '+kwargs['last'])
    print("hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ") # prints all the names on the same line

hello(title="Mr.",first="bro",middle="dude",last="code")
'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# str.format()= optional method that gives users more control when displaying output
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
number = 1000
print("the number pi is {:.3f}".format(number))# the number pi is 1000.000 // display just 3 digits after .
print("the number pi is {:,}".format(number))#the number pi is 1,000 // add a comma
print("the number pi is {:b}".format(number))#the number pi is 1111101000 // binary rep
print("the number pi is {:o}".format(number))#the number pi is 1750 //  4 rep
print("the number pi is {:X}".format(number))#the number pi is 3E8 // hexadec representation
print("the number pi is {:E}".format(number))#the number pi is 1.000000E+03 // scientific notation

animal ="cow"
item="moon"
# we can use the same index / keyword (repeat)
#like placeholder for a var /value the position is important
#print("the "+animal+" jumped over the "+item)
print("the {} jumped over the {}".format("animal","item"))
print("the {1} jumped over the {0}".format(animal,item)) #positionnal argument
print("the {animal} jumped over the {item}".format(animal="cow",item="moon")) #key word arg

text = "the{} jumped over the{}"
print(text.format(animal,item))
# adding some padding to the str
name="bro"
print("hello,my name is {}".format(name))#--> hello,my name is bro
print("hello,my name is {:10}. Nice to meet you ".format(name))#--> hello,my name is bro       . Nice to meet you
print("hello,my name is {:<10}. Nice to meet you ".format(name))# used to align  hello,my name is bro       . Nice to meet you
print("hello,my name is {:>10}. Nice to meet you ".format(name))#hello,my name is        bro. Nice to meet you
print("hello,my name is {:^10}. Nice to meet you ".format(name))# used to center hello,my name is    bro    . Nice to meet you
'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# random numbers
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
import random
x = random.randint(1,6)
y = random.random()
print(x,y)# --> 6 0.04895634343822752

myList =  ['rock','paper','scissors']
z = random.choice(myList)
print(z)# --> scissors

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)
print(cards)
# --> [7, 6, 4, 'A', 'Q', 3, 'J', 'K', 9, 2, 1, 8, 5]  ba3tharhomli
'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# exception:events detected during execution that interrupt the flow of a program
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
try:
    numerator = int(input("enter a number to devide: "))
    denominnator = int(input("enter a number to devide by: "))
    result = numerator/ denominnator

except ZeroDivisionError as e:
    print(e)# + as e to display what exception is
    print("you can't divide by zero !")
except ValueError:
    print("enter only  numbers plz")
except Exception:
    print("something went wrong :(")
else:
    print(result)
finally:
    print("this will always execute!")
'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# file detection
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
import os
path = "C:\\Users\\dell\\Desktop\\file.txt"
if os.path.exists(path):
    print("that location exists!")
    if os.path.isfile(path):
        print("that is a file")
    elif os.path.isdir(path):
        print("that is a dirctory")
else:
    print("that location dosen't exist!")
'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# reading file
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
try :
    with open("C:\\Users\\dell\\Desktop\\file.txt") as file:
         print(file.read())
except FileNotFoundError:
    print('that file was not found :(')
'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
#   write a file
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
text = "yoooooooo\nthis is some text\n have a good day"
with open("C:\\Users\\dell\\Desktop\\file.txt",'w') as file:
    file.write(text)

# with open('test.txt','a') as file // to append  : add by the end
# with open('test.txt','w') as file// to write by the beginning
'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# copying file
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
# copyfile() : copies contents of a file from source into a destination
# copy() : copyfile() + permission mode + destination can be a directory
# copy2() : copy()+ copies metadata (file's creation and modification times)

import shutil
shutil.copyfile('file.txt','copy.txt')#src,dst
'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# delete a file/folder
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
import os
import shutil
source = "test.txt"
destination = "C:\\users\\dell\\desktop\\test.txt"

try:
    if os.path.exists(destination):
        print("there is already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")

path = "empty_folder"
try:
   # os.remove(path)# delete file
   # os.rmdir(path)# delete an empty dir
   #shutil.rmtree(path)#delete a dir containing files
except FileNotFoundError:
    print("that file was not found")
except OSError:
    print("you can not delete that using that function!")
except PermissionError:
    print("you do not have permission to delete that")
else:
    print(path+" was deleted")
'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# module: file containing python code. may contain functions,classes, etc
# used with modular programming,which is to separate a program into parts
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
import messages # module without nickname

messages.hello()
messages.bye()

import messages as msg # module with nickname

msg.hello()
msg.bye()

from messages import hello,bye
from messages import *

messages.hello()
messages.bye()

# to get some useful ready implemanted module just
help("modules")
#Enter any module name to get more help.  Or, type "modules spam" to search
#for modules whose name or summary contain the string "spam".
'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# OOP
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
from car import Car
'''
car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

print(car_1.make)
print(car_1.model)
print(car_2.year)
print(car_2.color)

car_1.drive()
car_2.stop()
'''
# class instance variables
'''
car_1.wheels = 2 # changed from 4 to 2
'''
# inheritance = Héritage
'''
class Animal:
    alive = True

    def eat(self):
       print("this animal is eating")

    def sleep(self):
        print("this animal is sleeping")
# class child_class(parent_class) : extends
class Rabbit(Animal):
    def run(self):
        print("this rabbit is raunning")
class Fish(Animal):
    def swim(self):
        print("this fish is swimming")
class Hawk(Animal):
    def fly(self):
        print("this hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()
'''
# multi_level inheritance : when a deerived (child) class inherits another derived class
'''
class Organism:
    alive = True

class Animal(Organism):
    def eat(self):
        print("this animal is eating")

class Dog(Animal):
    def bark(self):
        print("this dog is barking")

dog = Dog()
print(dog.alive)
dog.bark()
dog.eat()
'''
# how it works
'''
class Prey:
    def flee(self):
        print("this animal flees")
class Predator:
    def hunt(self):
        print("this animal is hunting")
class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey,Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

fish.flee()
fish.hunt()
'''
#method overiding
'''
class Animal:
    def eat(self):
        print("this animal is eating")

class Rabbit(Animal):
    def eat(self):
        print("this rabbit is eating a carrot")

rabbit = Rabbit()
rabbit.eat() #--> this rabbit is eating a carrot it execute the more closer the eat of rabbit and not of the animal (parent)
'''
#method chaining = calling multiple methods sequentially
# each call performs an action on the same object and returns self
'''
class Car:
    def turn_on(self):
        print("you start the engine")
        return self
    def drive(self):
        print("you drive the car")
        return self
    def brake(self):
        print("you step on the brakes")
        return self
    def turn_off(self):
        print("you turn off the engine")

    car = Car()
    car.turn_on().drive()#method chaining calling methoods then immediatly ...
    car.brake().turn_off()
    car.turn_on().drive().brake().turn_off()
# or like this is more organizing in case a lot of method chaining
    car.turn_on()\
        .drive()\
        .brake()\
        .turn_off()
'''
# super() = function used to give access to the methods of parent class.
# returns a temporary object of a parent class when used
'''
class Rectangle:
    def __init__(self,length,width,height):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self,length,width):
        #self.length = length
        #self.width = width
        # instead we use
        super().__init__(length,width)
    def area(self):
        return self.length*self.width

class Cube(Rectangle):
    def __init__(self,length,width,height):
        #self.length = length
        #self.width = width
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height

square = Square(3,3)
cube = Cube(3,3,3)

print(square.area) #--> 9
print(cube.volume) #--> 27
'''
# prevent the user from creating  an object of that class
# + comples a user to override abstract methods in a child class

# abstruct class : a class which contains one or more abstract methods : not real a ghost class
# abstruct method : a method that has a declaration but does not have an implementation but it's need to be overited in the children classes
'''
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod # decorator
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def go(self):
        print("you drive the car")

class Motorcycle(Vehicle):
    def go(self):
        print("you ride the motorcycle")

    def stop(self):
        print("this motorcycle is stopped")

# vehicle = Vehicle() ne peut pas etre instancier creer object from it cuz it's abstract
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()
car.stop()
'''
# we can pass objects as arguments
'''
class Car:
    color = None

class Motorcycle:
    color = None

bike_1 = Motorcycle()
def change_color(car,color):
    car.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

change_color(car_1,"red")
change_color(car_2,"white")
change_color(car_3,"blue")
'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# Duck typing = concept where the class of an object is less important than the methods
# class type is not checked if min methods/attributes are present
# "If it walks a duck,and it quacks like a duck ,then it must be a duck
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
class Duck:
   def walk(self):
       print("this duck is walking")

   def talk(self):
       print("this duck is qwuaking")

class Chicken:
    def walk(self):
        print("this chicken is walking")
    def talk(self):
        print("this chicken is clucking")
class Person():
    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("you caught the critter!")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
person.catch(chicken)#should work also  cuz it has the same methods not the same object type 
'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# walrus operator :=
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°

# new to python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of larger expression
# assigned and use in one expression
'''
foods = list()
while True:
    food = input('what food do you like?: ')
    if food == "quit":
        break
    foods.append(food)

foods = list()
while food := input('what food do you like?: ') != "quit" :
    foods.append(food)
'''
#  assign function to variable
'''
def hello():
    print('hello')

print(hello)# <function hello at 0x0188D850>

hi = hello# we assign the memory address of flow to the hi variable so we can know use hi as a function
hello()
hi()

say = print# don't use the ()
say("whoa! I can't beleive this works! :O ")# will do the same as print function
'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# higher order function = a func that either:
#                   1. accepts a func as an argument
#                   2. returns a func (in python,functions are also treated as objects)
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
def loud (text):
    return text.upper()
def quiet(text):
    return text.lower()

def hello(func):
    text = func("hello")
    print(text)

hello(loud)# function as an argument  --> HELLO
hello(quiet)# --> hello

def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
print(divide(10)) #--> 5.0 // divide <-- dividend comes from divisor
'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# lambda function :
# function written in 1 line using lambda keyword
# accepts any number of arguments ,but only has one expression
# (think of it as a shortcut )
# (useful if needed for a short period of time , throw-away)
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# lambda parameters:expression # syntax
'''
def double(x):
    return  x*2

print(double(5))
# this gonna do the same
double = lambda x: x * 2
print(double(5))

multiply = lambda x, y: x * y
print(multiply(5,6))

add = lambda x, y, z: x + y + z
print(add(5, 6, 7))

full_name = lambda first_name, last_name: first_name+" "+last_name
print(full_name("Bro","Code"))

age_check = lambda age: True if age >= 18 else False
print(age_check(18))
'''
# sort data:
# sort() method = used with lists
# sorted() function = used with iterables
'''
#list
students = ["Squidward","Sandy","Patrick","Spongebob","Mr.Krabs"]
students.sort()
students.sort(reverse=True)
# tuple
students = ("Squidward","Sandy","Patrick","Spongebob","Mr.Krabs")
sorted_students = sorted(students,reverse=True)
# list of tuples
students = [("Squidward","F",60),
            ("Sandy","A",33),
            ("Patrick","D",36),
            ("Spongebob","B",20),
            ("Mr.Krabs","C",78)]
grade = lambda grades: grades[1]
age = lambda ages:ages[2]

students.sort(key=grade,reverse = True)
students.sort(key=age,reverse = True)

# tuple of tuples
students = (("Squidward","F",60),
            ("Sandy","A",33),
            ("Patrick","D",36),
            ("Spongebob","B",20),
            ("Mr.Krabs","C",78))
age = lambda ages:ages[2]

sorted_students = sorted(students,key=age)
'''
# map() = applies a function to each item in an iterable (list,tuple...)
# map(function,iterable)
'''
store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]

to_euros = lambda data: (data[0],data[1]*0.82)
to_dollars = lambda data: (data[0],data[1]/0.82)
store_euros = list(map(to_euros,store))

for i in store_euros:
    print(i)
'''
# filter() = creates a collection of elements from an iterable for which a function returns

# filter(function, iterable)
'''
friends = [("Rachel",19),
           ("Monica",18),
           ("Phoebe",17)
           ]

age = lambda data:data[1] >= 18
ado= list(filter(age, friends))
'''
# reduce() = apply a function to an iterable and reduce it to a single cumulative value
# performs function on first two elements and repeats process until 1 value remains

# reduce(function,iterable)
'''
import functools

letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x, y: x+y,letters)
print(word)# --> HE L L O  --> HEL L O --> HELL O --> HELLO

factorial = [5,4,3,2,1]
result = functools.reduce(lambda x, y: x*y,factorial)
print(result)# --> 5*4 =20 --> 20* 3 --> 60 --> 60*2 --> 120*1 --> 120 = 4!
'''
# list comprehension = a way to create anew list with less syntax
# can mimic certain lambda functions ,easier to read
# list = [expression for item in iterable]
# list = [expression for item in iterable if conditional]
# list = [expression if/else for item in iterable]
'''
squares = []
for i in range(1,11):
    squares.append(pow(i,2))

print(squares)
# --> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
squares = [i*i for i in range(1,11)]

print(squares)
# --> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


students = [100,90,80,70,60,50,40,30,0]
passed_students = list(filter(lambda x: x >= 60, students))
print(passed_students) #--> [100, 90, 80, 70, 60]

passed_students = [i for i in students if i >= 60]
print(passed_students) #--> [100, 90, 80, 70, 60]

passed_students = [i  if i >= 60 else "FAILD" for i in students]
print(passed_students) #--> [100, 90, 80, 70, 60, 'FAILD', 'FAILD', 'FAILD', 'FAILD']
'''
# dictionary comprehensive : create dictionaries using an expression
# can replace for loops and certain lambda functions
'''
# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable }
#---------------------------------------------------------------------------

cities_in_F = {'new york':32,'Boston':75,'los angeless':100,'chicago':50}

cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}

print(cities_in_C) #--> {'new york': 0, 'Boston': 24, 'los angeless': 38, 'chicago': 10}

weather = {'new york':'snowing','Boston':'sunny','los angeless':'sunny','chicago':'snowing'}
sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}
print(sunny_weather)# --> {'Boston': 'sunny', 'los angeless': 'sunny'}

desc_cities = {key: ("warm" if value >= 40 else "cold") for (key,value) in cities_in_F.items() }
print(desc_cities)#--> {'new york': 'cold', 'Boston': 'warm', 'los angeless': 'warm', 'chicago': 'warm'}
def check_temp(value):
    if value >= 70:
        return "hot"
    elif 69 >= value >= 40:
        return "warm"
    else:
        return "cold"
desc_cities = {key: (check_temp(value)) for (key,value) in cities_in_F.items() }
print(desc_cities)#--> {'new york': 'cold', 'Boston': 'hot', 'los angeless': 'hot', 'chicago': 'warm'}
'''
# zip function
# zip(*iterables) = aggregate elements from two or more iterables (list,tuples,sets,....)
# creates a zip object with paired elements stord in tuples for each element
'''
usernames = ["Dude","bro","mister"]
passwords = ("p@ssword","abc123","guest")

users = zip(usernames,passwords)
for i in users:
   print(i)

'''
('Dude', 'p@ssword')
('bro', 'abc123')
('mister', 'guest')
'''
users = dict(zip(usernames,passwords))# cast to dict /list whatever you want
print(type(users)) #--> <class 'dict'>
for key,value in users.items():
    print(key+" : "+value)

'''
'''
Dude : p@ssword
bro : abc123
mister : guest
'''
'''

login_date = ["1/1/2021","1/4/2022","6/1/2023"]
users = zip(usernames,passwords,login_date)

for i in users:
    print(i)

'''
('Dude', 'p@ssword', '1/1/2021')
('bro', 'abc123', '1/4/2022')
('mister', 'guest', '6/1/2023')
'''
'''
# ********************************
# if __name__ == '__main__'
# *****************************

# y tho?
# 1. module can be run as a standalone program
# 2. module can be imported and used by other modules

# python interpreter sets "special var",one od which is __name__
# then python will execute the code found within __main__
# python will assign the __name__ var a value  of '__main__' if it's
# the initial module being run
'''

import messages
print(__name__)
print(messages.__name__)

'''
'''
__main__
messages'''
'''
if __name__ == '__main__':
    print("running this module direct")
else:
    print("running this module indirect")

#--> running this module direct in that case
def main():
    print('hello')
if __name__ == '__main__':
    main()
'''
# time module
'''
import time
# find my computer epoch you can change it
print(time.ctime(0)) #--> Thu Jan  1 01:00:00 1970
# convert a time expressed in seconds since epoch to a readable string
# epoch : when your computer thinks time began (reference point)
print(time.ctime(1000000)) # --> Mon Jan 12 14:46:40 1970

print(time.time())# return current seconds since epoch : 1692741142.2470863

print(time.ctime(time.time()))# --> return the current time :Tue Aug 22 22:54:12 2023

time_object = time.localtime()
print(time_object)
# --> time.struct_time(tm_year=2023, tm_mon=8, tm_mday=22, tm_hour=22, tm_min=55, tm_sec=58, tm_wday=1, tm_yday=234, tm_isdst=0)
# let's put it in a format
local_time = time.strftime("%B %d %Y %H:%M:%S",time_object)
print(local_time) #--> August 22 2023 22:58:37

time_object = time.gmtime()#UTC time

time_string = "20 April,2020"
time.strptime(time_string,"%d %B,%Y")
print(time_object)
# year,month,day,hours,minutes,secs,day of the week,day of the year,dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0 ,0)

time_string = time.asctime(time_tuple)
print(time_string) # Mon Apr 20 04:20:00 2020

time_string = time.mktime(time_tuple)
print(time_string) # converted to seconds --> 1587352800.0
'''
# multithreading
# thread = a flow execution like a seperate order of instructions
# however each thread takes a turn running to achieve concurrency
#         GIL = global interpreter lock
#         allows only one thread to hold the control of python interpreter at any one time
# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing
# io bound = program/task spends most of it's time waiting for external events (user input,web scrap)
#            use multithreading
'''

import threading
import time

print(threading.active_count())
print(threading.enumerate())

# 1
# [<_MainThread(MainThread, started 3568)>]

def eat_breakfast():
    time.sleep(3)
    print("you eat breakfast")

def drink_coffe():
    time.sleep(4)
    print("you drunk coffe")

def study():
    time.sleep(5)
    print("you finsh studying")
# we complete these tasks sequentially nand not currently in order not the same time : multithreading  not multitasking

eat_breakfast()
drink_coffe()
study()

# --> 1 thread 12sec

x = threading.Thread(target=eat_breakfast,args=())
x.start()

y = threading.Thread(target=drink_coffe,args=())
y.start()

z = threading.Thread(target=study,args=())
z.start()

# --> 4 threads just five sec
print(time.perf_counter()) # how it took to complete 

x.join()
y.join()
z.join()
#--> we only have one main thread after join
'''
# daemon thread = a thread that runs in the background,not important for program to run
# your program will not wait for daemon threads to complete before exiting
# non-daemon threads cannot normally stay alive until task is complete
# ex. background tasks, garbage collection waiting for input long running process
'''
import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for:",count,"seconds")
        
x = threading.Thread(target=timer, daemon=True)
x.start()

x.setDaemon(True)
print(x.isDaemon())
answer = input("Do you wish to exit?")
'''
#**********************
# multiprocessing
#**********************
#multiprocessing = running tasks in parallel on diffrent  cpu cores, bypasses GIL used for  thread
#  multiprocessing = better for cpu bound tasks (heavy cpu usage)
#  multithreading = better for io bound tasks (waiting around)
'''
from multiprocessing import Process, cpu_count
import time
def counter(num):
    count = 0
    while count < num:
        count += 1
def main():
    print(cpu_count())
    #a = Process(target=counter, args=(1000000000,))

    a = Process(target=counter, args=(500000000,))
    b = Process(target=counter, args=(500000000,))

    b.start()
    a.start()

    a.join()
    b.join()
    print("finished in:",time.perf_counter(),"seconds")

if __name__ == '__main__':
   main()# create a child process
'''
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# GUI: graphical user interface
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
'''
from tkinter import *
# widgets = GUI elements: buttons,textboxes,labels,images
# windows = serves as a container to hold or contain these widgets

window = Tk() # instantiate an instance of a window
window.geometry("420x420")# set the width and height of the window
window.title("Bro code first gui program")# change the title

#icon = PhotoImage(file='python.png')
#window.iconphoto(True,icon)

window.config(background="black")

window.mainloop()# place window on computer screen , listen for events
'''
# label : area widget that holds text and/or an img within a window
'''
from tkinter import *
window = Tk()
icon = PhotoImage(file='python.png')
window.iconphoto(True,icon)
# customize the label

photo = PhotoImage(file='python.png') # il faut juste une petite photo quelleques choses comme ça
label = Label(window,
              text="hello world",
              font=('Arial',40,'bold'),
              fg='#00FF00',bg='black',
              relief=RAISED,# add a border
              bd=10,# the size of the border
              padx=20,# space between the text and the border
              pady=20 ,# add space
              image=photo,
              compound='bottom')

# to show the label in the window = add a label to the window we use :
label.pack()# add to the center
label.place(x=0,y=0)# place the label in the top left corner of the window

window.mainloop()
'''
# button = you click it,then it does stuff
'''
from tkinter import *
count = 0
def click():
    global count
    count += 1
    print(count)
    print("you clicked the button!")# you clicked the button! showed up in the console when clicked

window = Tk()
photo = PhotoImage(file='python.png')# we must add it after the window to show it up

# create a button:
button = Button(window,
                text="click me!",
                command=click,
                font=("Comic Sans",30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",# to not flash when click on the button
                state=ACTIVE,
                activebackground="black",
                image=photo,
                compound="bottom"
                )
button.pack()# add the button to the window to show up

window.mainloop()
'''

# entry widget = textbox that accepts a single line of user input
'''
from tkinter import *

def submit():
    username = entry.get()
    print("hello "+username)
    entry.config(state=DISABLED)

def delete():
    entry.delete(0,END)# delete all of the caracters

def backspace():
    entry.delete(len(entry.get())-1,END)
window = Tk()

entry = Entry(window,
              font=('Arial',50),
              fg="#00FF00",
              bg="black",
              show="*"# to show hidden text
              )
entry.insert(0,'Spongebob')
entry.pack(side=LEFT)

submit_button = Button(window,text="submit",command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,text="delete",command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,text="backspace",command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()
'''
# check buttons
'''
from tkinter import *
def display():
    if(x.get()==1):
        print("you agree!")
    else:
        print("you don't agree ! ")
window = Tk()
photo = PhotoImage(file='python.png')

x = IntVar() # 1/0
#x = BooleanVar() # True/False
#x = StringVar() # yes/no
check_button = Checkbutton(window,
                           text="i agree to something",
                           variable=x,
                           onvalue=1,# True /yes
                           offvalue=0,
                           command=display,
                           font=('Arial',20),
                           fg='#00FF00',
                           bg='black',
                           activeforeground='#00FF00',
                           activebackground='black',
                           padx=25,
                           pady=10,
                           image=photo,
                           compound='left'
                           )
check_button.pack()
window.mainloop()
'''
# scale
''' 
from tkinter import *
                       
def submit():
    print("the tempreture is: "+str(scale.get())+" degrees C")
    
window = Tk()
                       
hot_img=PhotoImage(file='hot.png')
hotLabel = Label(image=hot_img)
hotLabel.pack()
                       
scale = Scale(window,
              from_=1000,
              to=0,
              length=600,
              orient=VERTICAL,#ortientation of scale
              font=('Consolas',20),
              tickinterval=10,#adds numeric indicators for value
              showvalue=0,#hide current value)
              resolution=5,#increment of slider
              throughcolor='#69EAFF',
              fg="#FF1C00",
              bg='#111111')
                       
scale.set(((scale['from']-sclae['to'])/2)+scale['to'])# ser curent value of slider
scale.pack()
                       
cold_img=PhotoImage(file='cold.png')
coldLabel = Label(image=cold_img)
coldLabel.pack()
                       
                       
button = Button(window,text="submit",command=submit)
button.pack()
                       
window.mainloop()
'''
# radio button = similar to checkbox,but you can only select one from a group
'''
from tkinter import *
food = ["pizza","humberger","hotdog"]
                       
def order():
    if(x.get()==0):
       print("you ordered pizza")
    elif(x.get()==1):
       print("you ordered humberger")
    elif(x.get()==2)!
       print("you ordered a hotdog")
    else:
       print("huh?")
window = Tk()
                       
x = IntVar()
pizzaImage = PhotoImage(file='pizza.png')
humbergerImage = PhotoImage(file='humberger.png')
hotdogImage = PhotoImage(file='hotdog.png')
                       
foodImages = [pizzaImage,humbergerImage,hotdogImage]
                       
for index in range(len(food)):
     radiobutton = Radiobutton(window,
                               text=food[index],# adds text to radio buttons
                               variable=x,#groups radiobuttons together if they share the same variable 
                               value=index,# assign each radio button a diffrent value
                               padx= 25,#adds padding on x-axis
                               font=("Impact",50),
                               image=foodImages[index],#adds image to radiobutton
                               compound='left' #adds image & text (left-side)
                               indicater=0# eleminate circle indicators
                               width=375,#sets of radiobuttons
                               command=order# don't add the () ,set command of radiobutton to function
                              )
                       
                       
radiobutton.pack(anchor=W)
                       
window.mainloop()
'''
# listbox = A listing of selectable tewt items within it's own container
'''

from tkinter import *
def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    print("you have ordered : ")
    #print(listbox.get(listbox.curselection()))
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    #listbox.delete(listbox.curselection())
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constania",35),
                  width=12,
                  selectmode=MULTIPLE,
                  )
listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"bread")
listbox.insert(4,"soop")
listbox.insert(5,"salad")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

addButton = Button(window,text="add",command=add)
addButton.pack()

deleteButton = Button(window,text="delete",command=delete)
deleteButton.pack()

submitButton = Button(window,text="submit",command=submit)
submitButton.pack()

window.mainloop()
'''
# messagebox
'''
from tkinter import *
from tkinter import messagebox #import meassagebox library
def click():
   # messagebox.showinfo(title="this is an info",message="you are a person")
   # while True:
        #messagebox.showwarning(title='Warning! ', message="you have a virus!!!")

    #messagebox.showwarning(title='Warning! ',message="you have a virus!!!")
    #messagebox.showerror(title='ERROR! ',message="something went wrong!!!")

    #if messagebox.askokcancel(title='ask ok cancel ',message="do you want to do thing?"):
    #    print("you did a thing!")
    #else:
    #    print("you canceled a thing!")

    #if messagebox.askretrycancel(title='ask try cancel ',message="do you want to retry a thing?"):
    #   print("you retried a thing!")
    #else:
    #   print("you canceled a thing!")

    #if messagebox.askyesno(title="ask yes or no",message="do you like cake?"):
    #    print('L like cake too:')
    #else:
    #    print("why do you not like cake :(")
   #answer = messagebox.askquestion(title='ask a question',message='do you like pie?')
   #if (answer == 'yes'):
   #    print('L like pie too :)')
   #else:
   #    print('why do you not like pie? :(')
   #print(messagebox.askyesnocancel(title='yes no cancel',message="do you like to code?"))# return boolean value
   answer = messagebox.askyesnocancel(title='yes no cancel',message="do you like to code?",icon='warning')
   if(answer == True):
       print("you like to code")
   elif(answer == False):
       print("then why you are watching a video on coding?")
   else:
       print("you have dodged the question")

window=Tk()

button = Button(window,command=click,text='click me')
button.pack()

window.mainloop()
'''
# color chooser
'''
from tkinter import *
from tkinter import colorchooser #submodule

def click():
    #color = colorchooser.askcolor()
    #print(color)
    #colorhex = color[1]
    #print(colorhex)
    #window.config(bg=colorhex)#change background color
    # in one line of code
    window.config(bg=colorchooser.askcolor()[1])#change background color

window = Tk()
window.geometry("420x420")
button = Button(text='click me',command=click)
button.pack()

window.mainloop()
'''
# text widget : functions like a text area,you can enter multiple line of text
'''
from tkinter import *
def submit():
    input = text.get("1.0",END)
    print(input)

window = Tk()

text = Text(window,
            bg="light yellow",
            font=("Ink Free",25),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg="purple")
text.pack()
button = Button(window,text="submit",command=submit)
button.pack()
window.mainloop()
'''
# file dialog
'''
from tkinter import *
from tkinter import filedialog

def openfile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\dell\\PycharmProjects\\pyfad",
                                          title="open file okay?",
                                          filetypes=(("text files","*.txt"),("all file","*.*")))
    file = open(filepath,'r')
    print(file.read())
    file.close()

window = Tk()
button = Button(window,text='Open',command=openfile)
button.pack()
window.mainloop()
'''
# save a file
'''
from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\dell\\PycharmProjects\\pyfad",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("HtML file",".html"),
                                        ("All files",".*")
                                    ])
    if file is None:
        return
    
    #filetext = str(text.get(1.0,END))
    filetext = input("enter some text i guess: ")

    file.write(filetext)
    file.close()
window = Tk()
button = Button(window,text='Save',command=saveFile)
button.pack()
text = Text(window)
text.pack()

window.mainloop()
'''
# set a menubar
'''
from tkinter import *
def openFile():
    print("File has been opened")

def saveFile():
    print("File has been saved")

def cut():
    print("you cut some text")

def copy():
    print("you copied some text")

def paste():
    print("you print some text")
window = Tk()

openimg = PhotoImage(file='file.png')
saveimg = PhotoImage(file='save.png')
exitimg = PhotoImage(file='exit.png')

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,
                tearoff=0,
                font=("MV Boli",15))

menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile,image=openimg,compound='left')
fileMenu.add_separator()
fileMenu.add_command(label="Save",command=saveFile,image=saveimg,compound='left')
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit,image=exitimg,compound='left')

editMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)


window.mainloop()
'''
# frame = a rectangular container to group and hold widgets
'''
from tkinter import *
window = Tk()
#button = Button(window,text="W",font=('consolas',25),width=3)
#button.pack()
frame = Frame(window,bg='pink',bd=5,relief=SUNKEN)
#frame.pack(side=BOTTOM)
frame.place(x=100,y=100)
Button(frame,text="W",font=('consolas',25),width=3).pack(side=TOP)
Button(frame,text="A",font=('consolas',25),width=3).pack(side=LEFT)
Button(frame,text="S",font=('consolas',25),width=3).pack(side=LEFT)
Button(frame,text="D",font=('consolas',25),width=3).pack(side=LEFT)

window.mainloop()
'''
#windows
'''
from tkinter import *
def create_window():
    new_window = Toplevel()# Toplevel():new window ' on top' of other windows linked to a 'bottom' window not like  Tk():new independent window
    old_window.destroy()#close out of old window
old_window = Tk()

Button(old_window,text="create new window",command=create_window).pack()

old_window.mainloop()
'''
# tabs
'''
from tkinter import *
from tkinter import ttk

window = Tk()
notebook = ttk.Notebook(window)# a widget that manages a collection of windows /displays

tab1 = Frame(notebook)#new frame for tab1
tab2 = Frame(notebook)#new frame for tab2

notebook.add(tab1,text="Tab 1")
notebook.add(tab2,text="Tab 2")
notebook.pack(expand=True,fill="both")# expand to fill  any space not otherwise
                                      #fill: fill space on x and y axis


Label(tab1,text="Hello,this  is tab1",width=50,height=25).pack()
Label(tab2,text="Goodbye,this  is tab2",width=50,height=25).pack()



window.mainloop()
'''
# grid
'''
from tkinter import *
#grid() = geometry manager that organizes widgets in a table-like structure in a parent  container

window = Tk()
titleLabel = Label(window,text="enter your info",font=("Arial",25)).grid(row=0,column=0,columnspan=2)
firstNameLabel = Label(window,text="First Name: ",width=20,bg="red").grid(row=1,column=0)
firstNameEntry = Entry(window).grid(row=0,column=1)

lastNameLabel = Label(window,text="Last Name: ",bg="green").grid(row=2,column=0)
lastNameEntry = Entry(window).grid(row=1,column=1)

emailNameLabel = Label(window,text="email: ",bg="blue",width=30).grid(row=3,column=0)
emailNameEntry = Entry(window).grid(row=2,column=1)

submitButton = Button(window,text="Submit").grid(row=4,column=0,columnspan=2)

window.mainloop()

'''
# progress bar
'''
from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 50
    download = 0
    speed = 2
    while (download<GB):
        time.sleep(0.05)
        bar['value'] += (speed/GB)*100
        download+=speed
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+"/"+str(GB)+" GB completed")

        window.update_idletasks()



window = Tk()
percent = StringVar()
text = StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

percentLabel = Label(window,textvariable=percent).pack()
taskLabel = Label(window,textvariable=text).pack()

button = Button(window,text="download",command=start).pack()


window.mainloop()
'''
# canvas = widget that is used to draw graphs, plots,images in a window
'''
from tkinter import *
window = Tk()

canvas = Canvas(window,width=500,height=500)
#blueLine = canvas.create_line(0,0,500,500,fill="blue",width=5)
#redLine = canvas.create_line(0,500,500,0,fill="red",width=5)
#canvas.create_rectangle(50,50,250,250,fill="purple")
#points = [250,0,500,500,0,500]
#canvas.create_polygon(250,0,500,500,0,500,fill="yellow",outline="black",width=5)
#canvas.create_arc(0,0,500,500,fill="green",style=PIESLICE,start=180,extent=180,width=5)

canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)
canvas.create_oval(190,190,310,310,fill="white",width=10)

canvas.pack()

window.mainloop()
'''
# key events
'''
from tkinter import *
def dosomething(event):
    #print("you pressed: "+event.keysym)
    label.config(text=event.keysym)
window= Tk()

window.bind("<Key>",dosomething)# press any key and then calls the function
label = Label(window,font=("Helvetica",100))
label.pack()
window.mainloop()
'''
# mouse events
'''
from tkinter import *

def dosomething(event):
    print("Mouse coordinates: "+str(event.x)+","+str(event.y))

window = Tk()

window.bind("<Button-1>",dosomething)# left mouse click
window.bind("<Button-2>",dosomething)#scroll wheel
window.bind("<Button-3>",dosomething)# right mouse click
window.bind("<ButtonRelease>",dosomething)
window.bind("<Enter>",dosomething)# enter the window
window.bind("<Leave>",dosomething)# leave the window
window.bind("<Motion>",dosomething)# where the mouse moved

window.mainloop()
'''
# drop & drag widgets
'''
from tkinter import *

window = Tk()
def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)

label = Label(window,bg="red",width=10,height=5)
label.place(x=0,y=0)


label2 = Label(window,bg="blue",width=10,height=5)
label2.place(x=100,y=100)

label.bind("<Button-1>",drag_start)
label.bind("<B1-Motion>",drag_motion)

label2.bind("<Button-1>",drag_start)
label2.bind("<B1-Motion>",drag_motion)

window.mainloop()
'''
# moving images /keys
'''
from tkinter import *
def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-10)

def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+10)

def move_left(event):
    label.place(x=label.winfo_x()-10, y=label.winfo_y())

def move_right(event):
    label.place(x=label.winfo_x()+10, y=label.winfo_y())

window = Tk()

window.geometry("500x500")

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)

window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)

myimage = PhotoImage(file='python.png')
label = Label(window,image=myimage,bg='black')
label.place(x=0,y=0)

window.mainloop()
'''
# moving image in a canvas
'''
from tkinter import *

def move_up(event):
    canvas.move(myimage,0,-10)
def move_down(event):
    canvas.move(myimage, 0,10)
def move_left(event):
    canvas.move(myimage, -10, 0)
def move_right(event):
    canvas.move(myimage, 10, 0)
window = Tk()

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)

window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)

canvas = Canvas(window,width=500,height=500)
canvas.pack()

photoimage = PhotoImage(file='python.png')
myimage = canvas.create_image(0,0,image=photoimage,anchor=NW)

window.mainloop()
'''
# 2D animation
'''
from tkinter import *
import time

WIDTH = 500
HEIGHT = 500


xVelocity = 3
yVelocity = 2

window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

bg_photo = PhotoImage(file='space2.jpeg')
background = canvas.create_image(0,0,image=bg_photo,anchor=NW)

photo_image = PhotoImage(file='ufo (2).png')
my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)

image_width = photo_image.width()
image_height = photo_image.height()
while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if(coordinates[0]>=WIDTH-image_width or coordinates[0]<0):
        xVelocity = -xVelocity

    if (coordinates[1] >= HEIGHT-image_height or coordinates[1] < 0):
        yVelocity = -yVelocity

    canvas.move(my_image,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)



window.mainloop()
'''
# multiple animations
'''
from tkinter import *
from ball import *
import time

window = Tk()

WIDTH = 500
HEIGTH = 500

canvas = Canvas(window,width=WIDTH,height=HEIGTH)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,1,1,"white")
tennis_ball = Ball(canvas,0,0,50,4,3,"yellow")
basket_ball = Ball(canvas,0,0,125,8,7,"orange")

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()
'''
#*******************************************
# run .py file with cmd(terminal)
#*******************************************
# save file as .py (Python file)
# go to xommand prompt
# navigate to directory w/ your file: cd C:\Users\dell\PycharmProjects\pyfad\main.py
# invoke python interpreter + script: python main.py
'''
print("hello world!")
name  = input("what is your name? :")
print("Hello "+name)
'''
#***********************************************************
# Python pip
#************************************************************
#pip : package manager for packaes and modules from Python Package Index
#    included for Python versions 3.4+
#    open command prompt

#    help:                    pip
#    check:                   pip --version
#    update:                  pip install --upgrade pip
#    installed packages:      pip list
#    check outdated packages: pip list --outdated# outdated pas mise a jour
#    install a package:       pip install "package name"
#************************************************************
# py o exe file
'''
(windows Defender may prevent you from running)
(make sure pip and pyinstaller are installed/updated)

cd to directory that contains your .py file
pyinstaller ...
              -F  (all in 1 file)
              -w  (removes terminal window)
              -i icon.ico (adds custom icon to exe.)
              clock.py (name of your main python file)
              
.exe is located in the dist folder



'''


































































