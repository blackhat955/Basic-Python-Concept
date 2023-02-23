# working on the file system
# with is keyword called context manager

with open('main.py', 'r') as f:
    f_content=f.readline()
    print(f_content)
    pass


def OpenAfile():
    f = open('main.py', 'r')
    print(f.name)
    print(f.close())
    print(f.mode)


OpenAfile()
