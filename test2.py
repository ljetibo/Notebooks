import inspect



class InspectIt():
    
    def __init__(self, object):
        self.obj = object
        self.classes = inspect.getmembers(object, predicate=inspect.isclass)

        #self.methods command is similar to:
        #
        #self.methods = dict()
        #for owner_class in self.classes:
        #   owner = owner_class[0]
        #   clas =  owner_class[1]#(1)
        #   self.methods[owner] = inspect.getmembers(clas, predicate=inspect.isfunction)
        #
        #(1)classes are stored in list of tuples. 1st entry is name of the class.
        #(1)2nd entry is the actual class as an object you can reference and call, 
        #i.e. class = class_owner[1], class()--> <class 'module.class_name'>
        #
        #getmembers cannot look into classes unless we send it class as an object (module.class)
        #ismethod only works if there's an instance of a class. Pass a class as an object
        #and then look for functions and store them as methods.
        #
        #i.e. inspect.ismethod(InspectIt.getcode)-->False
        #     inspect.ismethod(InspectIt(your_module).getcode)-->True
        #
        #bellow we do the same just: {y for x in self.classes}
        #where y is the dict expresion
        #we get a dictionary with class names for keys
        #and lists of tuples(method_name, method_object) of those classes for values
        #dict( owner_class_name: list of tuples all methods belonging to the class  )  )
        #{"Class1": list(  (class1_method1_name, method_as_object), (class1_method2_name, method_as_object)  
        # "Class2": list(  (class2_method1_name, method_as_object), (class2_method2_name, method_as_object)
        #      ...}

        self.methods ={
            #class name      #get just functions from gotten object
                                        #get class from module, as object
            owner[0]:inspect.getmembers(owner[1], predicate=inspect.isfunction)
            for owner in self.classes #run through all classes in module
            }

        self.functions = inspect.getmembers(object,
                                            predicate=inspect.isfunction)
        self.snippets = inspect.getmembers(object, predicate=inspect.iscode)

        
    
    def _print_block(self, start, read):
        n_tabs = inspect.indentsize(read[start])
        in_block=True
        print(read[start-1], end="")#firstlineno gets set after declaration
        while in_block:             #go back 1 line to include it
            for char in range(n_tabs):
                try:
                    if read[start] == "\n":
                        start+=1
                    if read[start][n_tabs:n_tabs+3] == '"""':
                        while not read[start].endswith('"""\n'):
                            print(read[start], end="")
                            start+=1
                        start+=1
                    if read[start][char] != " ":
                        in_block=False
                    else:
                        print("TU SAM")
                        print(read[start], end="")
                        start+=1
                        
                except:
                    pass
        

    def _get_func_code(self, name):
        file = open(self.obj.__file__)
        read = file.readlines()
        func = getattr(self.obj, str(name)).__code__
        func_line = func.co_firstlineno
        self._print_block(func_line,read)
        
            
    def _get_method_code(self, owner, name):
        print("Method {} of clas {}\n".format(name, owner))
        file = open(self.obj.__file__)
        read = file.readlines()
        clas = getattr(self.obj, owner)
        func = getattr(clas, str(name)).__code__
        func_line = func.co_firstlineno
        self._print_block(func_line, read)
        print("\n\n")


    def get_code(self, name, owner_class=False):
        found = False
        for func in self.functions:
            if name == func[0]:
                self._get_func_code(name)
                found = True
                
        if owner_class:
            try:
                self._get_method_code(owner_class, name)
                found = True
            except:
                return("No methods of functions found")
        else:
            try:
                for owner, methods in self.methods.items():
                    for method_name, method in methods:
                        if method_name == name:
                            self._get_method_code(owner, method_name)
                            found = True
            except:
                pass

        if not found:
            raise NameError("No methods or functions with that name found")

    def _print_class_methods(self):
        for clas in self.classes:
            print("Class:", end="\t")
            print(clas[0])
            for method1, method2 in zip(self.methods[clas[0]][0::2],self.methods[clas[0]][1::2]) :
                print("\t\t{0:^25s}  ||  {1:^25s}".format(method1[0],method2[0]))
                #if your function has more than 25 characters you're doing
                #something wrong
        
    def _print_func(self):
        print("Functions:")
        for func1, func2 in zip(self.functions[0::2],self.functions[1::2]) :
            print("\t{0:<25s}  ||  {1:<25s}".format(func1[0],func2[0]))
            #if your function has more than 25 characters you're doing
            #something wrong


    @property
    def summary(self):
        self._print_class_methods()
        print()
        self._print_func()
        
        
        

        
        
def func():
    print("test")

class DrugaZaTest():
    """This is just some doc_string
with crappy indentation. Why are you even reading this?"""
    def __init__(self):
        pass


import test, hello
proba = InspectIt(inspect)
pro = InspectIt(test)
