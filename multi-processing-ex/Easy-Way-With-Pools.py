# remove the other_way function and directly run the code otherwise pickle error will come
# def one_way():
import concurrent
import concurrent.futures

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


with concurrent.futures.ProcessPoolExecutor() as executor:
    nums = [20,34,32,21]
    result:list[concurrent.futures.Future] = [executor.submit(fib,num) for num in nums]
    for f in concurrent.futures.as_completed(result):
        print(f.result())


# remove the other_way function and directly run the code otherwise pickle error will come
# better way to use map than submit
# submit returns a future object and does not block
def other_way():
    import concurrent.futures
    import math

    PRIMES = [
        112272535095293,
        112582705942171,
        112272535095293,
        115280095190773,
        115797848077099,
        1099726899285419]

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        sqrt_n = int(math.floor(math.sqrt(n)))
        for i in range(3, sqrt_n + 1, 2):
            if n % i == 0:
                return False
        return True

    def main():
        with concurrent.futures.ProcessPoolExecutor(max_tasks_per_child=1) as executor:
            for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
                print('%d is prime: %s' % (number, prime))
    main()