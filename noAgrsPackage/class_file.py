class StartStop:

    def __init__(self,function):
        self.function = function


    def call(self,*args):
        self.function(*args)