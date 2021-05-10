__project__ = 'MFAAuto'
__author__ = 'DeVaa'
__descript__ = "Copyright (c) 2021 Ozzius(deb991)"
__URL__ = 'https://github.com/deb991/'
__NB__ = 'For more information, please see github page & all commit details.'
__CipherSig__ = 'This project & all associate files are encrypted under PBEncryption cryptography. Another details will be available at the end of this pgogram.'

import os
import win32com.client as win32
from datetime import datetime, date

now = datetime.now()

#FilePath = 'C:\\Users\\Debashis.D.Biswas\\PycharmProjects\\EASFOM\\COCR_HC\\dump\\webTestScreenShotProd'
#os.chdir(FilePath)
#filesNew = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
# oldest = filesNew[0]
#newest = filesNew[-1]

#attData = os.path.isfile(newest)


##Checking Newest File for acknowledgement.
#FilePath = 'C:\\Users\\Debashis.D.Biswas\\PycharmProjects\\EASFOM\\COCR_HC\\dump\\webTestScreenShotProd'
#os.chdir(FilePath)
#filesNew = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
# oldest = filesNew[0]
#newest = filesNew[-1]
# print "Oldest:", oldest
#print("Newest:", newest)
#print("All by modified oldest to newest:", filesNew)


##Checking Newest File for acknowledgement.
#FilePath_UAT = 'C:\\Users\\Debashis.D.Biswas\\PycharmProjects\\EASFOM\\COCR_HC\\dump\\webTEstScreenSHotUAT'
#os.chdir(FilePath_UAT)
#filesNew_UAT = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
# oldest = filesNew[0]
#newest_UAT = filesNew_UAT[-1]
# print "Oldest:", oldest
#print("Newest:", newest_UAT)
#print("All by modified oldest to newest:", filesNew_UAT)

def MailGun():
    today = date.today()
    outlook = win32.Dispatch ( 'outlook.application' )
    mail = outlook.CreateItem ( 0 )
    mail.To = 'debashis.d.biswas@shell.com'
    #mail.Cc = 'INNNIA@SHELL.com; Kishalaya.Nath@shell.com'
    # mail.Cc = 'receipents; receipents'
    #mail.Bcc = ' P.PallaviBharti@shell.com'
    mail.Subject = 'User Cant login to CredNews Protal - MFA' + today.strftime("%d/%m/%Y")

    #attachment = (os.path.expanduser(os.getenv('USERPROFILE')) + "\\PycharmProjects\\EASFOM\\COCR_HC\\dump\\webTestScreenShotProd\\" + newest)
    #attachment_UAT = (os.path.expanduser(os.getenv('USERPROFILE')) + "\\PycharmProjects\\EASFOM\\COCR_HC\\dump\\webTEstScreenSHotUAT\\" + newest_UAT)
    #attachment =
    #mail.Attachments.Add(attachment)
    #mail.Attachments.Add(attachment_UAT)

    # F = open(os.path.expanduser(os.getenv('USERPROFILE')) + 'path')
    # line = F.read()

    (mail.body) = 'MFA'
    mail.send

if __name__ == '__main__':
    MailGun ()