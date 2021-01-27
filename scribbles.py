# def namelist(names):

names = [{'name':'Niall'}, {'name':'Susie'},{ 'name':'Ricardo'}]

str_list = []
for x in names:
        str_list.append(x.get('name'))

if len(str_list) > 1:
    print(' & '.join([', '.join(str_list[:-1]), str_list[-1]]))
elif len(str_list) == 1:
    print(str_list[0])
else:
    print('')



l = ['a', 'b', 'c']
z = ' & '.join(', '.join(l).rsplit(', ', 1))
# print(z)

print(' & '.join(l))
print(', '.join(l).rsplit(', ', 1))



def namelist(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), 
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''
print(namelist([{'name':'Niall'},{'name':'Susie'},{'name':'Ricardo'},{'name':'Mum'}]))

names = [{'name':'Niall'},{'name':'Susie'},{'name':'Ricardo'},{'name':'Mum'}]

x = '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), names[-1]['name'])
print(x)

arr = [1,9,4]
# def gimme(input_array):
x = sorted(arr)

if x[1] in arr:
    print(arr.index(x[1]))

print("Hello World")

def diamond(size):
    size = int(n)
    if (size =< 0) or (size % 2 ==0):
        print ("Diamond Size Must Be A Positive Odd Integer")
        return None
        
    for digit in range(size):
        for 


# def diamond(size):
def diamond(size):  

    if size <= 0:
        return None
    if size % 2 == 0:
        return None
              
    for i in range(size):
        for s in range (size - i):
            return (" "*s) 
        for j in range((i * 2) + 1):
            return "*" * (j) /n

diamond(3)
    
    
for i in range(userInput, 0, -1):
    for s in range (userInput - i) :
        print(" ", end="")
    for j in range((i * 2) - 1):
        print("*", end="")
    print()


