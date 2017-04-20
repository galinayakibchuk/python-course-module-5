from lab_work_5.lab_work_5_2.main import *

def function_one(variable: str):
    print('function one call!')

def function_two(variable: str):
    print("function two call: {path}!".format(path=variable))

pi = 3,14

if __name__ == '__main__':
    print('definitions module executed!')
    print('PI = ', pi)
    function_one()

