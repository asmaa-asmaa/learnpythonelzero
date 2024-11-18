#print("i love programming") # this is comment
# this comment
#print("i love laaab")
#print(10)
#print(type(10))
#print(type(-50))
#print(type(100.3))
#print(type('i love python'))
#print(type([1,2,3,4]))
#print(type((1,2,3,4)))
#print(type({"one": 1, "two": 2}))
#print(2==2)
#print(2==4)
#print(type(2==2))

#variable = "value"
#print(variable)
#help("keywords")
#a,b,c=1,2,3
#print(a)
#print(b)
#print(c)

#print("hello\b world")
#print("hello \
#new \
#world")
#print("i love test\\")
#print("i love 'test'")
#print("i love \"test\"")
#print("i love\n test")
#print("123456\rabcd")
#print("love\tpython")
#print("\x4f\x70")

#msg= "hello"
#two= "python"
#print(msg + " " + two)
#print(msg + " \n" + two)

#name="asmaa"
#age="33"
#country="egypt"
#print("\"name:" +" "+ name + "\""+ "\n" +"\"age:" +" "+ age + "\"" +"\n"+ "\"country:" +" "+ country + "\"")
#print( type(name))

#myString= """first
#second "test" 'test'
#third"""
#myScostring='''first
#second 'test'\\ "test"\
#third'''
#mythstring= "first\nsecond\nthird"
#print(myString)
#print(myScostring)
#print(mythstring)

#strin="i love python"

#print(strin[1])
#print(strin[-1])
#print(strin[0 : 4])
#print(strin[:8])
#print(strin[8:])
#print(strin[:])
#print(strin[0::1])
#print(strin[::1])
#print(strin[::2])
#print(strin[::3])

#print(len(strin))



#a="  i love python  "
#print(a.strip())
#print(a.rstrip())
#print(a.lstrip())
#b="@#we love prog@#@#@#"
#print(b.strip("@#"))
#print(b.rstrip("@#"))
#print(b.lstrip("@#"))

#c="i love 3d technology and ai"
#print(c.title())
#print(c.capitalize())
#print(c.upper())
#print(c.lower())

#k="i love python and php"
#print(k.split())
#l="i-love-python-and-php"
#print(l.split("-"))
#print(l.split("-",2))
#print(l.split("-", 3))
#print(l.rsplit("-", 3))

#v= "asmaa"
#print(v.center(9))
#print(v.center(9,"#"))

#g="i love python and php because php is easy"
#print(g.count("php"))
#print(g.count("php",0,25))

#i="hello world"
#s="HELLO WORLD"
#print(i.swapcase())
#print(s.swapcase())

#print(i.startswith("h"))
#print(i.startswith("H"))
#print(i.startswith("w",6,10))

#print(i.endswith("d"))
#print(i.endswith("o",0,5))

#print(i.index("h", 1,5)) error

#print(i.find("h", 5,8))

#w="asmaa"
#print(w.rjust(10))
#print(w.rjust(10, "#"))

#print(w.ljust(10))
#print(w.ljust(10, "#"))

#x="""firstline
#secondline
#thirdline"""
#print(x.splitlines())
#print(x.split())

#h="hello\tnew\tworld"
#print(h.expandtabs(5))


#d,e,f="1","11","111"

#print(d.zfill(3))
#print(e.zfill(3))
#print(f.zfill(3))

#m="hello New World"
#print(m.istitle())
#print(m.islower())

#j=" "
#print(j.isspace())

#n="asmaa_front"
#z="asmaaFront"
#p="asmaa--front"
#print(n.isidentifier())
#print(z.isidentifier())
#print(p.isidentifier())

#n="abbbbbc"
#z="assss999"
#p="999999"
#print(n.isalpha())
#print(z.isalpha())
#print(p.isalpha())
#print(n.isalnum())
#print(z.isalnum())
#print(p.isalnum())

#a="hello one two three one one"
#print(a.replace("one", "1"))
#print(a.replace("one", "1",1))

#myList=["asmaa","mahmoud","fahmy"]
#print("-".join(myList))

#name ="asmaa"
#age=25
#rank=10
#print("my name is: %s and my age is: %d and my rank is %f" % (name, age, rank))
#print(" my rank is %.1f" % rank)
#print("my name is: {} and my age is {} and my rank is {}" .format(name, age, rank))
#print("my name is: {:s} and my age is {:d} and my rank is {:f}" .format(name, age, rank))
#print("my name is: {:.3s} and my age is {:d} and my rank is {:.2f}" .format(name, age, rank))


#longMessage="hello my clients provide an amazing service developing websites"
#print("message is: %.5s" % longMessage)

#money=567890234987
#print("money is {:_d}".format(money))
#print("money is {:,d}".format(money))

#a,b,c="one","two","three"
#print("hello {} {} {}".format(a,b,c))
#print("hello {1} {2} {0}".format(a,b,c))
#print("hello {} {} {}".format(b,c,a))

#s,d,f = 10,20,30
#print("{1: .2f} {2: .3f} {0: .4f}".format(s,d,f))

#name="asmaa"
#age="25"
#print(f"my name is {name}, my age is {age}")

#name="asmaa"
#age="25"
#country="egypt"

#print("\"hello \'"+ name +"\', how you doing \\ \"\"\" your age is \""+ age+ "\"\" + and your country is: "+ country)

#print(f"\"hello \'{name} \', how you doing \\\n\"\"\" your age is \"{age}\"\" +\nand your country is: {country}")

#name="Elzero"
#print(name[1 : 4])
#print(name[0 : : 2])
#print(f"{name[-2]}{name[-4]}{name[-6]}")
#print(name[-2]+ name[-4]+ name[-6])

#name= "#@#@Elzero#@#@"
#print(name.strip("#@"))

#name="i <3 python and although <3 elzero web school"
#name_two="Elzero"
#print(name.replace("<3", "love"))
#print(name_two.index("z"))


#complexNumber=5+6j

#print(type(5+6j))
#print("real part is: {}".format(complexNumber.real))
#print("imaginary part is: {}".format(complexNumber.imag))
#print(100)
#print(float(100))
#print(complex(100))
#print(10.50)
#print(int(10.50))
#print(complex(10.50))

#print(-30 - -20)
#print(5 + 10 * 1000) #10005 bydrab ba3deen yagm3
#print((5+10)*100)

#print(100/20)
#print(int(100/20))

#print(8% 2) #0
#print(9 % 2) # 1  ba2ee el 2asma

#print(2 ** 5) # 2*2*2*2*2 ...exponent oos

#print(100// 20)
#print(110//20) #floor division

#myList = ['one',"two","one",1, 100.5, True]
#myList[1]=2
#print(myList)
#myList[0:3]=[]
#print(myList)
#myList[0:3]=["a","b","c"]
#print(myList)
#myList[0:3]=["a"]
#print(myList)

#friends=["asmaa","mahmoud","yasmin"]
#friends.append("eman")
#print(friends)
#oldFr=["lama","tala"]
#friends.append(oldFr)

#print(friends)
#print(friends[4])
#print(friends[4][1])

#a=[1,2,3,4]
#b=["a","b","c"]
#c=["one","two"]
#a.extend(b)
#a.extend(c)
#print(a)

#x= [1, 2, 3, 4, 'a', 'b', 'c', 'one', 'two',"one"]
#x.remove("one")
#print(x)

#y=[1,3,2,-1,100,30,-2]
#y.sort()
#print(y)
#y.sort(reverse=True)
#print(y)

#z=[10,1,80,100,"asmaa",100]
#z.reverse()
#print(z)

#a=[1,2,3,4]
#a.clear()
#print(a)

#a=[1,2,3,4]
#b=a.copy()
#a.append(5)
#print(a)
#print(b)

#a=[1,2,3,1,2,1]
#print(a.count(1))

#e=['a',"b","c","d","c"]
#print(e.index("c"))
#e.insert(0, "as")
#print(e)
#e.insert(-1,"test")
#print(e)

#a=[1,2,3,4,"a","b"]
#print(a.pop(0))

#myTupleO=("asmaa","mahmoud")
#myTupleT="asmaa","mahmoud"
#print(myTupleO)
#print(myTupleT)
#myTupleThree=(1,2,3,4,5)
#print(myTupleThree[0])

#aTuple=("as",1,True,"hello")

#a=("asmaa")
#b="asmaa"
#print(type(a))
#print(type(b))

#c=("asmaa",)
#f="asmaa",
#print(type(c))
#print(type(f))
#print(len(c))

#a=(1,2,3,4)
#b=(5,6)
#c= a + b
#print(c)
#d=a+(7,8)+b
#print(d)
#print(a*2)
#print(b*3)

#f=(1,2,3,4,5,1,2,1)
#print(f.count(1))
#print(f.index(3))
#print("the position of index is: {:d}".format(f.index(3)))
#print(f"the position of index is: {f.index(3)}")

#a=("a","b","c")
#x,y,z=a
#print(x)
#print(y)
#print(z)

#a=("a","b",1,"c")
#x,y,_,z=a
#print(x)
#print(y)
#print(z)

#ttuple=("osama",2,3,4)
#llist=list(ttuple)
#llist[0]="elzero"
#neTuple=tuple(llist)
#print(neTuple)

#mySet = {"asmaa","ali",100}
#print(mySet)
#mySetTwo= {"asmaa",1,2,"asmaa",1,3}
#print(mySetTwo)
#mySetTwo.clear()
#print(mySetTwo)

#setOne={"one","two","three"}
#setTwo={1,2,3}
#b={"5","6"}
#print(setOne|setTwo)
#print(setOne.union(setTwo,b))

#b.add("four")
#print(b)

#f=b.copy()
#print(f)
#b.remove("5")
#print(b)



#c={1,2,3,4}
#c.discard(4)
#print(c)
#print(c.pop())

#a={1,2,3}
#b={"a","b","c",1}
#a.update(b)
#print(a)
#a.update(["html","css"])
#print(a)

#from functools import reduce


#a={1,2,3,4}
#b={1,2,"a","b"}
#c={1,2,3}
#print(a.difference(b))
#print(a-b)
#print(a)
#print("#"*10) #separator
#a.difference_update(b)
#print(a)
#print("#"*10) #separator
#print(a.intersection(b))
#print(a&b)
#a.intersection_update(b)
#print(a)
#print("#"*10) #separator
#print(a.symmetric_difference(b))
#print(a^b)
#a.symmetric_difference_update(b)
#print(a)
#print("#"*10) #separator
#print(a.issuperset(c))
#print(a.issubset(c))
#print(a.isdisjoint(c))


#user={
 #   "name":"asmaa",
  #  "age":33,
   # "country":"egypt",
    #"skills": ["html","css","js"],
    #"rating":10.5,
#}
#print(user)
#print(user["country"])
#print(user.get("country"))
#print(user.keys())
#print(user.values())

# langs= {
#     "one": {
#         "name":"html",
#         "progress":"99%"
#     },
#     "two": {
#         "name":"css",
#         "progress":"98%"
#     },
    
# "three": {
#         "name":"js",
#         "progress":"97%"
#     },
# }
# print(langs)
# print(langs["one"])
# print(langs["one"]["progress"])
# print(len(langs))
# print(len(langs["one"]))


# frameOne= {
#     "name":"vuejs",
#     "progress":"99%"
# }
# frameTwo= {
#     "name":"reactjs",
#     "progress":"80%"
# }
# frameThree= {
#     "name":"angular",
#     "progress":"80%"
# }

# allFramework= {
#     "one": frameOne,
#     "two": frameTwo,
#     "three": frameThree,
# }
# print(allFramework)

#user= {
    #"name": "asmaa"
#}
#user.clear()
#user["age"]= 36
#user.update({"country": "egypt"})
#print(user)
#b=user.copy()
#print(b)
#print("#"*10)
#print(user.setdefault("name","ali"))
#print(user.setdefault("age",33))
#print(user)
#print(user.setdefault("country"))
#print(user)

# member= {
#     "name":"taha",
#     "skill":"js"
# }
#member.update({"age":10})
#print(member.popitem())
#print("#"*10)

# allMembers=member.items()
# member["age"]= 10
# print(allMembers)

#a=("keyOne","keyTwo","keyThree")
#b="x"
#print(dict.fromkeys(a,b))

#skills= {
 #   "html progress is": "98%", 
  #  "css progress is": "97%",
   # "js progress is": "99%",   
#}
#for key, value in skills.items():
#print(f"{key}: {value}")
#a=skills.items()
#x,y,z = a
#print(x)
#print(y)
#print(z)

# name=" "
# print(name.isspace())
# print(100>200)
# print(bool("asmaa"))
# print(bool(100))
# print(bool(10.50))
# print(bool(True))
# print(bool([1,2,3]))
# print(bool(" "))

# print(bool(0))
# print(bool(""))
# print(bool([]))
# print(bool(False))
# print(bool(None))


#age = 33
#country="egypt"
#rank= 10
#print(country == "egypt")
#print(age > 16 and country == "egypt" and rank>0)
#print(age > 16 or country == "jordan" or rank>0)
#print(not age >16)

#x= 10
#y= 20
#z= x + y
#print(z)
#x=x+y
#print(x)
#y+=x
#print(y)
#x=x-y
#x-=y
#print(x)

#print(100 == 100)
#print(100 == 100.0)

#print(100 != 100)
#print(100 != 100.00)

#print(100>=100)
#print(100>=50)
#print(100<=50)

#a=10
#print(type(a))
#print(type(str(a)))

#c="asmaa"
#d=[1,2,3,4,5]
#e={"a","b","c"}
#f={"d": 1, "e":2, "f": 3}
#print(tuple(c))
#print(tuple(d))
#print(tuple(e))
#print(tuple(f))

#c="asmaa"
#d=(1,2,3,4,5)
#e={"a","b","c"}
#f={"d": 1, "e":2, "f": 3}
#print(list(c))
#print(list(d))
#print(list(e))
#print(list(f))

#c="asmaa"
#d=[1,2,3,4,5]
#e=("a","b","c")
#f={"d": 1, "e":2, "f": 3}

#print(set(c))
#print(set(d))
#print(set(e))
#print(set(f))

#d=[["a",1],["b",2]]
#e=(("a",1),("b",2))

#print(dict(d))
#print(dict(e))

#fName= input("what is your first name")
#mName= input("what is your middle name")
#lName= input("what is your last name")
#fName=fName.strip().capitalize()
#mName=mName.strip().capitalize()
#lName=lName.strip().capitalize()

#print(f"hello {fName} {mName:.1s} {lName} happy to see you")



#fName= input('what\'s your first name ?').strip().capitalize()
#yrMail= input("what is your email ?").strip()

#userNa=yrMail[0: yrMail.index("@")].strip()
#domain=yrMail[yrMail.index("@")+1 :].strip()

#print(f"hello {fName} yor mail is {yrMail}")
#print(f" your username is {userNa} \n your domain is {domain}")


#age = int(input("what is your age ?"))
#months= age*12
#weeks=months*4
#days=age*365
#hours= days*24
#minutes=hours*60
#seconds=minutes*60

#print(f"your age is {age}")
#print(f"months: {months}")
#print(f"weeks: {weeks:,}")
#print(f"days: {days:,}")
#print(f"hours: {hours:,}")
#print(f"minutes: {minutes:,}")
#print(f"seconds: {seconds:,}")

#html= input("your emil is :").strip().lower()
#css= html[:html.index('@')]
#print(f"hello {css.capitalize()}")

#name="asmaa"
#country="egypt"
#price= 100
#isStudent="yes"

#if country == "egypt" or country ==  "qatar": 
   #print(f"hello {name} the price is {price - 80}")
   #if isStudent == "yes":
           #print(f"hello {name} price is {price - 90}")
   #else: 
            #print(f"hello {name} the price is {price - 80}")
#elif country=="lebnon" :
    #print(f"hello {name} the price is {price - 70}")   
#else:
    #print(f"hello {name} the price is {price - 20}")    
     
#moverule= 18
#age= 18
#print("movie is suitable for you" if age >= moverule else "movie is not suitable for you")

#print("#"*80)
#print("please choose unit you can write first letter or fullname".center(80,"#"))
#print("#"*80)

#age= input("please write age").strip()
#unit=input("please choose unit: months, weeks,days").strip().lower()

#months=int(age)*12
#weeks=months*4
#days=int(age)*365

#if unit == "months" or unit == "m":
    #print(f"your age in units is {months}")
#elif unit == "weeks" or unit == "w":
     #print(f"your age in units is {weeks:,}")
#elif unit == "days" or unit == "d":
     #print(f"your age in units is {days:,}")

#admins=["asmaa","mahmoud","ali"]

#name=input("write your name").strip().lower()

#if name in admins:
    
 #   print(f"hello {name} you are an admin")
  #  option = input('do you want to delete or update').strip().lower()

   # if option == "delete":
    #    admins.remove(name)
     #   print('deleted')
      #  print(admins)
    #elif option == "update":
     #   newN= input("write new name").strip().lower()
      #  admins[admins.index(name)] = newN
       # print("updated")
        #print(admins)
#elif name not in admins:
 #   print("you are not admin")
  #  op=input('do you need to add you y or n').strip().lower()
   # if op == "y" or op == "yes":
    #    admins.append(name)
     #   print("added")
      #  print(admins)
    #elif op == "n" or op == "no":
     #   print("not added")
      #  print(admins)    
    #else:
     #   print("wrong option")

#a= 0
#while a < 15:
 #   print(a)
  #  a += 1
#print("loop done")  

#while False:

 #print("no thing")

#friends=["asmaa","soha","alia","ali","huda"] 

#a = 0
#while a < len(friends):

 #   print(f"#{str (a + 1).zfill(2)} {friends[a]}")
  #  a += 1
#else:
 #   print("friends printed") 


  

#myFav=[]
#maxFav= 5
#while maxFav > 0:
 #   fav=input("write the fav without https://")
  #  myFav.append(f"https://{fav.strip().lower()}")
   # maxFav-=1
    #print(f"fav added,{maxFav} places left")
  #  print(myFav)
#else:
 #   print("bookmark is full, you can not add more")   
#if len(myFav)>0:
 #   myFav.sort()
  #  index=0
   # print("printing the list")
    #while index< len(myFav):
     #   print(myFav[index])
      #  index+=1


#tries= 4
#coPas= "9999"

#pas=input("write password").strip()

#while pas != coPas:
#     tries -= 1 
 #    print(f"pass wrong,{'last' if tries == 1 else tries} chance lefted")
  #   pas=input("write password").strip()
   #  if tries == 1:
    #      print("contact callcenter to reset password")
     #     break
#else:
      
 #    print("password correct") 
             

#umbers=[1,2,3,4]

#for num in numbers:
 #   if num % 2 == 0:
  #      print(f"{num} is even")
   # else:
    #    print(f"{num} is odd")
#else:
#    print("loop finished")



#myRange= range(1, 50)
#for ra in myRange:
 #   print(ra)

#mySkills= {
 #   "html": "99%",
  #  "css": "98%",
   # "js": "97%",
    #"vujs": "96%",
    #"python": "100%"
#}

#for skill in mySkills:
 #   print(f"{skill} progress is: {mySkills[skill]}")


#people= {
 # "asmaa": {
  #"html": "99%",
   #"css": "98%"
  #}, 
  #"ali": {
   #"html": "100%",
   #"css": "96%"
  #}
 #}

#for per in people:
 #   print(per)
  #  for skill in people[per]:
   #     print(f"{skill}: {people[per][skill]}")

#for per_key , per_value in people.items(): # tare2a tanya ashl mn elly fo2
 #   print(per_key)
  #  for skill_key, skill_value in per_value.items():
   #     print(f"-{skill_key} : {skill_value}")
#nums=[1,2,3,4,5]
#for num in nums:
    #if num == 3:
     #   continue
    #if num == 3:
     #     break
    #print(num)
    #print(num)
    #if num == 3:
     # break
 #    if num == 3:
  #        pass
   #  print (num)     





#def function_name():
 #   print("hello")
#function_name()    
#def function_two():
 #   return("hi")
#print(function_two())
#def function_three():
 #   return("hey")
#three = function_three()
#print(three)

#a,b,c=100,50,25

#def addition(n1,n2,n3):
 #   if type(n1) != int or type(n2) != int or type(n3) != int:
  #      print("only integer allowed")
   # else:    
    #     print(f"hello {n1 + n2 + n3}")
#addition(a,b,c)


#def fullName(f,m,l):
 #   return(f"hello {f.strip().capitalize()} {m.upper():.1s} {l}")

#print(fullName("asmaa","mohamed","hussanin"))

#def hello(name, *skills): # * esmaha unpack
 #       print(f"hello {name}, your skills are: ")
  #      for skill in skills:
   #       print(f"-{skill}")
#hello("Asmaa","html","css","js","vuejs","python")

#sskills={
 # "vuejs":"90%",
  # "python": "100%"
#}
#def dicFun(name,**skills):
 #   print(f"hello {name}, your skills are:")
  #  for key , value in skills.items():
   #   #print(type(skills))
    #  print(f"{key} => {value}")
#dicFun("asmaa", html= "90%", css= "99%", js= "100%")    
#dicFun("ali", **sskills)      

#def nn(name="unknown", age="unknown",country="unkown"):
 #   print(f"hello {name} age is {age} country is {country}")
#nn("asmaa", "33")    

#x=0
#def localFun():
 #   x=1
  #  print(f"fromlocal one {x}")
#localFun()

#def localFunt():
 #   global x
  #  x=2
   # print(f"fromlocal one {x}")
#localFunt()

#def localFunth():
 #   print(f"fromlocal one {x}")
#localFunth()
#print(f"hello from global {x}")



#def cleanWord(word):
 #   if len(word) == 1:
  #      return(word)
   # if word[0] == word[1]:
    #    return cleanWord(word[1:])
    #return word[0] + cleanWord(word[1:])
#print(cleanWord('wwwooorldd'))

#hello= lambda name, age : f"hello {name}, your age is {age}" #lambda function zay el anoynoums function fi js mn 3'er asm
#print(hello("asmaa","33"))


#import os
#print(os.getcwd())
#file = open("asmaaa.txt") # 3shan hwa msh fi el current working directory
#file = open("asmaa.txt") # current directory
#file = open(r"C:\Users\Public\learnpython\asmaaa.txt")
#print(os.path.abspath(__file__))
#print(os.path.dirname(os.path.abspath(__file__)))
#os.chdir(os.path.dirname(os.path.abspath(__file__)))
#print(os.getcwd())

#myFile= open(r"C:\Users\Public\learnpython\asmaaa.txt","r")
#print(myFile)
#print(myFile.name)
#print(myFile.mode)
#print(myFile.encoding)

#print(myFile.read())
#print(myFile.read(5))
#print(myFile.readline())
#print(myFile.readline(8))
#print(myFile.readlines())
#print(type(myFile.readlines()))

#for line in myFile:
    

 #   print(line)
  #  if line.startswith("1"):
   #     break

#mFile= open(r"C:\Users\Public\learnpython\new.txt","w")
#print(mFile.write("hello asmaa\n"))
#print(mFile.write("second line\n"))

#mylist =["asmaa\n","ali\n","amir\n"]
#print(mFile.writelines(mylist *2))

#mFile= open(r"C:\Users\Public\learnpython\new.txt","a")
#print(mFile.write(" what do you think\n"))
#print(mFile.write("append second line\n"))

#mylist =["asmaa\n","ali\n","amir\n"]
#print(mFile.writelines(mylist))
#print(mFile.write("\nappend last line"))

#mFile= open(r"C:\Users\Public\learnpython\new.txt","r")
#print(mFile.truncate(8)) # file mode append
#print(mFile.tell())
#print(mFile.seek(7))
#print(mFile.read())

#mFile= open(r"C:\Users\Public\learnpython\nnew.txt","a")
#import os
#os.remove(r"C:\Users\Public\learnpython\nnew.txt")



#import os
#os.chdir(r"Desktop")
#os.mkdir("ass")
#for file in range(1,51):
    
 #myfile= open(rf"C:\Users\zoom\Desktop\ass\txt{file}.txt","r")
 #print(myfile.name)
 #print(myfile.write("hello world\n"*30))
 #print(len(myfile.readlines()))
 #print(len(file.read()))
 
#delll= (os.listdir(r"C:\Users\zoom\Desktop\ass")[1:31])
#print(delll)
#for dd in delll:
 #os.remove(rf"C:\Users\zoom\Desktop\ass\{dd}")



#os.rename(r"C:\Users\zoom\Desktop\ass\txt25.txt", r"C:\Users\zoom\Desktop\ass\zero.txt")


#myfile= open(r"C:\Users\zoom\Desktop\ass\elzero.txt", "w")
#myfile.write("hello world hello")

#myfile= open(r"C:\Users\zoom\Desktop\ass\elzero.txt", "r")
# print(len(myfile.read().split()))
#print(myfile.read().lower().count("l"))


#x=[1,2,3,4]
#if all(x):
 #   print("all elements are true")
#y=[1,2,3,4,[]]
#if all(y):
 #   print("all elements are true")
#else:
 #   print("there is at leat element false") 

#z=[1,2,3,4,[]]
#if any(z):
 #   print("there is at least one element is true")
#else:
 #   print("all elements are false")  
#print(bin(100))  # 2a7wlo l lo3'a el computer byfhamha    

#a =1
#b =2
#print(id(a))  
#print(id(b))          

#a=[1,2,3]
#print(sum(a))
#print(sum(a,6))

#print(round(100.500))
#print(round(100.501))
#print(round(100.400))
#print(round(100.555, 2))
#print(round(100.5432,2))

#print(list(range(0)))
#print(list(range(10)))
#print(list(range(1,10)))
#print(list(range(0,20,2)))

#print("hello asmaa how are you")
#print("hello","asmaa","how","are","you")
#print("hello","asmaa","how","are","you", sep="|")

#print("first line", end=" ")
#print("second line")

#print(abs(100)) # 100
#print(abs(-100)) # 100
#print(abs(-10.19)) # 10.19

#print(min(1,2,3,4))
#print(max(1,2,3,4))
#print(min("a","b","osama"))
#print(max("a","b","osama"))

#print(pow(2,5)) # 2*2*2*2*2
#print(pow(2,5,10)) # 2*2*2*2*2 % 10

#a=['a',"b","c","d","f"]
#print(a[slice(3)]) # slice zai [:]
#print(a[slice(1,3)])
#print(a[slice(0,5,2)]) # 2amshy 7'atwateen


#my_list =[True, 1,1 ,["a","b"],10.5, 0]  
#if all(my_list[:4]): # 
 #   print("good")  
#else:
 #   print("bad")    

#if  all(my_list[:]): # 
 #   print("good")  
#else:
 #   print("bad")   
  


     

      
#def my_all(iterable): #function instead all function
 #   for element in iterable:
  #      if not element:
   #         return False
    
    #return True
        
#print(my_all([1,2,3,[]]))    
#print(my_all([1,2,3]))     

#def my_any(iterable):
 #   for element in iterable:
  #      if element:
   #         return True
            
    
    #return False
        
#print(my_any([0,1,2,3,[]]))    
#print(my_any([(),0]))  


#def my_min(iterable):
 #   iterator = iter(iterable)
  #  min_value = next(iterator)
   # for element in iterator:

    #    if element < min_value:
     #        min_value = element
    #return min_value    
    
        
#print(my_min([1,2,3,4,5]))    
#print(my_min((1,2,3,4,5)))    


#def my_max(iterable):
 #   iterator = iter(iterable)
  #  max_value = next(iterator)
   # for element in iterator:

    #    if element > max_value:
     #        max_value = element
    #return max_value    
    
        
#print(my_max([1,2,3,4,5]))    
#print(my_max((1,2,3,4,5)))  

#def formatText(text):
 #   return f"- {text.strip().capitalize()} -"

#myText=["asmaa","ali","tamer"]
#myformatData=map(formatText, myText)
#for name in myformatData:
 #   print(name)
#print("#"*6)   
#for name in map(formatText, myText):
 #   print(name)
#print("#"*6)   
#for name in list(map(formatText, myText)):
 #   print(name)
#print("#" * 6)
#for name in map( lambda text: f"- {text.strip().capitalize()} -", myText):
 #   print(name)


#def formatNames(name):
 #   return name.startswith("a")

#myNames=["asmaa","ali","tamer","soha","tammara"]
#myformatNames=filter(formatNames, myNames)
#for name in myformatNames:
    #print(name)
#print("#"*6)   
#for name in filter(formatNames, myNames):
 #  print(name)
#print("#"*6)   
#for name in list(filter(formatNames, myNames)):
 #  print(name)
#print("#" * 6)
#for name in filter( lambda name : name.startswith("t"), myNames):
   # print(name)
#numbers=[0,1,2,3,4,5,0]
#for num in filter( lambda number : number == 0, numbers):
# print(num)

#def sumNums(num1,num2):
 #   return num1+num2
#nums=[1,2,3]
#result= reduce(sumNums, nums)
#print(result)

#result= reduce(lambda num1, num2 : num1+num2, nums)
#print(result)

#skills=["html","css","js"]
#for skill in enumerate(skills):
 #   print(skill)
#for count, skill in enumerate(skills,1):
 #   print(f"{count}: {skill}")  


#print(reversed(skills))
#print(type(reversed(skills)))

#for skill in reversed(skills):
 #   print(skill)    

#string= "asmaa"
#for letter in reversed(string):
 #   print(letter)

#print(help(print))

#import random

#print(f"random float number: {random.random()}")

#print(dir(random))

#from random import random , randint

#print(f"float number: {random()}")
#print(f"random integer number: {randint(100, 900)}")

#import sys
#print(sys.path)

#sys.path.append(r"c:\hello")
#print(sys.path)

#import asmmodule
#print(dir(asmmodule))

#asmmodule.sayHello("asmaa")
#asmmodule.sayHello("ali")
#asmmodule.sayHowareyou("asmaa")
#asmmodule.sayHowareyou("ali")

#import asmmodule as asm # alis

#asm.sayHello("asmaa")

#from asmmodule import sayHello
#sayHello("smsm")

#from asmmodule import sayHello as say # alis
#say("samase")

#import termcolor
#import pyfiglet
#from colorama import init, Fore
#init(autoreset=True)
#print(Fore.RED + (pyfiglet.figlet_format("asmaa")))
#print(dir(termcolor))
#print(dir(pyfiglet))
#print(pyfiglet.figlet_format("asmaa"))
#print(termcolor.colored("asmaa", color="green"))


#from random import randint
#print(f"\"random even number between 1-10 => \" \"{randint(1, 5)* 2}\"")

#print(f"\"random odd number between 1-9 => \" \"{randint(1, 5)* 2 - 1}\"")

#import datetime
#print(dir(datetime))
#print(dir(datetime.datetime))

#print(datetime.datetime.now())
#print(datetime.datetime.now().year)
#print(datetime.datetime.now().month)
#print(datetime.datetime.now().day)

#print(datetime.datetime.min)
#print(datetime.datetime.max)

#print(datetime.datetime.now().time())
#print(datetime.datetime.now().time().hour)
#print(datetime.datetime.now().time().minute)
#print(datetime.datetime.now().time().second)

#print(datetime.time.min)
#print(datetime.time.max)

#myBirthDay = datetime.datetime(2000, 5, 3)
#currentDate = datetime.datetime.now()

#print(f"i lived for {currentDate - myBirthDay}")
#print(f"i lived for {(currentDate - myBirthDay).days} days")

#import datetime

#myBirth = datetime.datetime(2000, 4 ,5) #python strftime directive
#print(myBirth.strftime("%a"))
#print(myBirth.strftime("%A"))
#print(myBirth.strftime("%b"))
#print(myBirth.strftime("%B"))
#print(myBirth.strftime("%y"))
#print(myBirth.strftime("%Y"))
#print(myBirth.strftime("%A/ %B/%Y"))


#myString = "asmaa" #iterable 7aga tanf3 yat3ml 3aliha loop
#print(next(myString))

#myIterator = iter(myString) # iterator
#print(next(myIterator))
#print(next(myIterator))

#for letter in myString: # for bt7awl mystring la iterator
 #   print(letter)

#for l in iter(myString): # for bt7awl mystring la iterator
 #   print(l)

#def generator():
 #   yield 1
  #  yield 2
   # yield 3
   # yield 4

#myGen= generator()
#print(next(myGen))
#print(next(myGen))
#print("#"*30)
#for number in myGen:
 #   print(number)

#def myDecrator(fun):
 #   def nestedFun():
     #    print("before")
   #     fun()
    #    print("after")
    #return nestedFun
#@myDecrator  # tany tare2a de el 2a7sn best syntax
#def sayHello():
 #   print("hello from sayhello function")
##afterDecorartion = myDecrator(sayHello)    # awl tare2a 

##afterDecorartion()
#sayHello()


#def myDecrator(fun):
 #   def nestedFun(n1,n2):
  #       print("before")
   #      fun(n1,n2)
    #     print("after")
    #return nestedFun
#@myDecrator  # tany tare2a de el 2a7sn best syntax
#def calculate(n1 , n2):
 #   print(n1 + n2)

#calculate(10, 90)

#def myDecratorTwo(fun):
 #   def nestedFun(n1,n2):
  #       if n1 <0 or n2 < 0:
   #          print("one of numbers is less than zero")
    #     print("before")
     #    fun(n1,n2)
    #return nestedFun


#def myDecrator(fun):
 #   def nestedFun(n1,n2):     
  #       print("decorator one")
   #      fun(n1,n2)
    #return nestedFun
#@myDecratorTwo
#@myDecrator 
#def calculate(n1 , n2):
 #   print(n1 + n2)
#calculate(-5, 90)


#from time import time
#def decrator(fun):
 #   def speedTest():
  #      start = time()
   #     fun()
    #    end = time()
     #   print(f"function time is: {end - start} ") 
    #return speedTest

#@decrator
#def calSpeed():
 #   for num in range(1,150):
  #      print(num)

#calSpeed()



#from functools import reduce


#def reverse_string(my_string): # assignment 81-85
 #   rev = reversed(my_string)
  #  result= reduce(lambda leo, let: leo + let, rev)
   # yield result
#for c in reverse_string("elzero"):
 #   print(c)  

#listO =[1,2,3,4]
#listT=["a","b","c"]

#for item in zip(listO, listT):
 #   print(item)

#list1=[1,2,3,4]    
#list2=["a","b","c"]
#tuple1=("girl","boy","woman","man")
#dict1={"name":"asmaa","age":27,"country":"Egypt"}

#for item1, item2, item3, item4 in zip(list1,list2,tuple1,dict1):
 #   print(item1)
  #  print(item2)
   # print(item3)
    #print(item4, "=>" , dict1[item4])

#from PIL import Image
#myImg = Image.open(r"C:\Users\Public\project_1\landing page portfolio\imgs\cat-07.jpg")
#myImg.show()

#myBox=(0,0,300,300) # left top 3ard tool
#myNewImg = myImg.crop(myBox)
#myNewImg.show()

#myConverted = myImg.convert("L")
#myConverted.show()
#myrotatedImg = myImg.rotate(180)
#myrotatedImg.show()

#def asmaa_function(name):
 #   '''hello it is documentation from asmaa function'''
  #  print(f"hello {name}")
#print(asmaa_function.__doc__)
#help(asmaa_function)
#asmaa_function("asmaa")


#from functools import reduce


#mylist=["e","z","r",1,2,3] # assignment 86
#mytuple = ("l","e","o")
#mydata=[]

#for data in zip(mylist, mytuple):
  
 # neww = reduce(lambda lo,lt : lo+lt , data)
  #print(neww)
  #mydata.append(neww)
#print(mydata)

#final_string = reduce(lambda llo,llt : llo + llt , mydata)
#print(final_string)

#x= -10

#if x<0:
#    raise Exception(f"the number { x }  is less than zero")
#print("that will not printed because of error")

#y= 3

#if y<0:
 #   raise Exception(f"the number { y }  is less than zero")
#print("that will not printed because of error")

#x= "asmaa"

#if type(x) != int:
 #   raise ValueError("only numbers are allowed")
#print("that will not printed because of error")

#x= 5

#if type(x) != int:
 #   raise ValueError("only numbers are allowed")
#print("that will not printed because of error")

#try:
 #print(int(input('write your age')))
 #print(10/0)
 #print(x)
#except ValueError:
 #  print("value error")    
#except NameError:
#  print("not identified")   
#except ZeroDivisionError:
 # print("can not divide")  
#except:
 # print("general error")  




#the_file = None
#tries = 5

#while tries > 0:
 #   try:  
  #    print("please write the file path")
   #   print(f"you have {tries} tries left")
    #  print("example: d/:python/file")
     # file_name = input("please enter the path").strip()
      #the_file = open(fr"{file_name}","r")
      #print(the_file.read())
      #break
    #except FileNotFoundError:
     #      print("file not found")
      #     tries -= 1
    #except:
     #   print("error happened")
    #finally:
     #   if the_file is not None:
      #       the_file.close()
       #      print("file closed")
             
#else: 
 #     print("all tries are done")
      
#def hello(name)-> str: #hint
 #   print(f"say hello {name}")
#hello("adel")   

#def cal(n1,n2)-> int: #hint
 #   print(n1+n2)
#cal(2,3) 

#num = input("add your number") # assignment 91-94
#if num.isalpha() == True:
 #    raise Exception("input must be number")       
#if len(num)>1:
 #      raise IndexError("only one character allowed")
#if 1 <= int(num )<= 9:
 #     print(f"the  number is {num}")
#if int(num) <= 0:
 #      raise ValueError("number must be bigger than 0") 


#letter = input("add letter from a to z").strip() # assignment 91-94

#try:  
    
 #    if len(letter) >1:
  #        raise IndexError("INDEX ERROR")
   #  elif letter != letter.upper():
    #      raise Exception("not upper")
     #elif letter.isdigit()== True:
      #    raise ValueError("need alphabet only")
          
    
#except IndexError:
 #     print("INDEX ERROR")
#except ValueError:
 #     print("not alpha")
#except Exception:
 #     print("not upper")      
     
#else:
 # print("letter D")    
            
      
#import re
#my_string = re.search("[A-Z]","ASmaaMohamed") # return first match
#print(my_string)
#print(my_string.span())
#print(my_string.string)
#print(my_string.group())
#print(dir(my_string))

#my_search = re.search(r"[A-Z]{2}","ASmaaMohamed") # return first match
#print(my_search)
#print(my_search.span())
#print(my_search.string)
#print(my_search.group())

#is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)", "as@asmaa.com")
#if is_email:
 #   print("avalid e-mail")
#else:
 #   print("not a valid e-mail")   
#print(is_email)     
#import re
#email_input = input("please write your email")
#search = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.com|net|org|info", email_input) # match or return empty list []
#empty_list = []
#if search != []:
 #   empty_list.append(search)
  #  print("Email Added")
#else:
 #   print("invalid email")
#for email in empty_list:
 #   print(email) 
        
#string_one = "love python and programming"
#string_two = "i-love_python_and-a-programming"
#strn=re.split(r"\s",string_one)
#strnt=re.split(r"\s", string_one, 2)
#strnth=re.split(r"_",string_two)
#strntht=re.split(r"-",string_two)
#strnthtw=re.split(r"-|_",string_two)

#print(strn)
#print(strnt)
#print(strnth)
#print(strntht)
#print(strnthtw)

#for counter, word in enumerate(strnthtw, 1):
 #   if len(word) == 1:
  #      continue
   # print(f"word number: {counter} => {word.lower()}")

#print(re.sub(r"\s","-","i love python"))
#print(re.sub(r"\s","-","i love python", 1))

#import re
#my_web = "https://www.elzero.org:8080/category.php?article=105?name=how-to-do"
#searc= re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", my_web)
#print(searc)
#print(searc.group())
#print(searc.group(1))
#print(searc.group(2))
#print(searc.groups())

#searchFlag = re.search(r"[A-Z]{3}","hOLeelo", re.I) # letters not sensatives # M multiplelines # dotall match all characters and new line
#print(searchFlag)

#class Member:
 #   def __init__(self):
  #      print("new member has been added")
   #     self.name ="asmaa"
#one=Member()
#two= Member()   
#print(one)     
#print(two)
#print(dir(Member))
#print(one.__class__)
#print(one.name)
#print(two.name)

#class Membert:
 #   not_allowed_names=["hell","shit"]
  #  users_num = 0
   # def __init__(self,first_name,middle,last,gender):
    #    print("new membert has been added")
     #   self.name = first_name
      #  self.second= middle
       # self.third=last
        #self.gender = gender
        #Membert.users_num += 1
    #def full_name(self):
       # if self.name in Membert.not_allowed_names:
        #    raise ValueError("not allowed names")
        #else:
         #   return f"{self.name} {self.second} {self.third}"   
    #def name_with_title(self):
     #   if self.gender == "female":
      #      return(f"hello mss {self.name}") 
       # elif self.gender == "male":
        #    return(f"hello mr {self.name}")
        #else:
         #   return f"hello {self.name}"
    #def get_all_info(self):
     #   return f"{self.name_with_title()}, your fullname is: {self.full_name()}"  
    #def delete_user(self):
     #   Membert.users_num -= 1
      #  return f"user {self.name} deleted"

#print(Membert.users_num)     
#one=Membert("asmaa","mohamed","hussanin","female")
#two= Membert("ali","mohamed","mohey","male") 
#three=Membert("hell","lo","lk","ma")  
#print(Membert.users_num)   
  

#print(one)     
#print(two)
#print(dir(Member))
#print(one.__class__)
#print(one.name, one.second, one.third)
#print(two.second)
#print(one.full_name())
#print(one.name_with_title())
#print(two.name_with_title())
#print(one.get_all_info())
#print(two.get_all_info())
#print(three.full_name())

#print(three.delete_user())
#print(Membert.users_num)


#class Member:
 #   user_num =0
  #  @classmethod
   # def show_users_count(cls):
    #    return f"we have {cls.user_num} in our system"
    #@staticmethod
    #def hello_static():
     #   return "hello from static"
    #def __init__(self):
     #   self.name ="asmaa"
      #  Member.user_num +=1
    #def say_hello(self):
     #   return f"hello {self.name}"    

#print(Member.user_num)
#one = Member()
#print(Member.user_num)
#print(Member.show_users_count())
#print(Member.say_hello(one))
#print(Member().say_hello())
#print(one.hello_static())
#print(Member.hello_static())

#class Skill:
 #   def __init__(self):
  #      self.skills=["html","css","js"]

   # def __str__(self):
    #    return f"my skills are {self.skills}"    
    #def __len__(self):
     #   return len(self.skills)
#profile = Skill()
#print(profile)
#print(profile.__class__)

#my_string = "asmaa"
#print(my_string.__class__)
#print(str.upper(my_string))
#print(len(profile))
#profile.skills.append("vuejs3")
#profile.skills.append("python")
#print(len(profile))

#class Food:
 #   def __init__(self,name, price):
  #      self.name = name
   #     self.price = price
    #    print(f"{self.name} created from base, price is {self.price }")
    #def eat(self):
     #   print("eat from base")    

#class Apple(Food):
 #   def __init__(self,name,price,amount):
  #   self.amount = amount
     #Food.__init__(self,name)
   #  super().__init__(name,price)
    # print(f"{self.name} created from apple and amount is {self.amount}")

    #def get_from_tree(self):
     #  print("get from tree from  apple") 
    #def eat(self): #override besm nafs el fun
     #   print("eat from apple")     

#food_one = Food('rice', 20) 
#food_two= Apple("banana", 30, 2) 
#food_two.eat()         
#food_one.eat()
#food_two.get_from_tree()
    

#class BaseOne:
 #   def __init__(self):
  #      print("baseone")
   # def fun_one(self):
    #    print("one")    
#class BaseTwo:
   # def __init__(self):
    #    print("basetwo")
    #def fun_two(self):
     #   print("two")    
#class Derived(BaseOne, BaseTwo):
 #   pass

#my_var = Derived()
#print(Derived.mro())
#my_var.fun_one()
#my_var.fun_two()

#class Base:
 #   pass
#class DerivedOne(Base):
 #   pass
#class DerivedTwo(DerivedOne):
 #   pass
#n1 =10
#n2=20
#print(n1 + n2)
#s1 = "hello"
#s2= "python"
#print(s1+ " " + s2)

#print(len([1,2,3,4]))
#print(len("asmaa"))
#print(len({'key_one': 1, "key_two": 2}))

#class A:
 #   def do_something(self):
  #      print("from class A")
   #     raise NotImplementedError("derived class must implement this method")
#class B(A):
 #   def do_something(self):
  #      print("from class b")
#class C(A):
 #   def do_something(self):
  #      print("from class c")
#my_instance = C()
#my_instance.do_something()

#class Member:
 #   def __init__(self, name):
  #      self.name = name #public
#one = Member("asmaa")
#print(one.name)   
#one.name = "ali"    
#print(one.name) 

#class Membert:
 #   def __init__(self, name):
  #      self._name= name #protected
#onet = Membert("asmaa")
#print(onet._name)   
#onet._name= "ali"    
#print(onet._name) 

#class Memberth:
 #   def __init__(self, name):
  #      self.__name= name #private
   # def say_hello(self): #encapsulated gowa el class
    #    print(f"hello {self.__name}")    
#oneth = Memberth("asmaa")
#print(oneth.__name)   
#oneth.__name= "ali"    
#print(oneth.__name) 
#oneth.say_hello()
#print(oneth._Memberth__name)

#class Memberth:
 #  def __init__(self, name):
  #     self.__name= name #private
   #def say_hello(self): #encapsulated gowa el class
    #    print(f"hello {self.__name}")   
   #def get_name(self):
    #   return self.__name
   #def set_name(self, new_name):
    #   self.__name = new_name    
#oneth = Memberth("asmaa")
#print(oneth.get_name())
#oneth.set_name("ali")
#print(oneth.get_name())


#class Memberth:
 #  def __init__(self, name, age):
  #     self.name= name 
   #    self.age = age
   #def say_hello(self): #encapsulated gowa el class
    #    return(f"hello {self.name}")   
   #@property
   #def age_in_days(self):
    #   return self.age * 365
   #def set_name(self, new_name):
    #   self.__name = new_name    
#oneth = Memberth("asmaa", 10)
#print(oneth.name)
#print(oneth.say_hello())
#print(oneth.age_in_days())
#print(oneth.age_in_days)

#from abc import ABCMeta, abstractmethod
#class Programming(metaclass=ABCMeta): #abc abstract base
 #   @abstractmethod
  #  def has_oop(self):
   #     pass
    #def say_hi(self):
     #   return "hi" 
#class Python(Programming):
 #   def has_oop(self):
  #      return "yes"
#class Pascal(Programming):
 #   def has_oop(self):
  #      return "no" 
   # def say_hello(self):
    #    return "hello"   

#one = Programming()
#print(one.has_oop())
#print(one.say_hi())
#one = Python()
#print(one.has_oop())
#two =Pascal()
#print(two.say_hello())


#class A:
 #  def __init__(self, one):
  #    self.one = one
      
  
#class B:
 #def __init__(self, two):
  #    self.two = two   
#class C:
 #def __init__(self, three):
  #    self.three = three      

   
#class Name(A,B,C):
 #def __init__(self, one,two,three):
  #   A.__init__(self,one)
   #  B.__init__(self,two)
    # C.__init__(self,three)


 #def show_info(self):
        
  #    return(f"the name is {self.one}{self.two}{self.three} ")
#the_name = Name("el","ze","ro")

#print(the_name.show_info())


#import sqlite3

#db=sqlite3.connect("app.db")

#db.execute("CREATE TABLE if not exists skills (name TEXT, progress INTEGER, user_id INTEGER)")
#cr= db.cursor()
#cr.execute("CREATE TABLE if not exists users (user_id INTEGER, name TEXT)")
#cr.execute("CREATE TABLE if not exists skills (name TEXT, progress INTEGER, user_id INTEGER)")

#cr.execute("insert into users(user_id, name) values(1, 'asmaa')")
#cr.execute("insert into users(user_id, name) values(2, 'ali')")
#cr.execute("insert into users(user_id, name) values(3, 'saher')")

#my_list = ["asmaa",'ali',"tamer"]

#for key, n in enumerate(my_list):
 #   cr.execute(f"insert into users(user_id, name)values({key + 1},'{n}')")

#cr.execute("select name from users")
#cr.execute("select user_id,name from users")
#cr.execute("select * from users")


#print(cr.fetchone()) # get first row in table if no rows exist get none
#print(cr.fetchone())
#print(cr.fetchone())
#print(cr.fetchone())
#print(cr.fetchall())
#print(cr.fetchmany(2))
#db.commit()
#db.close()



#import sqlite3

#def get_all_data():
    
   # try:
        
    #    db= sqlite3.connect("app.db")
     #   print("connected to database successfully")

      #  cr = db.cursor()
       # cr.execute("select * from users")
       # result = cr.fetchall()
       # print(f"database has {len(result)} row")
       # print("showing data:")
       # for row in result:
          #  print(f"user id is {row[0]}", end=" ")
           # print(f"and user name is {row[1]}")

    #except sqlite3.Error as er:
     #   print(f"error reading data {er}")

    #finally:
     #   if(db):
      #      db.close() 
       #     print("connection to database is closed")    
#get_all_data()

#import sqlite3

#db = sqlite3.connect("app.db")
#cr = db.cursor()
#cr.execute("update users set name = 'gamal' where user_id = 1")
#cr.execute("delete from users")
#cr.execute("delete from users where name = 'ali'")

#cr.execute("select * from users")
#print(cr.fetchall())
#db.commit()


#import sqlite3
#db = sqlite3.connect("app.db")
#cr = db.cursor()
#cr.execute("create table if not exists skills(name, progress, user_id)")

#def commit_close():
 #  db.commit()
  # db.close()
   #print("connection to database closed")
#uId= 2

#input_message = """
#what do you want?
#"s" => show all skills
#"a" => add a new skill
#"d" => delete a skill
#"u"=> update skill progress
#"q" => quite the app
#choose option: 
#"""
#user_input = input(input_message).strip().lower()
#command_list=["s","a","d","u","q"]


#def show_skills():
 #   cr.execute(f"select * from skills where user_id = '{uId}'")
  #  result = cr.fetchall()
   # print(f"you have {len(result)} skills: ")
    #for key, value in enumerate(result):
     #   print(f"{key + 1}-{value[0]}, progress => {value[1]}")

    #commit_close()
#def add_skills():
 #   sk = input("write your skill: ").strip().capitalize()
  #  cr.execute(f"select name from skills where name = '{sk}' and user_id = '{uId}'")
   # result = cr.fetchone()
    #if result == None:
        
     # prog = input("write skill progress: ").strip()
      #cr.execute(f"insert into skills(name, progress, user_id) values('{sk}','{prog}','{uId}')") # (name, progress, user_id)momkn delete it or not
    #else:
     #   print("already exists, want to update progress?") 
      #  ys= input("choose y or n")[0].strip().lower()
       # if ys == "y":
        #  prog = input("write skill progress: ").strip()

         # cr.execute(f"update skills set progress = '{prog}' where name ='{sk}' and user_id='{uId}'") 
          #print("updated successfully")
          #commit_close()

        #elif ys == "n":
         #   commit_close()
        #else:
         #   print("error")  
          #  commit_close()



#def delete_skills():
 #sk = input("write your skill: ").strip().capitalize()
 #cr.execute(f"delete from skills where name = '{sk}' and user_id = '{uId}'")
 #commit_close()   
#def update_skills():
 #   sk = input("write your skill: ").strip().capitalize()
  #  prog = input("write skill progress: ").strip()
   #cr.execute(f"update skills set progress = '{prog}' where name = '{sk}' and user_id = '{uId}'")

    #commit_close()

#if user_input in command_list:
 #   print(f"command found {user_input}")
  #  if user_input == "s":
   #     show_skills()
    #elif user_input == "a":
     #   add_skills()
    #elif user_input == "d":
     #   delete_skills()    
    #elif user_input == "u":
     #   update_skills()
    #else:
     #   print("app closed") 
      #  commit_close()        
#else:
 #   print(f"command is not exist \" {user_input}\"")


#import sqlite3
#db = sqlite3.connect("app.db")
#cr = db.cursor()
#cr.execute("create table if not exists skills(name, progress, user_id)")
#my_tuple = ('java',"65",1)
#cr.execute("insert into skills values('java','65',2)")
#cr.execute("insert into skills values(?, ? ,?)", ('js',"55",4))

#cr.execute("insert into skills values(?, ?, ?)", my_tuple)

#cr.execute("select * from skills")
#cr.execute("select * from skills order by user_id")
#cr.execute("select * from skills order by user_id asc")
#cr.execute("select * from skills order by user_id desc")
#cr.execute("select * from skills order by name")
#cr.execute("select * from skills order by name limit 2")
#cr.execute("select * from skills order by name 2 offset 2") 3ayz 2 bas w fawt 2
#cr.execute("select * from skills where user_id > 1")
#cr.execute("select * from skills where user_id in (1,2,3)")
#cr.execute("select * from skills where user_id not in (1,2,3)")

#res= cr.fetchall()
#print(res)

#db.commit()
#db.close()

#print(__name__)
#import py_one # type: ignore

#import timeit
#print(dir(timeit))

#print(timeit.timeit("'elzero' * 1000"))

#print(timeit.timeit("name = 'elzero'; name * 1000"))

#import random

#print(random.randint(0, 50))
#print(timeit.timeit(stmt="random.randint(0, 50)", setup="import random"))
#print(timeit.repeat(stmt="random.randint(0, 50)", setup="import random", repeat=4))

#import logging
#print(dir(logging))
#logging.basicConfig(filename="my_app.log", filemode="a", format="%(asctime)s => %(name)s | %(levelname)s | '%(message)s'", datefmt="%d - %B - %Y, %H:%M:%S") # filemode = "w" get last msg only
#logging.critical("this is critical message")
#logging.error("this is error message")
#logging.warning("this is warning message")

#my_logger = logging.getLogger("asmaa") # change name instead of root

#my_logger.warning("ths is warning")


#assert 3*8 == 24, "should be 24"
#assert 3*8 == 23, "should be 24"

#def test_case_one():
 #   assert 5*10 == 50, "should be 50"

#def test_case_two():
  #  #assert 5*5 == 5, "should be 25"
 #   assert 5*5 == 25, "should be 25"


#if __name__ == "__main__":
 #   test_case_one()    
  #  test_case_two()
   # print("all tests passed")

#import unittest
#class MyTestCase(unittest.TestCase):
 #   def test_one(self):
  #      self.assertTrue(100> 97, "should be true")
   #     #self.assertTrue(100> 100, "should be true")
   # def test_two(self):
    #    self.assertEqual(40+60,100, "should be 100")
    #def test_three(self):
       ## self.assertTrue(100> 97, "should be true")
     #   self.assertGreater(100, 101, "should be true")
    
#if __name__ == "__main__":
 #   unittest.main()    

#import string
#import random
#print(string.digits)
#print(string.ascii_letters)
#print(string.ascii_lowercase)
#print(string.ascii_uppercase)

#def make_serial(count):
 #   all_chars= string.ascii_letters + string.digits
  #  print(all_chars)
   # chars_count = len(all_chars)
    #print(chars_count)
    #serial_list = []

    #while count > 0:
     #   random_number = random.randint(0, chars_count -1)
      #  random_charachter= all_chars[random_number]
       # serial_list.append(random_charachter)
        #count -= 1
    #print("".join(serial_list))


#make_serial(10)    

# from flask import Flask
# skills_app = Flask(__name__)
# @skills_app.route("/")
# def homepage():
#     return "hello from flask framework"

# @skills_app.route("/about")
# def aboutpage():
#     return "about page from flask framework"

# if __name__ == "__main__":
#   skills_app.run(debug=True, port=9000)
#from flask import Flask, render_template


#skills_app = Flask(__name__)

#my_flaskskills=[("html", 80),("css",90),("js",100)]
#@skills_app.route("/")
#def homepage():
#   return render_template('homepage.html', pagetitle="h", test="hello a", custom_css="home")

#@skills_app.route("/about")
#def aboutpage():
 #   return render_template("about.html", pagetitle="a", test="hello b")

#@skills_app.route("/add")
#def addpage():
 #   return render_template("add.html", pagetitle="d", test="hello c", custom_css="add")
#@skills_app.route("/skills")
#def skillspage():
 #   return render_template("skills.html", pagetitle="s", test="hello s", page_head="my skills", description="this is skills page",skills=my_flaskskills, custom_css="skills")

#if __name__ == "__main__":                                       
 # skills_app.run(debug=True, port=9000) 

# from selenium import webdriver
# from selenium.webdriver.common.by import By




# #from webdriver_manager.chrome import ChromeDriverManager i dont need it

# browser = webdriver.Chrome()
# browser.get("https://elzero.org")

# browser.find_element(By.CSS_SELECTOR, "#search").send_keys("Front End Developer")
# browser.implicitly_wait(1)



# browser.find_element(By.CSS_SELECTOR, ".search-submit").click()
# browser.implicitly_wait(1)
# browser.find_element(By.CSS_SELECTOR, ".all-search-posts .search-post:first-of-type h3 a").click()


# browser.implicitly_wait(1)

# views_count =browser.find_element(By.CSS_SELECTOR, ".z-article-info .z-info:last-of-type span:last-child").click()
# browser.implicitly_wait(1)

# print(views_count.get_attribute('innerHTML'))
# browesr.quit()


#import numpy as np
#print(np.__version__)
#print(dir(np))
#my_list = [1, 2, 3, 4, 5]
#my_array = np.array(my_list)
#print(my_list)
#print(my_array)
#print(type(my_list))
#print(type(my_array))

#print(my_list[0])
#print(my_array[0])

#a = np.array(10) # zero dimension array
#b= np.array([10, 20]) # one dimension array
#c= np.array([[1,2],[1,4]]) # two dimension array
#d= np.array([[[5,6],[7,9]],[[1,3],[4,8]]]) # three dimension array

#print(d[1][1][1]) #8 
#print(d[1,1,1]) #8
#print(d[1, 1, -1]) #8

#print(a.ndim)
#print(b.ndim)
#print(c.ndim)
#print(d.ndim)

#my_custom_array = np.array([1, 2, 3], ndmin=3)
#print(my_custom_array)
#print(my_custom_array.ndim)
#print(my_custom_array[0][0][0]) #1
#print(my_custom_array[0,0,0]) #1


#print(id(my_list[0]))
#print(id(my_list[1]))
#print("#"*10)
#print(id(my_array[0]))
#print(id(my_array[1]))

#my_datalist = [1,2, "a","b",True,10.50]
#my_arraydata= np.array([1,2, "a","b",True,10.50])
#my_arraydatatwo=np.array([10,20,30.5])

#print(my_datalist)
#print(my_arraydata) #7awlhom klohm string
#print(my_arraydatatwo) #7awlhom klohm float
#import numpy as np
#import time
#import sys

# elements = 15000000

# my_list1= range(0,elements) #end not iclude ..we can delete0 and will still begin from 0
# my_list2=range(0,elements)

# my_array1= np.arange(elements)
# my_array2= np.arange(elements)

# list_start = time.time()
# list_result = [(n1 + n2) for n1,n2 in zip(my_list1, my_list2)]
# print(f"list time: {time.time()-list_start}")

#for n1,n2 in zip(my_list1, my_list2):
 #   print(n1 + n2)

# array_start = time.time()
# array_result = my_array1 + my_array2
# print(f"array time: {time.time()-array_start}")

#print(list_result)
#print(array_result)

#m_array = np.arange(100)
#print(m_array)
#print(m_array.itemsize) # one element by bytes
#print(m_array.size) #length
#print(m_array.itemsize * m_array.size)

#m_list = range(100)
#print(sys.getsizeof(m_list[1]))
#print(len(m_list))
#print(len(m_list)* sys.getsizeof(m_list[1]))


#import numpy as np

#a= np.array(['a','b','c','d','e','f'])
#print(a.ndim)
#print(a[1])
#print(a[1:4])
#print(a[0:4])
#print(a[2:])

#b=np.array([['a','b','x'],['c','d','y'],['e','f','z'],['m','n','o']])
#print(b.ndim)
#print(b[1])
#print(b[0:3, 0:2])
#print(b[2:, 0])
#print(b[2: , 0:2])
#print(b[2:, 0:2:2])
#import numpy as np
#my_array1= np.array([1,2,3])
#my_array2= np.array([1.5,20.15,3.601])
#my_array3= np.array(["as","b","ali"])

#print(my_array1.dtype)
#print(my_array2.dtype)
#print(my_array3.dtype)

#my_array4= np.array([1,2,3], dtype="f")
#my_array4= np.array([1,2,3], dtype=float)
#my_array4= np.array([1,2,3], dtype="float")

#my_array5= np.array([1.5,20.15,3.601], dtype="i") # or int or "i"
#my_array6= np.array(["as","b","ali"], dtype=int) #value error


#print(my_array4.dtype)
#print(my_array5.dtype)
#print(my_array6.dtype)


#my_array7 = np.array([0,1,2,3,0,4])
#print(my_array7.dtype)
#print(my_array7)
#print("#" * 50)
#my_array7= my_array7.astype("float")
#print(my_array7.dtype)
#print(my_array7)
#print("#" * 50)
#my_array7 = my_array7.astype("bool")
#print(my_array7.dtype)
#print(my_array7)

#my_array8 = np.array([100, 200, 300, 400], dtype="float")
#print(my_array8.dtype)
#print(my_array8[0].itemsize)

#import numpy as np
#my_array1 = np.array([10,20,30])
#my_array2 = np.array([5,2,4])
#print(my_array1 + my_array2)
#print(my_array1 - my_array2)
#print(my_array1 * my_array2)
#print(my_array1 / my_array2)

#my_array1 = np.array([[1,4], [5,9]])
#my_array2 = np.array([[2, 7], [10, 5]])
#print(my_array1 + my_array2)
#print(my_array1 - my_array2)
#print(my_array1 * my_array2)
#print(my_array1 / my_array2)

#my_array4= np.array([10, 20, 30])
#print(my_array4.min())
#print(my_array4.max())
#print(my_array4.sum())
#print("#" * 50)
#my_array5 = np.array([[6,4], [3,9]])
#print(my_array5.min())
#print(my_array5.max())
#print(my_array5.sum())
#print(my_array5.ravel())


#my_array1= np.array([1, 2, 3, 4])
#print(my_array1.ndim)
#print(my_array1.shape) #(4,)

#my_array2= np.array([[1, 2, 3, 4], [1, 2, 3, 4],[1, 2, 3, 4]])
#print(my_array2.ndim)
#print(my_array2.shape)  # (3, 4)

#my_array3= np.array([[[1, 2, 3, 4], [1, 2, 3, 4]],[[1, 2, 3, 4] , [1, 2, 3, 4]]])
#print(my_array3.ndim)
#print(my_array3.shape) # (2, 2, 4)

# my_array4 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

# my_reshaped= my_array4 = my_array4.reshape(3, 4)
# print(my_reshaped)
# print(my_reshaped.ndim)
# print(my_reshaped.shape)

#my_array4 = np.array([[1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5,6,7,8,9,10]])

#my_reshaped= my_array4 = my_array4.reshape(-1)
#print(my_reshaped)
#print(my_reshaped.ndim)
#print(my_reshaped.shape)
#my_reshaped = my_array4.reshape(5, 4)
#print(my_reshaped)
#print(my_reshaped.ndim)
#print(my_reshaped.shape)
#my_reshaped = my_array4.reshape(2,5, 2)
#print(my_reshaped)
#print(my_reshaped.ndim)
#print(my_reshaped.shape)

#import ascii_train

#print(ascii_train.train("asmaa"))


























