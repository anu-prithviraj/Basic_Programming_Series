from Palindrome import PalindromeFinder


def test_to_find_palindrome():
    dict = {"positive_example" : "Madam, I'm Adam!!", "negative_example" : "Boys"}  
    expected_for_test_palindrome.pyhappy_case = True 
    expected_for_unhappy_case = False
    for each_in_dict in dict:
        pobj = PalindromeFinder(dict[each_in_dict])
        if each_in_dict == "positive_example":
            result = pobj.to_find_palindrome()
            assert result == expected_for_happy_case
        elif each_in_dict == "negative_example":
            result = pobj.to_find_palindrome()
            assert result == expected_for_unhappy_case    
        else:
            raise Exception("Execution completed without test")

            
    

         
