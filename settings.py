import logging


# logging
console_log_level = logging.INFO
file_log_level = logging.INFO
save_logs_to_file = False

# requests
# if the Plextrac instance is running on https without valid certs, requests will respond with cert error
# change this to false to override verification of certs
verify_ssl = True

# description of script that will be print line by line when the script is run
script_info = ["====================================================================",
               "= Report Template Import/Export Script                            =",
               "=-----------------------------------------------------------------=",
               "=  Used to export a report template and save it as a JSON file.   =",
               "=  You can then keep the file as a backup or import it to a       =",
               "=  different instance of Plextrac.                                =",
               "==================================================================="
            ]
