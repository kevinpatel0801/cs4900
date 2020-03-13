#!/usr/bin/python
"""
This is code to write and read from a file


"""

__author__ = "Kevin Patel"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "kevpatel@vsu"
__status__ = "done"


def write_primes(l, file_name):
    """Summary line
    This is a the code that opens the file and writes the number
    to the file.

    Args:
        file_name (str): intput file name
        Returns:
            N/A
    Raises:
        IOError: io error
    Examples:
        write.write ('%s\t" % l)

    """
    write_file = open(file_name, "w")
    write_file.write('%s\t' % l)


def read_primes(file_name):
    """Summary line
        This code reads the file and returns the list
        Args:
            file_name (str): intput file name
            Returns:
                return l
        Raises:
            IOError: io error
        Examples:
           read_file = open(file_name, "r")

        """
    read_file = open(file_name, "r")
    if read_file.mode == "r":
        l = read_file.read()
        return l
