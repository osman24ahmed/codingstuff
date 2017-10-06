class call(object):
    def __init__(self, id, name, number, time, reason,):
        self.id = id
        self.name= name
        self.number = number
        self.time = time
        self.reason = reason

    def display(self):
        printStr = '\nId:'+ self.id
        printStr += '\nName:'+ self.name
        printStr += '\nNumber:'+ self.number
        printStr += '\nTime:'+ self.time
        printStr += '\nReason:'+ self.reason
        print printStr


class callcenter(object):
    def __init__(self)
        self.calls = []
        self.size = len(self.calls)

    def add(self, call):
        self.calls.apennd(call)
        self.size = len(self.calls)

    def info(self):
        for i in range(0, self.size):
            print self.calls[i].name + " "+ self.calls[i].number


    def remove(self):
        self.calls.pop(0)
        self.size = len(self.calls)



















call1 = call('1','ahmed','555-555-5555', '5:20', 'bill')
call2 = call('1','fred','552-555-5555', '5:21', 'bills')
call3 = call('1','greg','555-555-5555', '5:20', 'bill')
call4 = call('1','steve','552-555-5555', '5:21', 'bills')
print call1
call1.display()
cen1 = callcenter()
cen1.add(call1)
cen1.add(call2)
cen1.infor()