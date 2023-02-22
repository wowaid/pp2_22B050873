def filter_prime(numbers): 
    return filter(lambda x: all(x % i != 0 for i in range(2, x)), numbers) 

numbers = list(map(int , input().split())) 
prime_numbers = list(filter_prime(numbers)) 
print(prime_numbers)