# print("hello world")
# a = 1
# a = "Hello world"
# a = [1,2,3]
# a = [1.2, 'Hello','W',2]
# if 1==2 :
#       print("a equals 1")
#       print("2 bigger 1")
# elif 1<2 :
#       print("1 less than 2")
# python = "Python"
# for letter in python:
#       print  'Current letter :', letter
# count = 0;
# while count <9 :
#       print 'count :', count
#       count+=1
# print "good bye !"
# def sumTwoInt(a,b):
#       return a+b
# print "result :",sumTwoInt(5,6)
# def sumNumberWith10(a,b=10):
#       return a
# print "result sum a number with 10:",sumNumberWith10(b=15,a=2)
# textArea = '''this is line 1
# this is line true'''
# print textArea
str = 'hello world'
print str[0:4]
print str[:4]
print str[3:]
print str[0:-1]
print 'get length of str', len(str)
str =str.replace('l','o')
print 'find \'l\' and replace \'o\' :',str
print 'find substring \'w\t',str.find('w')
print 'find substring \'world\t',str.find('world')
# rfind : find from the right to the left
arr= str.split(" ")
for item in arr :
    print "item :",item
arr= str.splitlines()
for item in arr:
    print "item :",item
text ="34556"
isNumber = text.isdigit()
print(isNumber)
