__project__ = 'MFAAuto'
__author__ = 'DeVaa'
__descript__ = "Copyright (c) 2021 Ozzius(deb991)"
__URL__ = 'https://github.com/deb991/'
__NB__ = 'For more information, please see github page & all commit details.'
__CipherSig__ = 'This project & all associate files are encrypted under PBEncryption cryptography. Another details will be available at the end of this pgogram.'

import datetime as dt
import re

import win32com.client

respondMail = "C:\\Users\\Debashis.D.Biswas\\PycharmProjects\\MFAAuto\\mailGun\\mailReq.py"

##Current time
curTime = dt.datetime.now()
lastQtrTIme = dt.datetime.now() - dt.timedelta(minutes=30)
##############################################

outlook = win32com.client.Dispatch("Outlook.application")
mapi = outlook.GetNamespace("MAPI")

for stor in win32com.client.Dispatch("Outlook.Application").Session.Stores:
    print('\nDisplaying FMB names\t')
    #print('\nstor.DisplayName\t')
    print( stor.DisplayName)
    print('\t\nEnd of Display Name')
    break

Inbox = mapi.Folders["debashis.d.biswas@shell.com"].Folders['Inbox']
##~~~~~~~~~~~~~~~User Inbox Details~~~~~~~~~~~~~~~~~##
inboxMails = Inbox.items
inboxMails.sort("[ReceivedTime]", True)
##>>>>>>>>>>>>>>>Assignment<<<<<<<<<<<<<<<<##
inboxMail = inboxMails.GetFirst()
inboxMail_count = inboxMails.count
inboxMail_Sub = inboxMail.Subject
# inboxMail_body = inboxMail.body
bodyData = inboxMail.body

replyMailSub = re.search(r'Re:*', inboxMail_Sub)    #Used
SeleniumJobTrig = re.search(r'Re:Re*', inboxMail_Sub)   #Used

readQus = re.search(r'Re:Questioner*', inboxMail_Sub)   #Used

questionerChk = re.search(r'Re:<<Questioner>>', inboxMail_Sub)  #Used

newsCredSender = re.search(r'creativehub', inboxMail.SenderEmailAddress)  # Used
newsCredSenderATShell = re.search(r'@shell', inboxMail.SenderEmailAddress)  # Used

newsCredSenderDEMO = re.search(r'debashis', inboxMail.SenderEmailAddress)  # Used
newsCredSenderDEMOATShell = re.search(r'@shell.com', inboxMail.SenderEmailAddress)  # Used

mfaSrch = re.search(r"MFA", bodyData)  # Used
mfaSrch_small = re.search(r"mfa", bodyData)  # Used

newsCredSubMFA = re.search(r'MFA', inboxMail_Sub)  # Used
newsCredSubApp = re.search(r'News', inboxMail_Sub)  # Used

newsCredSubKWrdA = re.search(r'mfa', inboxMail_Sub)  # Used
newsCredSubKWrdB = re.search(r'Cred', inboxMail_Sub)  # Used

newsCredSubKWrdC = re.search(r'authentication', inboxMail_Sub)  # Used
newsCredSubKWrdD = re.search(r'authenticator', inboxMail_Sub)  # Used

newsCredSubKWrdE = re.search(r'denied', inboxMail_Sub)  # Used
newsCredSubKWrdF = re.search(r'Shell Brand Applications', inboxMail_Sub)  # Used

newsCredSubKWrdG = re.search(r'login', inboxMail_Sub)  # Used
newsCredSubKWrdH = re.search(r'account', inboxMail_Sub)  # Used

newsCredSubKWrdI = re.search(r'Lost', inboxMail_Sub)  # used
newsCredSubKWrdJ = re.search(r'mfa$', inboxMail_Sub)  # used

newsCredSubKWrdK = re.search(r'MFA Support', inboxMail_Sub)  # Used

##>>>>>>>>>>>>>>>End of Assignment<<<<<<<<<<<<<<##
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

def mailIDReg():
    import win32com.client as win32
    # from datetime import *
    # now = datetime.now()
    from time import strftime


    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = 'debashis.d.biswas@shell.com'
    # mail.Cc = 'INNNIA@SHELL.com; Kishalaya.Nath@shell.com'
    # mail.Cc = 'receipents; receipents'
    # mail.Bcc = ' P.PallaviBharti@shell.com'
    mail.Subject = 'Re:' + strftime("%d/%m/%Y") + inboxMail_Sub

    # F = open(os.path.expanduser(os.getenv('USERPROFILE')) + 'path')
    # line = F.read()

    (mail.body) = 'Hi,\n Kindly share your mail ID associated with your current employeer. \n\nThanks in advance.\nShell Global function'


    mail.send

def qusUsr():
    from datetime import datetime, date
    import win32com.client as win32
    now = datetime.now()

    today = date.today()
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = 'debashis.d.biswas@shell.com'
    # mail.Cc = 'INNNIA@SHELL.com; Kishalaya.Nath@shell.com'
    # mail.Cc = 'receipents; receipents'
    # mail.Bcc = ' P.PallaviBharti@shell.com'
    mail.Subject = '<<Questioner>> || ' + today.strftime("%d/%m/%Y") + '||' + inboxMail_Sub

    (mail.body) = 'Hi,\n\n Kindly provide us below information ' \
                  'associated to MFA authentication.\n' \
                  '\n\t1>Question: Are you using an iPhone or Android to install the Google Authenticator app? ' \
                  '\n\t2>Question: Have you recently deleted and re-installed the Google Authenticator app? ' \
                  '\n\t3>Question: Have you changed phones since downloading the Google Authenticator app? ' \
                  '\n\nThanks in advance.\nShell Global function'
    mail.send


def usrInbox():
#>>>>>>> 079b111 (Added UX/ UI module into the Code block.)

    global inboxMail
    while inboxMail:
        for inboxMail in lastQtrMessages:
            if inboxMail.unread == True:
                print('Initiating Main process -- flag 1.1')

#<<<<<<< HEAD
                if replyMailSub:
                    print('\nSingle Re:*')
                    print('\nMail extraction & validation has been check at this stage!!')
                    print('\n\n')
                    print('\nSimple Questioner mail will be triggered !!')
                    print('\n\tAnswer check/ Validation !!')
                    print('\n\tQuestioner mail will be triggered!!')
                    qusUsr()
                    #break

                elif SeleniumJobTrig:
                    print('\nDouble Re:Re:*')
                    print('\nMail extraction & validation has been check at this stage!!')
                    print('\n\n')
                    print('\nSimple Questioner mail will be triggered !!')
                    print('\n\tAnswer check/ Validation !!')
                    print('\n\tQuestioner mail will be triggered!!')
                    qusUsr()
                    #break

                elif questionerChk:
                    print('\n\tQuestioner Mail read & act as per scenario\n\t')
                    answer = re.compile('\w+:yes+\.[a-z]{2}')
                    answer.findall(bodyData)


                else:
                    print('\nWhen fresh mail arrived' )
                    if newsCredSenderDEMO or newsCredSenderDEMOATShell:
                        print('First checking Mail sender :: ')
                        print('Sender Mail:\t', newsCredSenderDEMO or newsCredSenderDEMOATShell)
                        print("\nAction Script placed\n")
                        mailIDReg()
                        break

                    elif newsCredSubMFA or newsCredSubKWrdA:
                        print('Match found MFA/ mfa keyword in Subject: >>')
                        print("Keyword match found: \t", newsCredSubMFA.group() or newsCredSubKWrdA.group())
                        mailIDs = re.findall('\S+@\S+', inboxMail.body)
                        print(mailIDs)
                        print('Sender Mail:\t', newsCredSender)
                        mailIDReg()
                        break

                    elif newsCredSubApp or newsCredSubKWrdB:
                        print('Match found APP Name keyword in Subject: >>')
                        print("Keyword match found: \t", newsCredSubMFA.group() or newsCredSubKWrdA.group())
                        mailIDs = re.findall('\S+@\S+', inboxMail.body)
                        print(mailIDs)
                        print('Sender Mail:\t', newsCredSender)
                        mailIDReg()
                        break

                    elif newsCredSubKWrdC or newsCredSubKWrdD:
                        print('Match found APP Name keyword in Subject: Autheticator KW >>')
                        print("Keyword match found: \t", newsCredSubMFA.group() or newsCredSubKWrdA.group())
                        mailIDs = re.findall('\S+@\S+', inboxMail.body)
                        print(mailIDs)
                        print('Sender Mail:\t', newsCredSender)
                        mailIDReg()
                        break

                    elif newsCredSubKWrdE or newsCredSubKWrdF:
                        print('Match found APP Name keyword in Subject: Denied/ Shell Brand Application >>')
                        print("Keyword match found: \t", newsCredSubMFA.group() or newsCredSubKWrdA.group())
                        mailIDs = re.findall('\S+@\S+', inboxMail.body)
                        print(mailIDs)
                        print('Sender Mail:\t', newsCredSender)
                        mailIDReg()
                        break

                    elif newsCredSubKWrdG or newsCredSubKWrdH:
                        print('Match found APP Name keyword in Subject: login/ Account  >>')
                        print("Keyword match found: \t", newsCredSubKWrdG.group() or newsCredSubKWrdH.group())
                        mailIDs = re.findall('\S+@\S+', inboxMail.body)
                        print(mailIDs)
                        print('Sender Mail:\t', newsCredSender)
                        mailIDReg()
                        break

                    elif newsCredSubKWrdI or newsCredSubKWrdJ:
                        print('Match found APP Name keyword in Subject: lost/ $mfa  >>')
                        print("Keyword match found: \t", newsCredSubKWrdG.group() or newsCredSubKWrdH.group())
                        mailIDs = re.findall('\S+@\S+', inboxMail.body)
                        print(mailIDs)
                        print('Sender Mail:\t', newsCredSender)
                        mailIDReg()
                        break

                    else:
                        print("\nNo MFA issue has been arrived yet\n")
                #break
            break
        break
    print('\tEOF')

if __name__ == '__main__':
    usrInbox()
