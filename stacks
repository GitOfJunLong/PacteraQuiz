class Stacks(object):
    def __init__(self):
        self.stack_arr = ['node']
 
    def l_pop1(self):
        n = self.stack_arr.index('node')

        if n == 0:
            print('Stack1 is empty.')
        else:
            self.stack_arr.pop(0)
 
    def r_pop1(self):
        n = self.stack_arr.index('node')

        if n == 0:
            print('Stack1 is empty.')
        else:
            self.stack_arr.pop(n - 1)
 
    def l_pop2(self):
        n = self.stack_arr.index('node')
        l = len(self.stack_arr)

        if n == l - 1:
            print('Stack2 is empty.')
        else:
            self.stack_arr.pop(n + 1)
    
    def r_pop2(self):
        n = self.stack_arr.index('node')
        l = len(self.stack_arr)

        if n == l - 1:
            print('Stack2 is empty.')
        else:
            self.stack_arr.pop(-1)
    
    def l_push1(self, data):
        self.stack_arr.insert(0, data)
 
    def r_push1(self, data):
        n = self.stack_arr.index('node')
        self.stack_arr.insert(n - 1, data)
    
    def l_push2(self, data):
        n = self.stack_arr.index('node')
        self.stack_arr.insert(n + 1, data)
    
    def r_push2(self, data):
        self.stack_arr.append(data)
