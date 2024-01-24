import argparse
import os
from cmd import Cmd


user_input = input("Command?")
if user_input == "list":
        path = os.getcwd() 
        
        # Get the list of all files and directories 
        dir_list = os.listdir(path) 
        
        print("Files and directories in '", path, "' :")  
        # print the list 
        print(dir_list)
        quit()

elif user_input == "exit":
        quit()
        
elif user_input == "help":
        print("add list exit help")
        quit()

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
parser.add_argument('--add', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')        


args = parser.parse_args()
print(args.accumulate(args.integers))