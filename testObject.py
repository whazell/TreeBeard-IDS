from nnbuilder import *
from databaseObject import *
from nntrainer import *
from testingHandlerMultithreaded import *
# from testingHandler import *
import numpy as np

testHandler = testingHandler("exampleSchema");
testHandler.testWholeNetwork();


# arr = [1, 2, 3, 4, 5, 6]
# blah = np.array_split(arr, 3)
# print(blah)
# for blag in blah:
# 	print(blag)
