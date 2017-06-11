'''
Created on 10.06.2017

@author: Jascha Riedel
'''

import sys
from MainApplication import MainApplication


if __name__ == '__main__':
    
    app = MainApplication(sys.argv)
    
    sys.exit(app.exec_())
