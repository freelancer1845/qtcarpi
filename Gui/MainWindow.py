'''
Created on 10.06.2017

@author: Jascha Riedel
'''
from PyQt5.Qt import QWidget, Qt, QStyleOption, QPainter, QStyle,\
    QPushButton, QLabel
from PyQt5.QtCore import QCoreApplication
from Gui.Positions import *
from Backend.core.MainController import MainController

class MainWindow(QWidget):
    '''
    The MainWindow of the application opened by MainApplication
    '''
    
    alreadyCreated = False

    def __init__(self):
        if self.alreadyCreated is True:
            raise RuntimeError('The MainWindow may only be created Once!')
        self.alreadyCreated = True
        '''
        Constructor
        '''
        super().__init__()
        
        self.initUi()
        
        
    

    def initUi(self):
        self.setGeometry(50, 50, 1024, 600)
        self.setObjectName('MainWindow')
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        
        exitButton = QPushButton('Exit', self)
        exitButton.setObjectName("ExitButton")
        exitButton.resize(EXIT_BUTTON_WIDTH, EXIT_BUTTON_HEIGHT)
        exitButton.move(EXIT_BUTTON_X, EXIT_BUTTON_Y)
        exitButton.clicked.connect(QCoreApplication.instance().quit)
        
        self.createMainControls()
        
        self.createStatusBar()
        
        self.createMiscControls()
        
       
        self.show()
        
    def createStatusBar(self):
        statusBar = QWidget(self)
        statusBar.setObjectName('StatusBar')
        statusBar.setGeometry(STATUS_BAR_X, STATUS_BAR_Y, STATUS_BAR_WIDTH, STATUS_BAR_HEIGHT)
        
        self.modeLabel = QLabel(self)
        self.modeLabel.setObjectName('ModeLabel')
        self.modeLabel.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.modeLabel.setText('Undefined')
        self.modeLabel.setGeometry(STATUS_MODE_X, STATUS_MODE_Y, STATUS_MODE_WIDTH, STATUS_MODE_HEIGHT)
        MainController.getInstance().stateChangedSignal.connect(lambda mode: self.handleModeChange(mode))
        
        infoLabel = QLabel(self)
        infoLabel.setObjectName('InfoLabel')
        infoLabel.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        infoLabel.setText('99.9 MHz')
        infoLabel.setGeometry(STATUS_INFO_X, STATUS_INFO_Y, STATUS_INFO_WIDTH, STATUS_INFO_HEIGHT)
        MainController.getInstance().statusLabelChangedSignal.connect(lambda text: infoLabel.setText(text))
        
        
        timeLabel = QLabel(self)
        timeLabel.setObjectName('TimeLabel')
        timeLabel.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        timeLabel.setText('17:22\t08.02.1993')
        timeLabel.setGeometry(STATUS_TIME_X, STATUS_TIME_Y, STATUS_TIME_WIDTH, STATUS_TIME_HEIGHT)
        ''' 
            TODO : Add some code that always displays the correct time.
        '''
    
    def createMainControls(self):
        radioButton = QPushButton('FM Radio', self)
        radioButton.resize(MAIN_CONTROLS_WIDTH, MAIN_CONTROLS_HEIGHT)
        radioButton.move(MAIN_CONTROLS_X_START, MAIN_CONTROLS_Y)
        radioButton.clicked.connect(lambda: MainController.getInstance().changeState(MainController.STATE_FM))
        
        
        auxButton = QPushButton('AUX', self)
        auxButton.resize(MAIN_CONTROLS_WIDTH, MAIN_CONTROLS_HEIGHT)
        auxButton.move(MAIN_CONTROLS_X_START + MAIN_CONTROLS_WIDTH + MAIN_CONTROLS_DISTANCE, MAIN_CONTROLS_Y)
        auxButton.clicked.connect(lambda: MainController.getInstance().changeState(MainController.STATE_AUX))
       
        mediaButton = QPushButton('Media', self)
        mediaButton.resize(MAIN_CONTROLS_WIDTH, MAIN_CONTROLS_HEIGHT)
        mediaButton.move(MAIN_CONTROLS_X_START + 2 * (MAIN_CONTROLS_WIDTH + MAIN_CONTROLS_DISTANCE), MAIN_CONTROLS_Y)
        mediaButton.clicked.connect(lambda: MainController.getInstance().changeState(MainController.STATE_MEDIA))
    
    
        
    def createMiscControls(self):
        '''
            TODO :    Create Play/Stop Skip Fast Forward etc. buttons. 
                      Also create methods in MainController that are connected
                      to the buttons and called if "click" or "clicked" signal is emitted.
                      The methods check the current state and act accordingly.
                      Also not all buttons should be enabled in the different modes. 
                      
                      Custom styled media buttons will be added later. QPushButton('Play', self)...
        '''
        
        '''
            TODO :    Create something to allow for easy volume change
        '''
        pass
    
    
    
    def handleModeChange(self, mode):
        if mode == MainController.STATE_FM:
            self.modeLabel.setText('FM Radio')
        elif mode == MainController.STATE_AUX:
            self.modeLabel.setText('AUX')
        elif mode == MainController.STATE_MEDIA:
            self.modeLabel.setText('Media')
        elif mode == MainController.STATE_IDLE:
            self.modeLabel.setText('Idle')
        else:
            self.modeLabel.setText('Unkown Mode: ' + str(mode))
    
        
        
    def paintEvent(self, *args, **kwargs):
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, o, p, self)
        
        return QWidget.paintEvent(self, *args, **kwargs)
