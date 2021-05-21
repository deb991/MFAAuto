__project__ = 'MFAAuto'
__author__ = 'DeVaa'
__descript__ = "Copyright (c) 2021 Ozzius(deb991)"
__URL__ = 'https://github.com/deb991/'
__NB__ = 'For more information, please see github page & all commit details.'
__CipherSig__ = 'This project & all associate files are encrypted under PBEncryption cryptography. Another details will be available at the end of this pgogram.'

import os
import xml.etree.cElementTree as ET

def analystCred():
    root = ET.Element("root")
    doc = ET.SubElement(root, "doc")

    ET.SubElement(doc, "mailID", usrMail='').text = "debashis.d.biswas@shell.com"
    ET.SubElement(doc, "DistributionList", DL='').text = "somwpro@shell.com"

    tree = ET.ElementTree(root)

    os.chdir("..\\res")

    tree.write("main.xml")

def mailExtrct():
    root = ET.Element("root")
    doc = ET.SubElement(root, "doc")

    ET.SubElement(doc, "mailID", usrMail='').text = "debashis.d.biswas@shell.com"
    ET.SubElement(doc, "DistributionList", DL='').text = "somwpro@shell.com"

    tree = ET.ElementTree(root)

    os.chdir("..\\res")

    tree.write("analystCred.xml")