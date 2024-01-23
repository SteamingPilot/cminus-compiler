import sys
import os
import unittest

# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name
# where the current directory is present.
ast = os.path.dirname(current) + "/ast"
parsep = os.path.dirname(current) + "/parser"

# adding the parent directory to
# the sys.path.

sys.path.append(ast)
sys.path.append(parsep)

from api import *
import cminus_parser as cminus_parser
import subprocess

class test_qs(unittest.TestCase):
      
    def test_qs(self):
        fn = "../input/test_qs.cm"
        self.assertEqual(cminus_parser.compile_program(fn),"Success");
        asm = fn.replace("input","output").replace(".cm",".s")
        run = asm.replace(".s","")
        cmd = ["/usr/bin/gcc","-o",run,asm]
        status = subprocess.run(cmd)
        self.assertEqual(status.returncode,0)
 
        out = asm.replace(".s",".out")
        fin = fn.replace(".cm",".in")
        f = open(out,"w")
        i = open(fin,"r")
        cmd = [run]
        status = subprocess.run(cmd,stdout=f,stdin=i)
        f.close() 
        self.assertGreaterEqual(status.returncode, 0)
 
        orig = out.replace("output","orig").replace(".out",".orig")
        cmd = ["/usr/bin/diff","-w","-B","-b",out,orig]
        status = subprocess.run(cmd)
        self.assertEqual(status.returncode,0)
    
if __name__ == '__main__':
    unittest.main()
