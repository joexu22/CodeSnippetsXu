import unittest
        
def generateList(n):
    numberList = []
    for x in range(n):
        numberList.append(x)
    return numberList

def fermat_little_theorem_explorer(n):
    numberList = generateList(n)
    for i in numberList:
        numberList[i] = numberList[i]**n
    return numberList

def moduloList(n):
    originalNumbers = generateList(n)
    numberList = fermat_little_theorem_explorer(n)
    moduloList = [e % n for e in numberList]
    # assert(originalNumbers == moduloList)
    return moduloList;

class TestFeratLittleTheroem(unittest.TestCase):
    def test_generateList(self):
        TestInput = 9
        TestArray = [0,1,2,3,4,5,6,7,8]
        self.assertEqual(generateList(TestInput), TestArray)

    def test_fermat_little_theorem_explorer(self):
        TestInput = 9
        TestArray = [0,1,2,3,4,5,6,7,8]
        TestArrayOutput = [element ** TestInput for element in TestArray]
        # print(TestArrayOutput)
        self.assertEqual(TestArrayOutput, fermat_little_theorem_explorer(9))
        
    def test_moduloList(self):
        TestInputFail = 9
        TestGeneratedFail = generateList(TestInputFail)
        ModuloListFail = moduloList(TestInputFail)
        self.assertNotEqual(TestGeneratedFail, ModuloListFail)

        TestInputPass = 7
        TestGeneratedPass = generateList(TestInputPass)
        ModuloListPass = moduloList(TestInputPass)
        self.assertEqual(TestGeneratedPass, ModuloListPass)

if __name__ == '__main__':
    unittest.main()