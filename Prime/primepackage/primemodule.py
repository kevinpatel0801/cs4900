#!/usr/bin/env python
__author__ = "Kevin Patel"
__license__ = "GPL"
__version__ = "0.2"
__email__ = "kevpatel@vsu"
__status__ = "done"


def isPrime(n):
    """Summary line
           This code reads the file and returns the list
              return true if it is prime if not then false
               Returns:
                   return true
                   return false
           Raises:
               it raises if the value is less then 0
           Examples:
             if isPrime(5)
    """
    if n < 0:
        raise ValueError("value can not be less then 0")
    elif n > 0:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


def getNPrime(num):
    """Summary line
            This code get all the prime numbers and put it in a array
            list.
               Args:
                  num:
                  return true if it is prime if not then false
                   Returns:
                      return list1
               Raises:
                   IOError: io error
               Examples:
                 put 2 in to the file because it is prime
    """

    list1 = []
    for i in range(2, num*6-55):
        if isPrime(i):
            list1.append(i)
    return list1
