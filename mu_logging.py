import logging
logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%y %h:%M:%S'
                    )

logging.debug("this is a debug message")
logging.warning("this is warning message")
logging.info("this is a info message")
logging.error("this is a error message")
logging.critical("this is a critical message")
