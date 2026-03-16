# type conversion
a = 5
b = 3.14
sum = a + b #automatic type conversion (int to float)
print(sum) # 8.14

c= "10"
sum2 = a + c # this will raise an error because we cannot add an integer and a string
print(sum2) # 15

sum3 = a + int(c) # we can convert the string to an integer before adding also called tpe casting
print(sum3) # 15