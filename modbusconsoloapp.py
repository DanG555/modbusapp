#
# Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#

# ModbusSlaveServer.py
# Runs a modbus slave device in memory for testing purposes.
# This AWS Lambda function allocates registers for the modbus tcp slave and starts
# the server. If an exception occurs, it will wait 5 seconds and try again.
# Since the function is long-lived it will run forever when deployed to a 
# Greengrass core.  The handler will NOT be invoked in our example since 
# the we are executing an infinite loop.

import time
import logging
import sys
#import pymodbus libraries for the server
from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

# instantiate logger which will log any exceptions to Cloudwatch or Greengrass 
# local logs
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

while True:
    try:
        #create registy for modbus server
        store = ModbusSlaveContext(
            di = ModbusSequentialDataBlock(0, [17]*100),
            co = ModbusSequentialDataBlock(0, [17]*100),
            hr = ModbusSequentialDataBlock(0, [17]*100),
            ir = ModbusSequentialDataBlock(0, [17]*100))
        context = ModbusServerContext(slaves=store, single=True)
        
        # change default port of modbus from 502 to 5020 as it requires 
        # root permissions below 1024
        StartTcpServer(context, address=("localhost", 5020))
    except Exception, e:
        logging.info("Error: {0}".format(str(e)))
    time.sleep(5)