__project__ = 'MFAAuto'
__author__ = 'DeVaa'
__descript__ = "Copyright (c) 2021 Ozzius(deb991)"
__URL__ = 'https://github.com/deb991/'
__NB__ = 'For more information, please see github page & all commit details.'
__CipherSig__ = 'This project & all associate files are encrypted under PBEncryption cryptography. Another details will be available at the end of this pgogram.'

import datetime as dt
import re

import win32com.client

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
    inboxMail_body = inboxMail.body

    # Flag: 1 ::::::::::::::::::::::
    print('>>>>>>>>>Inbox checking<<<<<<<<')
    print(inboxMail, "\nMail Count:", inboxMail_count, '\n', inboxMail_Sub, '\n')
    ##==============================

    lastQtrMessages = inboxMails.Restrict("[ReceivedTime] >= '" + lastQtrTIme.strftime('%m/%d/%Y %H:%M %p') + "'")

    for inboxMail in lastQtrMessages:
        print(inboxMail_Sub)
        #print(inboxMail.ReceivedTime)
        inboxMail = lastQtrMessages.GetFirst()
        inboxMail_iter = lastQtrMessages.GetNext()
        print('\n')
        bodyData = inboxMail.body

    while inboxMail:
        for inboxMail in lastQtrMessages:
            if inboxMail.unread == True:
                print('Initiating Main process -- flag 1.1')
                mfaSrch = re.search(r"MFA", inboxMail.body) #Used
                mfaSrch_small = re.search(r"mfa", inboxMail.body)

                newsCredSubMFA = re.search(r'MFA', inboxMail.Subject)  #Used
                newsCredSubApp = re.search(r'News', inboxMail.Subject) #Used

                newsCredSubKWrdA = re.search(r'mfa', inboxMail.Subject) #Used
                newsCredSubKWrdB = re.search(r'Cred', inboxMail.Subject) #Used

                newsCredSubKWrdC = re.search(r'authentication', inboxMail.Subject)
                newsCredSubKWrdD = re.search(r'authenticator', inboxMail.Subject)

                newsCredSubKWrdE = re.search(r'denied', inboxMail.Subject)
                newsCredSubKWrdF = re.search(r'Shell Brand Applications', inboxMail.Subject)

                newsCredSubKWrdG = re.search(r'login', inboxMail.Subject)
                newsCredSubKWrdH = re.search(r'account', inboxMail.Subject)

                newsCredSubKWrdI = re.search(r'Lost', inboxMail.Subject)
                newsCredSubKWrdJ = re.search(r'mfa$', inboxMail.Subject)

                newsCredSubKWrdK = re.search(r'MFA Support', inboxMail.Subject)

                newsCredSender = re.search(r'creativehub@shell.com', inboxMail.SenderEmailAddress)


                if newsCredSender:
                    print('First checking Mail sender :: ')
                    print(newsCredSender)
                    break




                #if mfaSrch:
                #    print('Match found>>> \t')
                #    print(mfaSrch.group())
                #    print("<<Email extraction started >>")
                #    mailIDs = re.findall('\S+@\S+', inboxMail.body)
                #    print(mailIDs)
                #    print(newsCredSender)

                if newsCredSubMFA or newsCredSubKWrdA:
                    print('Match found MFA/ mfa keyword >>')
                    print(newsCredSubMFA.group() or newsCredSubKWrdA.group())
                    mailIDs = re.findall('\S+@\S+', inboxMail.body)
                    print(mailIDs)
                    print(newsCredSender)



                #elif mfaSrch_small:
                #    print('Match found in small Case >>> \t')
                #    print(mfaSrch_small.group())
                #    print("<<Email extraction started for small case >>")
                #    mailIDs = re.findall('\S+@\S+', inboxMail.body)
                #    print(mailIDs)
                #    print(newsCredSender)
                #    break

                elif  newsCredSubApp or newsCredSubKWrdB:
                    print('Match found APP Name keyword >>')
                    print(newsCredSubMFA.group() or newsCredSubKWrdA.group())
                    mailIDs = re.findall('\S+@\S+', inboxMail.body)
                    print(mailIDs)
                    print(newsCredSender)


        break




    print('\tEOF')


if __name__ == '__main__':
    usrInbox()
    #gssFMB()