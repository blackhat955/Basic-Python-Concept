
value=int(input("Enter the input to choose right class:  "))


class working:
    def lima(self, name: str, Lname:str, age: int):
        """

        :type age: int
        """
        self.name = name
        self.Lname = Lname
        self.age = age
        print("Welcome to the Party Mr" + name + Lname + "and your age" +age)
        print(type(age))
        # Working with strings

        # Single quote not working in python correct because it interpret not properly
        # count, find, replace, uppper, lower all are methods for doing cool stuff with strings
    def Concatinate(self):
        print("You are inside of Concatinate Function=====>")
        message = 'Hellow World'
        print(message.find('Hellow'))
        # how to concatinate the resultant string
        greeting = 'Hellow'
        name = "Durgesh"
        message = '{},{}. Welcome!'.format(greeting, name)  # this is another way to concatinate the strings
        print(message)
        # Or we can use morden  f  method
        message=f'{greeting},{name}. Welcome!'
        print("This is printing using new formating method" +message)

        # we have dir method which can help you know all associated function with that variable

        print(dir(name))
        # get more info you can use help

        print(help(str))
    def int_float(self):
        # round method used to round to it nearest value
        print(round(3.55))

    def list(self):
        course=['History','Math','Physics','CompSci']
        print(course)#==>4
        print(course[0])#==History
        print(course[-1])#== reverse list as output

        for item in course:
            print(item)
        print(course[0:2])#==> 0 inclusive and 2 inexclusive index

        print(course[2:])#==> starting from 2 all the way to end this method called slcing

        # add element on the list append and this add element in the last
        # to add element at the specific point than use insert method

        course.insert(0,'Art')
        print(course)# add single element at the starting index
        # you can also add a another list with insert method

        course1=['Geo','Commer']
        course.insert(0,course1)
        print(course)

        # her we have an extend method to join two list
        course.extend(course1)#==> join two list as output
        print(course)

        # Remove values form list

        course.remove('Math')
        # pop method
        k=course.pop()#==> it return value it deleted
        print(k)

        # to reverse the list
        print("============Revese=========")
        print(course.reverse())

        # difference between sort and sorted method
        # sort-> sort the existing list where sorted-> return a new list with sorted element
        # k=sorted(course)
        # print(k)
        # print(course.sort())

        for items in course:
            print("this is just print the values{0}".format(items))

        for index, course in enumerate(course):
            print(f'This is printed both index & course:  {index},{course}')

        # .join method
        course_str = '-'.join(course)
        print(course_str)

    # list is mutable and tipple are not mutable
    def tuple_set(self):
        # to create empty tuple we can use tuple_1=() that's it
        tuple_1=('History','Math','Physics','CompSci')
        tuple_2=tuple_1
        print(tuple_1)
        print(tuple_2)
        # we can't modify tuple

        x=int(input("want to check immutability Enter 1  :"))

        if x==1:
            tuple_1[0] = 'Art'  # this will give you error

    def set(self):
        # to create an empty set use can't do like set={} thie creats and empty dictionary insted use set_1=set() this is an inbulit tool come with python
        # set won't care about the indexing of the value so becuse of this each time you try to print the set will get different result
        # like you get different element at first index at each time
        # this is set and seaching an element in the set is more efficient as compare to the doing same prcess in the list and tuple
        course = {'History', 'Math', 'English', 'Math', 'Math', 'English'}
        course_art={ 'Math', 'English', 'English','Art','geography'}
        print(course)
        # searching in set using in operator is quite effiecient when it come in terms of time compare to ot rivival List and tuple
        print('Math' in course)
        # it has intersection mehtod to find what's common between two sets
        print(course.intersection(course_art))
        # take union of  the sets
        print(course.union(course_art))

    def dictionary(self):
        print('thie is a dictionary')
        student={'name':'durgesh','age':23,'course':['Computer Science','Information Technology']}
        print(type(student))
        # the get method print the value if the key is exist in the dictionary otherwise it print none
        print(student.get('name'))
        print(student['course'])# this is also a method to get access of the values stored in the dictionaries
        # add new elemet into the dictionary
        student['phone']=234433344
        # to update the value
        student['name']='Om'
        # or you can update mutiple element at one go
        student.update({'name':'kuldeep','address':'Jaunpur'})
        print(student)
        # print the number of keys
        print(len(student))
        # to get the name of keys
        print(student.keys())
        # to print all the values
        print(student.values())
        # Loop throuh dictionaries
        for key in student:
            print('Printing keys in the dictionaries:  '+key)# this is only print the keys not value
        # to ge the values you can iterate in different way
        for key,val in  student.items():
            print(key, val) # this is printing key and value pair together

    def iteration_loop(self):
        nums=[1,2,3,34,4,5,6,7]
        for num in nums:
            print(num)

















d=working()# Class for working and Learning

if value==1:
    d.lima("Durgesh","Tiwari","23")
elif value==2:
    d.Concatinate()
elif value==3:
    d.int_float()
elif value==4:
    d.list()
elif value==5:
    d.tuple_set()
elif value==6:
    d.set()
elif value==7:
    d.dictionary()




