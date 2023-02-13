#Exercise 1

#list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
    i = i*i*i
    if i >= 1001:
        break
    print(i)
print('number exceeds 1000')

#Exercise 2

num = 2

while num <= 100:
    check = 2
    while check < num:
        if num % check == 0:
            break
        check +=1
    else:
        print(num)
    num+= 1

# Exercise 3

person_age = int(input('How old are you?'))

if person_age < 18:
    print('kids')
elif person_age <= 65:
    print('adults')
else:
    print('seniors')