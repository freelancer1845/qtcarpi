'''
Created on 10.06.2017

@author: Jascha Riedel
'''
from PyQt5 import QtCore
from PyQt5.Qt import QApplication, QFontDatabase
from Gui.MainWindow import MainWindow
from Backend.core.MainController import MainController
from PyQt5.QtCore import qCritical
from PyQt5.QtCore import qDebug
from PyQt5.QtCore import QtInfoMsg
from PyQt5.QtCore import QtWarningMsg
from PyQt5.QtCore import QtCriticalMsg
from PyQt5.QtCore import QtFatalMsg
import logging


class MainApplication(QApplication):
    '''
    The Qt Application starting point.
    '''


    def loadSkin(self):
        qDebug('Loading skin...')
        try:
            with open('resources/skin.css', 'r') as handle:
                skinCss = handle.read()
                self.setStyleSheet(skinCss)
        except IOError as err:
            qCritical('Failed to load skin file.')
    
    
    def __init__(self, argv):
        '''
        Constructor
        '''
        super().__init__(argv)
        
        #initalize sysout logging
        QtCore.qInstallMessageHandler(MainApplication.qt_message_handler)
        
        #set log level
        logging.basicConfig(level= logging.DEBUG)
        
        #set the skin
        self.loadSkin()
        
        #Create the MainController
        self.mainController = MainController()
        
        # Create the Main Window
        self.mainWindow = MainWindow()
        
    @classmethod
    def qt_message_handler(cls, mode, context, message):
        if mode == QtInfoMsg:
            mode = 'INFO'
        elif mode == QtWarningMsg:
            mode = 'WARNING'
        elif mode == QtCriticalMsg:
            mode = 'CRITICAL'
        elif mode == QtFatalMsg:
            mode = 'FATAL'
        else:
            mode = 'DEBUG'
        print('qt_message_handler: line: %d, func: %s(), file: %s' % (
            context.line, context.function, context.file))
        print('  %s: %s\n' % (mode, message))
        
        