# 2. Write a function that counts the number of times the number 7 occurs in a given integer
# # without converting it to a string.
# # For example the number 7,704,793 would output 3

my_number = 7704793
def seven_count(number):
    number_of_sevens = 0
    n = abs(number)
    while n > 0:
        remainder = n % 10
        if remainder == 7:
                number_of_sevens += 1
        n = (n - remainder) / 10
    return number_of_sevens
print(seven_count(my_number))