# Coded by t0int <3 using colorama
import colorama

class logger:
    def __init__(self, log_file):
        colorama.init()
        self.log_file = log_file
        self.log_file_handle = open(log_file, 'w')
    def error(self,str):
        print(colorama.Fore.RED + "[ERROR]: "+str + colorama.Fore.WHITE)
        self.log_file_handle.write("[ERROR] " + str + "\n")
    def warning(self,str):
        print(colorama.Fore.YELLOW + str + colorama.Fore.WHITE)
        self.log_file_handle.write("[WARNING] " + str + "\n")
    def info(self,str):
        print(colorama.Fore.GREEN + str + colorama.Fore.WHITE)
        self.log_file_handle.write("[INFO] " + str + "\n")
    def debug(self,str):
        print(colorama.Fore.BLUE + str + colorama.Fore.WHITE)
        self.log_file_handle.write("[DEBUG] " + str + "\n")
