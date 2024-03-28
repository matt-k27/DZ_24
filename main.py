from inspect import isgenerator

print('DZ24')

def prime_generator(end):
    seed = [True] * (end + 1)
    for i in range(2, end + 1):
        if seed[i]:
            yield i
            for j in range(i * i, end + 1, i):
                seed[j] = False

# def prime_generator(end):
#     for number in range(2, end+1):
#         if ((number == 2 or number == 3 or number == 5 or number == 7) or
#                 (number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0)):
#             yield number


gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')

print('Thank you for using')
