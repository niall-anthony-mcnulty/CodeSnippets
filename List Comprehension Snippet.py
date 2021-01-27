
x = int(input("Enter A Value:"))
y = int(input("Enter A Value:"))
z = int(input("Enter A Value:"))
n = int(input("Enter A Value:"))

arr = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n]

print (arr)

print(type(arr))
print(arr[0])