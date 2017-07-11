'''
Created on 10.06.2017

@author: Jascha Riedel
'''
from PyQt5.Qt import QApplication, QFontDatabase
from Gui.MainWindow import MainWindow
from Backend.core.MainController import MainController
from PyQt5.QtCore import qCritical
import logging


class MainApplication(QApplication):
    '''
    The Qt Application starting point.
    '''


    def loadSkin(self):
        
        try:
            with open('resources/skin.css', 'r') as handle:
                skinCss = handle.read()
                self.setStyleSheet(skinCss)
        except IOError:
            qCritical('Failed to load skin file.')
    
    
    def __init__(self, argv):
        '''
        Constructor
        '''
        super().__init__(argv)
        
        #set log level
        logging.basicConfig(level= logging.DEBUG)
        
        #set the skin
        self.loadSkin()
        
        #Create the MainController
        self.mainController = MainController()
        
        # Create the Main Window
        self.mainWindow = MainWindow()
        