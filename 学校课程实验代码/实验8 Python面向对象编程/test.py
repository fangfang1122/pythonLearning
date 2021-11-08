from functools import reduce


def mul(a, b):
    print(a, b)
    return a * b


# sum1 = reduce(lambda a, b: a * b, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
sum1 = reduce(mul, list(range(1, 21)))
print(sum1)


class Cat:
    __species = 'cat'

    def catch_mice(self):
        print(f'A {self.__species} catches a mouse!')


class Babby(Cat):
    pass


babby = Babby()
babby.catch_mice()
