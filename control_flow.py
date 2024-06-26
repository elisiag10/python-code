age = 18
if age >= 18:
    print("you are now an adult :)")

temp = 25
if temp > 30:
    print("It's warm outside")
else:
    print("It's not too hot")

res = 85
if res >= 90:
    grade = "A"
elif res >= 80:
    grade = "B"
elif res >= 70:
    grade = "C"
else:
    grade = "D"
print (f"your grade obtained is {grade}")
print (f"hello world")

fruits = ["apples", "bananas", "grapes"]
for fruit in fruits:
    print(f"Current fruit: {fruit}")

for num in range(1, 6):
    print (f"Number: {num}")

cnt = 0 
while cnt < 5:
    print(f"Count: {cnt}")
    cnt += 1

numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 == 0:
        print(f"Skipping this even number: {num}")
        continue
    print(f"Current number: {num}")
for i in range(3):
    for j in range(3):
        print(f"i: {i} j: {j}")

#Funcution defined as recursive

def recursive(i, j):
    if i < 3:
        if j < 3:
            print(f"i: {i} j: {j}")
            recursive(i, j + 1)
        else:
            recursive(i + 1, 0)
    else:
        return

recursive(0, 0)