__project__ = 'MFAAuto'
__author__ = 'DeVaa'
__descript__ = "Copyright (c) 2021 Ozzius(deb991)"
__URL__ = 'https://github.com/deb991/'
__NB__ = 'For more information, please see github page & all commit details.'
__CipherSig__ = 'This project & all associate files are encrypted under PBEncryption cryptography. Another details will be available at the end of this pgogram.'

import os
import sys
import win32com.client
import datetime as dt
import re

##Current time
curTime = dt.datetime.now()
lastQtrTIme = dt.datetime.now() - dt.timedelta(minutes=30)
##############################################

outlook = win32com.client.Dispatch("Outlook.application")
mapi = outlook.GetNamespace("MAPI")

Inbox = mapi.Folders["debashis.d.biswas@shell.com"].Folders['Inbox']
##~~~~~~~~~~~~~~~User Inbox Details~~~~~~~~~~~~~~~~~##

##Find other Mail Boxes

for stor in win32com.client.Dispatch("Outlook.Application").Session.Stores:
    print('\nDisplaying FMB names\t')
    print( stor.DisplayName)
    print('\t\nEnd of Display Name')

##EOF

def usrInbox():
    inboxMails = Inbox.items
    inboxMails.sort("[ReceivedTime]", True)
    inboxMail = inboxMails.GetFirst()
    inboxMail_count = inboxMails.count
    inboxMail_Sub = inboxMail.Subject
    # inboxMail_body = inboxMail.body

    # Flag: 1 ::::::::::::::::::::::
    print('>>>>>>>>>Inbox checking<<<<<<<<')
    print(inboxMail, "\nMail Count:", inboxMail_count, '\n', inboxMail_Sub, '\n')
    ##==============================

    lastQtrMessages = inboxMails.Restrict("[ReceivedTime] >= '" + lastQtrTIme.strftime('%m/%d/%Y %H:%M %p') + "'")

    for inboxMail in lastQtrMessages:
        print(inboxMail_Sub)
        print(inboxMail.ReceivedTime)
        inboxMail = lastQtrMessages.GetFirst()
        inboxMail_iter = lastQtrMessages.GetNext()
        print('\n')
        bodyData = inboxMail.body

    while inboxMail:
        for inboxMail in lastQtrMessages:
            if inboxMail.unread == True:
                print('Initiating Main process -- flag 1.1')
                mfaSrch = re.search("^mfa", inboxMail.body)



        break




    print('\tEOF')







if __name__ == '__main__':
    usrInbox()
    #gssFMB()