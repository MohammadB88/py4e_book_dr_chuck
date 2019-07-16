# in this example I must read the number in a float variable.
str = 'X-DSPAM-Confidence:0.8475'

# METHOD 1
index1 = len(str)
# this ""str[index1-6:]"" is called string slicing
number1 = float(str[index1-6:])
print(number1)

# METHOD 2
index2 = str.find(':')
# this ""str[index2+1:]"" is called string slicing
number2 = float(str[index2+1:])
print(number2)
