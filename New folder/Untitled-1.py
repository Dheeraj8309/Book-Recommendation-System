n1 = int(input('Enter positive number less than 100 '))
if(n1%2!=0):
    print("Weird")
elif n1 in range(2, 5):
    print("Not weird")
elif n1 in range(6, 20):
    print("Weird")
elif(n1>20):
    print("Not Weird")

