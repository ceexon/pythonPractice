#!/bin/python3

import os
import sys
import unittest


#
# Complete the timeConversion function below.
#
def timeConversion(input_time):
    #
    # Write your code here.
    #
    if input_time[-2:] == "AM":
        if input_time[:2] == "12":
            return "00" + input_time[2:-2]

        elif int(input_time[:2]) <= 11:
            return input_time[:-2]

    elif input_time[-2:] == "PM" and input_time[:2] == "12":
        return input_time[:-2]

    elif input_time[-2:] == "PM":
        begin = int(input_time[:2])
        begin = begin + 12
        return str(begin) + input_time[2:-2]


class TestConverter(unittest.TestCase):
    def test_timeConverter(self):
        result = timeConversion("06:40:03AM")
        self.assertEqual(result, "06:40:03")

if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # s = input()
    #
    # result = timeConversion(s)
    #
    # f.write(result + '\n')
    #
    # f.close()
    unittest.main()
