# 2. Sum of All Multiples of 3 or 5 below 1000
# # If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# # Find the sum of all the multiples of 3 or 5 below 1000.

# i = 0

# for n in range (1,1000):
#     a = 3
#     b=5
#     if n % a == 0 or n % b == 0:
#         i +=n
# print (n)


# result = 0
# for i in range(0,1000):
#     if (i % 3 == 0 or i % 5 == 0):
#         print (i)
#         result = result + i
# print (result)

max = 1000  # notice this here
result = 0
for i in range(0,max):
    if i%3 == 0 or i%5 == 0:
        result += i

print (result)