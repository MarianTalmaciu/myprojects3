from tkinter import *

def MyCalc(source, side):
    storeObj = Frame(source, borderwidth = 6, bd = 6, bg = 'light grey')
    storeObj.pack(side = side, expand = YES, fill = BOTH)
    return storeObj

def button(source, side, text, command = None):
    storeObj = Button(source, text = text, command = command)
    storeObj.pack(side = side, expand = YES, fill = BOTH)
    return storeObj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 24 bold')
        self.pack(expand = YES, fill = BOTH)
        self.master.title('Fast Calculator')

        display = StringVar()
        Entry(self, relief = GROOVE, textvariable = display, justify = 'right', bd = 32, bg = 'light grey').pack(side = TOP, expand = YES, fill = BOTH)

        for clearBut in (['C'],['CE']):
            erase = MyCalc(self, TOP)
            for ichar in clearBut:
                button(erase, LEFT, ichar, lambda storeObj = display, q = ichar: storeObj.set(''))

        for NumBut in ('789/', '456*', '123-', '0.+'):
            FunctionNum = MyCalc(self, TOP)
            for iEquals in NumBut:
                button(FunctionNum, LEFT, iEquals, lambda storeObj = display, q = iEquals: storeObj.set(storeObj.get() + q))

        EqualsButton = MyCalc(self, TOP)
        for iEquals in '=':
            if iEquals == '=':
                btniEquals = button(EqualsButton, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease>', lambda e, s = self, storeObj = display: s.calc(storeObj), '+')
            else:
                btniEquals = button(EqualsButton, LEFT, iEquals, lambda storeObj = display, s = '%s'% iEquals: storeObj.set(storeObj.get() + s))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set('ERROR')

if __name__ == '__main__':
    app().mainloop()

