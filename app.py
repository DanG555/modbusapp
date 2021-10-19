#!/bin/python

from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
from random import uniform
#Create an instance of ModbusServer




try:
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
            
except Exception, e:
    logging.info("Error: {0}".format(str(e)))
    print("Shutdown server ....")
    server.stop()
    print("Server is offline")
