#Reloading a module using reload() of importlib module
from importlib import reload
import time
import Module1
print("This program is going to sleep state for 30 s")
time.sleep(30)
reload(Module1)
import Module1
print("After reloading the Module1")
