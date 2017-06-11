'''
Created on 10.06.2017

@author: Jascha Riedel
'''
from PyQt5.Qt import QPushButton



class Button(QPushButton):

    
    
    
    def __init__(self, text, parent):
        super().__init__(text, parent)
        
        self.initUi()
    
    def initUi(self):
        pass
    