#demande limit
a = 0
b = 1
count = 0
limit = int(raw_input("nombre "))

while count < limit:
    print(count)
    count = a+b
    a = b
    b = count
