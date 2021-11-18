from typing import Text
import unittest
import subprocess

class TestStringMethods(unittest.TestCase):
    def test_code(self):
        subprocess.Popen(["powershell.exe", "python Ex1.py input\Ex1_Buildings\B3.json input\Ex1_Calls\Calls_a.csv myOutput.csv"])
        
        subprocess.Popen(["powershell.exe", "java -jar lib\Ex1_checker_V1.2_obf.jar 207296989,209530583 " + "input\Ex1_Buildings\B3.json" + "  " + "myOutput.csv" + "  outputFormTEster.log >testResults.txt"])
        
        with open('expectResults.txt') as f:
            exp = f.read()
        
        with open('testResults.txt') as f:
            res = f.read()
        
        self.assertEqual(exp, res)  
if __name__ == '__main__':
    unittest.main()
        
        
         