#!/usr/bin/python

"""A Python program generating a list of prime numbers and output them into a csv file
 
"""
__author__ = "Kevin Patel"
__license__ = "GPL"
__version__ = "0.2"
__email__ = "kevpatel@vsu"
__status__ = "done"

from primepackage import *


def main():
    """Generate 100 prime numbers and output it into output.csv file
       use try and exept to handle exceptions
    """


try:
    primes = getNPrime(100)

    write_primes(primes, 'output.csv')

    l = read_primes('output.csv')
except:
    print("function not found")
else:
    print(l)

if __name__ == '__main__':
    main()
