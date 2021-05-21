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

for stor in win32com.client.Dispatch("Outlook.Application").Session.Stores:
    #print('\nDisplaying FMB names\t')
    print('\nstor.DisplayName\t')
    print( stor.DisplayName)
    #print('\t\nEnd of Display Name')
    break

Inbox = mapi.Folders["debashis.d.biswas@shell.com"].Folders['Inbox']
##~~~~~~~~~~~~~~~User Inbox Details~~~~~~~~~~~~~~~~~##

def usrInbox():
    inboxMails = Inbox.items
    inboxMails.sort("[ReceivedTime]", True)
    inboxMail = inboxMails.GetFirst()
    inboxMail_count = inboxMails.count
    inboxMail_Sub = inboxMail.Subject
    inboxMail_body = inboxMail.body

    # Flag: 1 ::::::::::::::::::::::
    print('>>>>>>>>>Inbox checking<<<<<<<<')
    #print(inboxMail, "\nMail Count:", inboxMail_count, '\n', inboxMail_Sub, '\n')
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

                newsCredSender = re.search(r'creativehub', inboxMail.SenderEmailAddress)
                newsCredSenderATShell = re.search(r'@shell', inboxMail.SenderEmailAddress)

                newsCredSenderDEMO = re.search(r'debashis', inboxMail.SenderEmailAddress) #Used
                newsCredSenderDEMOATShell = re.search(r'@shell.com', inboxMail.SenderEmailAddress)   #Used

                mfaSrch = re.search(r"MFA", bodyData) #Used
                mfaSrch_small = re.search(r"mfa", bodyData)

                newsCredSubMFA = re.search(r'MFA', inboxMail.Subject)  #Used
                newsCredSubApp = re.search(r'News', inboxMail.Subject) #Used

                newsCredSubKWrdA = re.search(r'mfa', inboxMail.Subject) #Used
                newsCredSubKWrdB = re.search(r'Cred', inboxMail.Subject) #Used

                newsCredSubKWrdC = re.search(r'authentication', inboxMail.Subject) #Used
                newsCredSubKWrdD = re.search(r'authenticator', inboxMail.Subject)  #Used

                newsCredSubKWrdE = re.search(r'denied', inboxMail.Subject)         #Used
                newsCredSubKWrdF = re.search(r'Shell Brand Applications', inboxMail.Subject)  #Used

                newsCredSubKWrdG = re.search(r'login', inboxMail.Subject)  #Used
                newsCredSubKWrdH = re.search(r'account', inboxMail.Subject) #Used

                newsCredSubKWrdI = re.search(r'Lost', inboxMail.Subject)
                newsCredSubKWrdJ = re.search(r'mfa$', inboxMail.Subject)

                newsCredSubKWrdK = re.search(r'MFA Support', inboxMail.Subject)

                if  newsCredSenderDEMO or newsCredSenderDEMOATShell:
                    print('First checking Mail sender :: ')
                    print('Sender Mail:\t', newsCredSenderDEMO or newsCredSenderDEMOATShell)
                    break


                #if mfaSrch:
                #    print('Match found>>> \t')
                #    print(mfaSrch.group())
                #    print("<<Email extraction started >>")
                #    mailIDs = re.findall('\S+@\S+', inboxMail.body)
                #    print(mailIDs)
                #    print(newsCredSender)

                elif newsCredSubMFA or newsCredSubKWrdA:
                    print('Match found MFA/ mfa keyword in Subject: >>')
                    print("Keyword match found: \t",newsCredSubMFA.group() or newsCredSubKWrdA.group())
                    mailIDs = re.findall('\S+@\S+', inboxMail.body)
                    print(mailIDs)
                    print('Sender Mail:\t', newsCredSender)
                    break


                #elif mfaSrch_small:
                #    print('Match found in small Case >>> \t')
                #    print(mfaSrch_small.group())
                #    print("<<Email extraction started for small case >>")
                #    mailIDs = re.findall('\S+@\S+', inboxMail.body)
                #    print(mailIDs)
                #    print(newsCredSender)
                #    break

                elif  newsCredSubApp or newsCredSubKWrdB:
                    print('Match found APP Name keyword in Subject: >>')
                    print("Keyword match found: \t", newsCredSubMFA.group() or newsCredSubKWrdA.group())
                    mailIDs = re.findall('\S+@\S+', inboxMail.body)
                    print(mailIDs)
                    print('Sender Mail:\t', newsCredSender)
                    break

                elif newsCredSubKWrdC or newsCredSubKWrdD:
                    print('Match found APP Name keyword in Subject: Autheticator KW >>')
                    print("Keyword match found: \t", newsCredSubMFA.group() or newsCredSubKWrdA.group())
                    mailIDs = re.findall('\S+@\S+', inboxMail.body)
                    print(mailIDs)
                    print('Sender Mail:\t', newsCredSender)
                    break

                elif newsCredSubKWrdE or newsCredSubKWrdF:
                    print('Match found APP Name keyword in Subject: Denied/ Shell Brand Application >>')
                    print("Keyword match found: \t", newsCredSubMFA.group() or newsCredSubKWrdA.group())
                    mailIDs = re.findall('\S+@\S+', inboxMail.body)
                    print(mailIDs)
                    print('Sender Mail:\t', newsCredSender)
                    break

                elif newsCredSubKWrdG or newsCredSubKWrdH:
                    print('Match found APP Name keyword in Subject: login/ Account  >>')
                    print("Keyword match found: \t", newsCredSubKWrdG.group() or newsCredSubKWrdH.group())
                    mailIDs = re.findall('\S+@\S+', inboxMail.body)
                    print(mailIDs)
                    print('Sender Mail:\t', newsCredSender)
                    break

                elif newsCredSubKWrdI or newsCredSubKWrdJ:
                    print('Match found APP Name keyword in Subject: lost/ $mfa  >>')
                    print("Keyword match found: \t", newsCredSubKWrdG.group() or newsCredSubKWrdH.group())
                    mailIDs = re.findall('\S+@\S+', inboxMail.body)
                    print(mailIDs)
                    print('Sender Mail:\t', newsCredSender)
                    break
                #break
            #break
        break

    print('\tEOF')

if __name__ == '__main__':
    usrInbox()
    #gssFMB()