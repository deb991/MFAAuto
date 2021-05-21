__project__ = 'MFAAuto'
__author__ = 'DeVaa'
__descript__ = "Copyright (c) 2021 Ozzius(deb991)"
__URL__ = 'https://github.com/deb991/'
__NB__ = 'For more information, please see github page & all commit details.'
__CipherSig__ = 'This project & all associate files are encrypted under PBEncryption cryptography. Another details will be available at the end of this pgogram.'

from flask import Flask

Tracker = Flask(__name__)
@Tracker.route('/')

def mFunc():
    print('Tracker has been Initiated!!')
    return "Tracker"


if __name__ == '__main__':
    Tracker.run()
