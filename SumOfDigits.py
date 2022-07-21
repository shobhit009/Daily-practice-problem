def sum_of_digits(n):
    sum = 0
    while(n):
        x = n % 10
        sum += x
        n = n//10
    return sum

def recursive_sum_of_digit(n):
    if (n==0):
        return 0
    
    return (n%10 + recursive_sum_of_digit(n//10))
    
# print(sum_of_digits(10))
print(recursive_sum_of_digit(9987))

