# How to import module and work with them
# You can also import a new module complete from a new location on your  computer
# sys module taking care for all of this
import sys

# sys.path.append() and you can add address of the package which on differe location on your pc here
import  os as sys

print('This is show how to work with module in the python...')

def find_index(to_search,target):
    for i,val in enumerate(to_search): # enumerate fuction use to render the list value and as output it return index and value of the list respectively
        if val==target:
            return 1
    return -1

def WorkigWithOSModule():
    # what is os file to capable of
    print(dir(sys))
    print('We are working with module which is capable of doing OS Level Task:    ')
    print("sys.getcwd() This will give your current working directory"+sys.getcwd())
    # print("sys.chdir(sys.getcwd()) give coming  out one level up"+sys.chdir(sys.getcwd()))
    # print(sys.makedirs('Make/sun-make'))
    print(sys.listdir())
    # get modification time of the file
    from datetime import datetime
    mod_time=sys.stat('main.py').st_mtime
    print(datetime.fromtimestamp(mod_time))

    for dirpath,dirname,filename in sys.walk('C:\Program Files (x86)'):
        print(f'dir name of the pc:{dirname}' )
        print(dirpath)
        print(filename)
def printingEnvovariable():
    print(sys.environ.get('TMP'))


