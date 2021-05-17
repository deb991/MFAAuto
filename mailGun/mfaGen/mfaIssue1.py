__project__ = 'MFAAuto'
__author__ = 'DeVaa'
__descript__ = "Copyright (c) 2021 Ozzius(deb991)"
__URL__ = 'https://github.com/deb991/'
__NB__ = 'For more information, please see github page & all commit details.'
__CipherSig__ = 'This project & all associate files are encrypted under PBEncryption cryptography. Another details will be available at the end of this pgogram.'

from datetime import datetime, date

import win32com.client as win32

now = datetime.now()

today = date.today()
outlook = win32.Dispatch ( 'outlook.application' )
mail = outlook.CreateItem ( 0 )
mail.To = 'debashis.d.biswas@shell.com'

mail.Subject = 'Creative Hub Access Issue | MFA Token expired'

(mail.body) = 'Hello team,\n\n Good day!\nRequesting for your support to issue @karbasetti@blueskydefna.com a new ' \
              'MFA token to be able to access Creative Hub. She was able to register as an external user but her ' \
              'token have expired already.\nLooking forward to have this solved as soon as possible.\n\nThank you so ' \
              'much for your support!\nBest Regards,\nJoshua\nJoshua Mae Villar-Echaore\nCreative Services Project ' \
              'Manager – North America\nShell Business Operations\n 18th Floor Solaris One Building | 130 ' \
              'Dela Rosa Street Makati City | Philippines\nWeb: Shell.com | E-mail: Joshua-Mae.Villar@shell.com'
mail.send

#if __name__ == '__main__':
#    MailGun ()