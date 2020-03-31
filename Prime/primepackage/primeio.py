#!/usr/bin/python
"""
This is code to write and read from a file


"""

__author__ = "Kevin Patel"
__license__ = "GPL"
__version__ = "0.2"
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
     try to read the file if not then type file not found
    Examples:
        write.write ('%s\t" % l)


    """

    try:
        write_file = open(file_name, "w")
        write_file.write('%s\t' % l)
        write_file.close()
    except FileNotFoundError:
        print("file can not be read")
    else:
        print("file was written successfully")


def read_primes(file_name):
    """Summary line
        This code reads the file and returns the list
        Args:
            file_name (str): intput file name
            Returns:
                return l
        Raises:
           try to see if the file is found if not send file not found
        Examples:
           read_file = open(file_name, "r")

        """
    try:
        read_file = open(file_name, "r")
        if read_file.mode == "r":
            l = read_file.read()

    except FileNotFoundError:
        print("file can not be read")
    else:
        return l
        print("file was read successfully")
