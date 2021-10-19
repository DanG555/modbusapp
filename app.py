#!/bin/python

from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
from random import uniform
#Create an instance of ModbusServer




if __name__ == "__main__":
    #!/bin/python
    # server=ModbusServer(host="192.168.0.210",port=502,no_block=True)
    server = ModbusServer(host="127.0.0.1", port=502, no_block=True)

    try:
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
    except:
        print("Shutdown server ....")
        server.stop()
        print("Server is offline")
