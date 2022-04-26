import colorama

class Logger:
    def __init__(self, log_file):
        self.log_file = log_file
        self.log_file_handle = open(log_file, 'w')
        colorama.init()
    def error(self,log_str):
        """Log an error message to log file and console

        Args:
            log_str (str): String to log to file and console
        """
        
        print(colorama.Fore.RED + "[ERROR]: "+log_str + colorama.Fore.WHITE)
        self.log_file_handle.write("[ERROR] " + log_str + "\n")
    def warning(self,log_str):
        """Log an warning message to log file and console

        Args:
            log_str (str): String to log to file and console
        """
        
        print(colorama.Fore.YELLOW + log_str + colorama.Fore.WHITE)
        self.log_file_handle.write("[WARNING] " + log_str + "\n")
    def info(self,log_str):
        """Log an information message to log file and console

        Args:
            log_str (str): String to log to file and console
        """
        
        print(colorama.Fore.GREEN + log_str + colorama.Fore.WHITE)
        self.log_file_handle.write("[INFO] " + log_str + "\n")
    def debug(self,log_str):
        """Log an debugging message to log file and console

        Args:
            log_str (str): String to log to file and console
        """
        
        print(colorama.Fore.BLUE + log_str + colorama.Fore.WHITE)
        self.log_file_handle.write("[DEBUG] " + log_str + "\n")
