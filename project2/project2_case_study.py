"""
This module provides the requested output for Project 2.
"""
import operator


class BaseConverter:
    """
    This class provides a framework for converting from base 16 to base 10.
    """

    @staticmethod
    def convert_to_base10(base16_value):
        """
        A converter from base 16 to base 10.
        :param base16_value: A string representing a base 16 value.
        :return: A integer which represents the inputted string in base 10.
        """
        base10_value = 0
        base16_value_length = len(base16_value)
        for index, value in enumerate(base16_value):
            place_val = (16**(base16_value_length-index-1))  # E.g., 16^2.
            val_in_base10 = BaseConverter.get_base16_to_base10_dict()[value]
            base10_value += val_in_base10 * place_val

        return base10_value

    @staticmethod
    def get_base16_to_base10_dict():
        """
        Gives a map which indicates the base 10 value of each digit in base 16
        :return: A map/dictionary described above.
        """
        base16_base10_dictionary = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "A": 10,
            "B": 11,
            "C": 12,
            "D": 13,
            "E": 14,
            "F": 15
        }
        return base16_base10_dictionary


NUMBERS = ["ACED",
           "BED",
           "CAFE",
           "DECAF",
           "ED",
           "FACED"]

NUMBER16_AND_NUMBER10 = []

for number in NUMBERS:
    NUMBER16_AND_NUMBER10.append((number, BaseConverter().convert_to_base10(number)))

NUMBER16_AND_NUMBER10 = sorted(NUMBER16_AND_NUMBER10, key=operator.itemgetter(1))

for number_in_b16, number_in_b10 in NUMBER16_AND_NUMBER10:
    print(number_in_b16, number_in_b10, sep=", ")
