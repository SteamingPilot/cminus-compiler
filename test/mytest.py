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

fn = "./input/test_qs.cm"

print(getTreeNodeRep(cminus_parser.parse_program(fn)))
cminus_parser.compile_program(fn)

subprocess.run(["gcc", "-g", "-o", "./output/mytest", "./output/mytest.s"])
subprocess.run(["./output/mytest"])
