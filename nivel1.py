import os
os.path.abspath(os.getcwd())

r = os.path.dirname(os.path.realpath(__file__))
print(r)