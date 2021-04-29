
import argparse

class PalindromeFinder:
    """
    This class shows the python script implementation on finding
    if the given user input is a Palindrome or not.
    """

    def __init__(self, input):
        self.input = input

    def to_find_palindrome(self):
        """
        Return the palindrome of the user input given.

        Parameter:
            input : the string which is to be reversed

        returns:
            True or False based on the reversed string == input string    
        """
    
        if self.input.isalnum():
            input_to_case_change = self.input.casefold()
        else:
            input_to_case_change = ''.join(e for e in self.input if e.isalnum()).casefold()
        reverse_of_word = input_to_case_change[::-1]
        if input_to_case_change == reverse_of_word:
            print("The input given is a PALINDROME !! ")
        else:        
            print("The input given is NOT a PALINDROME")


def Parse_the_argument():
    """
    Parsing and adding command line arguments.
    """
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True,
                        help="Enter a palindrome word eg: AMMA")                 
    return parser

if __name__ == '__main__':
    parser = Parse_the_argument()
    args = parser.parse_args()
    palindrom_object = PalindromeFinder(input = args.input)
    palindrom_object.to_find_palindrome()