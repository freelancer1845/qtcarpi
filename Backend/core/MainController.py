'''
Created on 11.06.2017

@author: jasch
'''
from PyQt5.Qt import QObject, pyqtSignal
from PyQt5.QtCore import Qt, QMessageLogger, qDebug
import logging



class MainController(QObject):
    '''
    Main Control of the backend. Connects GUI with backend.
    '''
    STATE_IDLE = 0
    STATE_FM = 1
    STATE_AUX = 2
    STATE_MEDIA = 3

    
    state = STATE_IDLE
    
    testSignal = pyqtSignal()
    stateChangedSignal = pyqtSignal(int, name='stateChanged')
    
    statusLabelChangedSignal = pyqtSignal(str, name='statusLabelChanged')

    alreadyCreated = False
    
    INSTANCE = None;


    
    def __init__(self):
        '''
        Constructor
        '''
        super().__init__()
        if self.INSTANCE is not None:
            raise RuntimeError('Tried to create MainController multiple times!')
           
        
        self.connectSignals()
    
    @classmethod
    def getInstance(cls):
        if cls.INSTANCE is None:
            cls.INSTANCE = MainController()
        return cls.INSTANCE
    
    def connectSignals(self):
        self.stateChangedSignal.connect(self.handleStateChangedSignal)
    
    def changeState(self, newState):
        if self.state is not newState:
            self.stateChangedSignal.emit(newState)
            
    def handleStateChangedSignal(self, newState):
        self.state = newState
        logging.getLogger().debug('New state for MainController: ' + str(newState))
        
    def changeStatusLabel(self, text):
        self.statusLabelChangedSignal.emit(text)
    
    
    
    
        
        