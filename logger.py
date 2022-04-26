import colorama # For color in terminal
import io
import datetime

class Logger:
    """Logging class for logging messages to file and console"""
    def __init__(self, log_file):
        self.log_file = log_file
        self.log_file_handle = io.open(log_file, "w", encoding="utf-8")
        self.log_file_handle.write("Log file created at " + str(datetime.now()) + "\n")
        colorama.init()
    def error(self,log_str):
        """Log an error message to log file and console

        Args:
            log_str (str): String to log to file and console
        """
        print(colorama.Fore.RED + "[" + datetime.now() + "] [ERROR]: "+log_str + colorama.Fore.WHITE)
        self.log_file_handle.write("[" + datetime.now() + "] [ERROR] " + log_str + "\n")
    def warning(self,log_str):
        """Log an warning message to log file and console

        Args:
            log_str (str): String to log to file and console
        """
        print(colorama.Fore.YELLOW + "[" + datetime.now() + "] [WARNING] " + log_str + colorama.Fore.WHITE)
        self.log_file_handle.write("[" + datetime.now() + "] [WARNING] " + log_str + "\n")
    def info(self,log_str):
        """Log an information message to log file and console

        Args:
            log_str (str): String to log to file and console
        """
        print(colorama.Fore.GREEN + "[" + datetime.now() + "] [INFO] " + log_str + colorama.Fore.WHITE)
        self.log_file_handle.write("[" + datetime.now() + "] [INFO] " + log_str + "\n")
    def debug(self,log_str):
        """Log an debugging message to log file and console

        Args:
            log_str (str): String to log to file and console
        """
        print(colorama.Fore.BLUE + "[" + datetime.now() + "] [DEBUG] " + log_str + colorama.Fore.WHITE)
        self.log_file_handle.write("[" + datetime.now() + "] [DEBUG] " + log_str + "\n")
