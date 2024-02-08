import sys

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)

def main():
    n = int(sys.argv[0])
    print(fizzbuzz(n))

if __name__ == "__main__":
    main()
