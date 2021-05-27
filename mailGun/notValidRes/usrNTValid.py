__project__ = 'MFAAuto'
__author__ = 'DeVaa'
__descript__ = "Copyright (c) 2021 Ozzius(deb991)"
__URL__ = 'https://github.com/deb991/'
__NB__ = 'For more information, please see github page & all commit details.'
__CipherSig__ = 'This project & all associate files are encrypted under PBEncryption cryptography. Another details will be available at the end of this pgogram.'

from datetime import datetime, date

import win32com.client as win32

now = datetime.now()


def usrNTValid():
    today = date.today()
    outlook = win32.Dispatch ( 'outlook.application' )
    mail = outlook.CreateItem ( 0 )
    mail.To = 'debashis.d.biswas@shell.com'
    #mail.Cc = ''
    #mail.Cc = ''
    #mail.Bcc = ''
    mail.Subject = 'User provided mail ID is not valid: User Input required::' + today.strftime("%d/%m/%Y")

    (mail.body) = 'Hi, \n\nKindly be informed that, the provided mail ID not not associated to Shell\n' \
                  'Please respond us back with Mail ID, which could be find as asociated to Shell\n' \
                  '\n\nThanks in advnace\nShell Global function Analyst team'
    mail.send

if __name__ == '__main__':
    usrNTValid()