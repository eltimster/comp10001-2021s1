#
# Test harness for COMP10001 Project 2, 2021s1
#
# Author: Tim Baldwin
#
# Date: 26/4/2021
#
# Version 1.0
#



import sys


try:
    import program as submission  # import the file `program.py'
    import tests  # import the file `tests.py'
    try:
        import tests_extra
    except ImportError:
        print("WARNING: No 'tests_extra.py' file found ... running only the tests in 'tests.py'\n")

# exit if one of the above statements doesn't execute properly, presumably because `program.py' didn't import properly
except ImportError as detail:
    print(f"ERROR: {detail}")
    raise
except Exception as detail:
    print(f"ERROR: {detail}")
    raise

    
    


####################################################################################
#
# name: test()
#
# synposis: run the tests for the supplied function name, and check the outputs against those in `test`
# input(s): the function name to be tested (str)
# output(s): print the tests that are tried, and if unsuccessful, the correct value vs. returned value
#

def test(funct_name, testset):
    # print out the names of functions which can be tested in `funct_name` is not in `tests`, and exit
    if funct_name not in testset.test_cases:
        print(f"ERROR: '{funct_name}' is not a recognised function name; select from: {str(testset.test_cases.keys())}")
        return -1
    
    # run test (using valid function name)
    print(f"Testing the {funct_name} function ...\n")
    correct = 0  # number of tests passed
    
    # run the user-defined function with each of the sets of arguments provided in `tests`, and chech that the
    # output is correct
    for test in testset.test_cases[funct_name]:
        print(f"  testing {test[0]} ...")
        userval = eval(test[0])  # run the function with the supplied set of arguments (take the string and execute it)
        expval = test[1]
        
        # if the returned value is correct, increment `correct` and print a congratulatory print statement
        if test_equivalent(userval,expval,funct_name):
            correct += 1
            print("passed")
            
        # if the returned value is *in*correct, print diagnostics
        else:
            print("failed")
            print(f"    * expected = (type '{type(expval)}') {expval}")
            print(f"    * returned = (type '{type(userval)}') {userval}")
    
    # print the overall number of tests passed vs. attempted    
    print(f"\n{correct}/{len(testset.test_cases[funct_name])} tests passed for {funct_name}")

#   
# end test()    
####################################################################################





    
####################################################################################
#
# name: test_equivalent()
#
# synposis: test for equivalence between two arguments. In particular, for this project
#   we need to allow for different orders between hands, as well as different orders
#   for the cards in a hand. We do this by converting the a list-of-lists representation
#   into a set-of-sets representation. We use frozenset as the standard set() is mutable,
#   making it unhashable and thus unsuitable for inclusion in a set.
# input(s): two arguments of arbitrary type
# output(s): Boolean evaluation of the equivalence of the two arguments
#

def test_equivalent(a, b, funct_name):
    # we consider lists of lists to be the same as long as their contents are the same, 
    # ignoring order of both the outer and inner lists
    if funct_name == 'play':
        type_a = type(a)
        type_b = type(b)
        if type_a == type_b == str:
            return a == b
        elif type_a == type_b == tuple:
            return a[0] == b[0]
        else:
            return False
    if isinstance(a, list) and isinstance(b, list):
        try:
            return as_setset(a) == as_setset(b)
        except TypeError:
            # One of the items was not iterable, we fall back to standard equality
            return a == b
            
    # for everything else, we use the built-in notion of equality
    else:
        return type(a) == type(b) and a == b

#  
# end test_equivalent()   
####################################################################################

####################################################################################
#
# name: as_setset()
#
# synposis: convert a list-of-lists into a set of sets. This is to facilitate
#   order-agnostic checking of output.
# input(s): a list of lists
# output(s): a frozenset of frozensets 
#

def as_setset(seq):
    return frozenset(frozenset(s) for s in seq)

#  
# end as_setset()   
####################################################################################




def test_all(testset):
    for fn_name in sorted(testset.test_cases): 
        # if submission implements the given function
        if hasattr(submission, fn_name):
            test(fn_name,testset)
        else:
            print("No implementation for '{0}'".format(fn_name))



# A module's __name__ is set to __main__ when it is imported at the top level 
# (i.e. not by another module)
if __name__ == "__main__":
    test_all(tests)
    try:
        test_all(tests_extra)
    except NameError:
        pass

