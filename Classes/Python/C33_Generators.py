#Generator
'''Which produces a single value everytime'''

#Keyword used 'yield'
#In general
def numbers():
    return [1,2,3,4]

numbers()

#Generators uses yeilds - this is will know how many time the loop should iterate, and knows the memory as well!!
#Yeild ani use cheskuna prathi sari object create aitundi unlike return(Deentlo okate sari object create aitundi)
def numbers():
    yield 1
    yield 2
    yield 3
for i in numbers():
    print(i)

#Using Next
def numbers():
    yield 1 
    yield 2
    yield 3
g = numbers()
print(next(g))

#Malli pring next ante second number print aitundi!! Memory untadi daniki ekkad varku print chesindi ani
#printing as list

print(list(g))


def simple_gen():
    print("start")
    yield "A"
    print("Middle")
    yield "B"
    print ("End")

gene=simple_gen()
print (next (gene))