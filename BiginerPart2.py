from ModuleImport import find_index, WorkigWithOSModule as os,printingEnvovariable
value=int(input("Enter the value to check:  "))
class TestingOtherTwo():
    def hello_func(self):
        print('Hello function')
    def functionwithdefaultArgument(self,greetin,name='You'):
        message=f'{greetin},{name} welcome'
        print(message)
    def student_info(self,*args,**kwargs):
        print(args) # ==> tuple ('Math', 'Phy')
        print(kwargs) # ==> dictionary {'name': 'Durgesh', 'age': 23}

    def Call_A_modulefuctionWhich_youCreated(self):
        course=[1,2,3,4,5,6,6,7,10]
        val=find_index(course,int(input("Enter A value to check  :")))
        print(val)

    def OsModule(self):
        os()
    def EnvromentVaribale(self):
        printingEnvovariable()








# this called keep your code dry ++ not repeat your code

test=TestingOtherTwo()

if value==1:
    test.hello_func()
elif value==2:
    test.functionwithdefaultArgument('durgesh')# here i not passing 2nd argument but i didn;t get error because I set a default value there
elif value==3:
    # test.student_info('Math','Phy',name='Durgesh',age=23)
    # or you can do this way
    course=['Math', 'Phy']
    info={'name': 'Durgesh', 'age': 23}
    # this way you can pass list and dictionary for fo *args and **kwargs
    test.student_info(*course, **info)
    # this is for the test perpose
elif value==4:
    test.Call_A_modulefuctionWhich_youCreated()
elif value==5:
    test.OsModule()
elif value==6:
    test.EnvromentVaribale()
