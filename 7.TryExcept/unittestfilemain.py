import unittest
#Importing the file whose function i want to test
import unittestfile1

#defining a class that contains the test cases which are being tested
class Name_of_test(unittest.TestCase):
    
    #defining test cases
    def test_case1(self):
        #test case is defined here, what i want to test on my function
        test = "arjun verma"
        #result from that function is stored as result
        result = unittestfile1.function_to_be_tested(test)
        #result is being compared to expected reult aka what i expected the result to be!
        self.assertEqual(result,'Arjun Verma')
    
    def test_case2(self):
        test2 = "durgesh verma"
        result2 = unittestfile1.function_to_be_tested(test2)
        self.assertEqual(result2,'Durgesh Verma')

##It would print OK because all the tests are passed!    
if __name__ == "__main__":
    unittest.main()