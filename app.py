#!/bin/python

from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
from random import uniform
import logging
import sys
#Create an instance of ModbusServer

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


try:
    logging.info("Iniciando")
    server = ModbusServer(host="127.0.0.1", port=5020, no_block=True)
    print("Start server...")
    server.start()
    print("Server is online")
    state=[0]
    while True:
        DataBank.set_words(0,[int(uniform(0,100))])
        if state != DataBank.get_words(1):
            state = DataBank.get_words(1)
            print("Value of Registers 1 has changed to =" + str(state))
            sleep(0.5)
            
except Exception as e:
    logging.info("Error: {0}".format(str(e)))
    print("Shutdown server ....")
    server.stop()
    print("Server is offline")
