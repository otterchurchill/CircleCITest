import unittest
from scopeChecker import scopeCheck


class testScopeCheck(unittest.TestCase):
    
    scopeMatch = { ')':'(', ']':'[', '}':'{' } 

    
    def testTrues(self):
        correctSeqs = ["{()[]}", "{{{{{(){}[]}}}}}", "{[()][]}"]
        for seq in correctSeqs:
            print(seq)
            self.assertIs(scopeCheck(seq, self.scopeMatch),True)
    
    def testFalses(self):
        invalidSeqs = ["]}","[{}", "{([)]}", "{[(]}", "[{})]"]
        for seq in invalidSeqs:
            print(seq)
            self.assertIs(scopeCheck(seq, self.scopeMatch),False)


if __name__ == '__main__':
    unittest.main()
