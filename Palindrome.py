"""
Script to check whhether a given input(int/str) is a palindrom or not using reversed() function
"""
import argparse
import logging

class PalindromeFinder(object):

    def __init__(self, input):
        self.input = input

    def to_find_palindrome(self):
        input_to_case_change = self.input.casefold()
        reverse_of_word = input_to_case_change[::-1]
        try:
            if input_to_case_change == reverse_of_word:
                print("The input given is a PALINDROME !! ")
            else:        
                logging.error("The input given is NOT a PALINDROME")
        except Exception:
            logging.info("-----")        
            

def palindrome():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True,
                        help="Enter a palindrome word eg: AMMA")
                        
    return parser

if __name__ == '__main__':
    parser = palindrome()
    args = parser.parse_args()

    palindrom_object = PalindromeFinder(input = args.input)
    palindrom_object.to_find_palindrome()



