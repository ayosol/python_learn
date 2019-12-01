#Using while loop
num = 1
while num < 11:
    print("\U0001f600" * num)
    #print("#" * num)
    num = num + 1
#Using for loop
for num in range(1, 11):
    print("\U0001f600" * num)
    #print("#" * num)

#Using nested loops instead of string multiplication...
for num in range(1, 11):
    count = 1
    hasht = ""
    while count < num:
        #print("\U0001f600" * num)
        count += 1
        hasht += "#" 
    print(hasht)

#TO create a Triangle of nnumbers
counter = 9
num = 1
while counter > 0:
    spaces = " " * counter
    word = "\U0001f600" * num
    new_word = spaces + word + spaces
    print(new_word)
    counter = counter - 1
    num = num + 1
