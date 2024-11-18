import pyqrcode 

name = 'https://github.com/maazrana028'
k = pyqrcode.create(name)
k.png('GitHub.png',scale = 10)

import os
os.system('GitHub.png')
