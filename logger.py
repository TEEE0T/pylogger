# Made by t0int - using colorama
import io
import datetime
import colorama # For colors in terminal

date = datetime.datetime()

class Logger:
    """Logging class for logging messages to file and console"""
    def __init__(self, log_file):
        self.log_file = log_file
        with io.open(log_file, "w", encoding="utf-8") as io_handle:
            self.log_file_handle = io_handle
        self.log_file_handle.write("Log file created at "+str(date.now())+"\n")
        colorama.init()
    def error(self,log_str):
        """Log an error message to log file and console

        Args:
            log_str (str): String to log to file and console
        """
        print(colorama.Fore.RED+"["+str(date.now())+"] [ERROR]: "+log_str+colorama.Fore.WHITE)
        self.log_file_handle.write("["+str(date.now())+"] [ERROR] "+log_str+"\n")
    def warning(self,log_str):
        """Log an warning message to log file and console

        Args:
            log_str (str): String to log to file and console
        """
        print(colorama.Fore.YELLOW+"["+str(date.now())+"] [WARNING] "+log_str+colorama.Fore.WHITE)
        self.log_file_handle.write("["+str(date.now())+"] [WARNING] "+log_str+"\n")
    def info(self,log_str):
        """Log an information message to log file and console

        Args:
            log_str (str): String to log to file and console
        """
        print(colorama.Fore.GREEN+"["+str(date.now())+"] [INFO] "+log_str+colorama.Fore.WHITE)
        self.log_file_handle.write("["+str(date.now())+"] [INFO] "+log_str+"\n")
    def debug(self,log_str):
        """Log an debugging message to log file and console

        Args:
            log_str (str): String to log to file and console
        """
        print(colorama.Fore.BLUE+"["+str(date.now())+"][DEBUG] "+log_str+colorama.Fore.WHITE)
        self.log_file_handle.write("["+str(date.now())+"][DEBUG] "+log_str+"\n")
