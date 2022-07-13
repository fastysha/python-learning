import unittest

def equal_lists(list1,list2)->bool:
    if len(list1) != len(list2):
        return False
    # for n1,n2 in zip(list1,list2):
    #     if n1!=n2:
    #         return False
    # return True
    for i in range(len(list1)):
        num1=list1[i]
        num2=list2[i]
        if num1!=num2:
            return False
    return True

        

class TestEqualFunction(unittest.TestCase):
    def test_two_equal_list(self):
        self.assertTrue(equal_lists([1,2,3,4,5],[1,2,3,4,5]))
    def test_two_empty_list(self):
        self.assertTrue(equal_lists([],[]))
    def test_one_empty_list(self):
        self.assertFalse(equal_lists([1,2,3,4,5],[]))
    def test_one_reverse_list(self):
        self.assertFalse(equal_lists([1,2,3,4,5],[5,4,3,2,1]))
unittest.main()
    



            

            

