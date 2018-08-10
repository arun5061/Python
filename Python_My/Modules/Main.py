print("This is Main module importing Module1")
import Module1
print('Explictly calling function in Module1')
Module1.f1()
import time
from imp import reload
print("Entering into sleep first time")
time.sleep(0)
reload(Module1)
print("Entering into sleep second time")
time.sleep(0)
reload(Module1)

'''
Output for above program:
This is Main module importing Module1
Hello this is Module 1
Initial version-2
Explictly calling function in Module1
Hello this is Module 1
Entering into sleep first time
Hello this is Module 1
Initial version-1
Entering into sleep second time
Hello this is Module 1
Initial version-2
'''
