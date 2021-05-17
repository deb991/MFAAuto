__project__ = 'MFAAuto'
__author__ = 'DeVaa'
__descript__ = "Copyright (c) 2021 Ozzius(deb991)"
__URL__ = 'https://github.com/deb991/'
__NB__ = 'For more information, please see github page & all commit details.'
__CipherSig__ = 'This project & all associate files are encrypted under PBEncryption cryptography. Another details will be available at the end of this pgogram.'

from datetime import datetime, date

import win32com.client as win32

now = datetime.now()


def mailIDReq():
    today = date.today()
    outlook = win32.Dispatch ( 'outlook.application' )
    mail = outlook.CreateItem ( 0 )
    mail.To = 'debashis.d.biswas@shell.com'
    #mail.Cc = 'INNNIA@SHELL.com; Kishalaya.Nath@shell.com'
    #mail.Cc = 'receipents; receipents'
    #mail.Bcc = ' P.PallaviBharti@shell.com'
    mail.Subject = '<<Mail ID request to provide from USER>>' + today.strftime("%d/%m/%Y")

    # F = open(os.path.expanduser(os.getenv('USERPROFILE')) + 'path')
    # line = F.read()

    (mail.body) = 'Hi,\n Kindly share your mail ID associated with your current employeer. \n\nThanks in advance.\nShell Global function'
    mail.send

if __name__ == '__main__':
    mailIDReq()