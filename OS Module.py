# OS module

import os
#print os.listdir("/Users/prateekagnihotri/Desktop/")

#output --- gives a list of all the files and dirs at the path
'''
['KUBERNETES TUTORIAL.docx', "Prateek's Resume.pdf", 'STUFF1', 'SNIAVideo-combined.pdf', 'screenshots', '.DS_Store', '~$e cases for DataStores.docx', '.localized', 'Resume_Prateek Agnihotri.pdf', 'cloud-manager-backup-restore', 'StringExamples.py', 'idle.pyw', 'Working', 'Screenshot 2022-09-26 at 4.00.32 PM.png', 'dashboard installation on kubernetes cluster.txt', 'prateek.docx', 'PythonPrograms', 'Resume_Prateek_Latest.pdf', 'astro.pages', "prateek's resume 4thOct.docx", 'docker-elastic', 'Komp Bkp', 'Information Storage and Management-v.2.pdf', 'DDAY Docs', 'catalog logging.tx.txt', 'Storage Networks Explained_ Basics and Application of Fibre Channel SAN, NAS, iSCSI,InfiniBand and FCoE ( PDFDrive ).pdf', 'Storage Networks Explained 2nd Edition.pdf', 'Screenshot 2022-09-29 at 5.10.42 PM.png', "prateek's resume 4thOct.pdf", "Prateek's Resume for VMware.pdf", 'Sublime Text.app', 'san-module-notes.pdf']
'''

for (root,dirs,filenames) in os.walk("/Users/prateekagnihotri/Desktop/Working"):
     print "dirname is : " , root
     print "subdirs inside that dirname are : ", dirs
     print "filenames inside that dirnames are : ", filenames


print os.path.exists("/Users/prateekagnihotri/Desktop/Working") #true

print os.path.isdir("/Users/prateekagnihotri/Desktop/Working") #true

print os.path.isfile("/Users/prateekagnihotri/Desktop/Working") #false coz its a dir
