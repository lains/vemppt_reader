#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    This file is part of vemppt_reader.

    vemppt_reader is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    vemppt_reader is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with vemppt_reader.  If not, see <https://www.gnu.org/licenses/>.
"""

import vemppt_parser        #Text parse script
import vemppt_register      #Data register script
import vemppt_message       #Message output

import sys                      #System primitives
import logging                  #Log errors
import serial                   #Read VEDirect data via serial USB
import ctypes                   #To use MessageBoxW
import time                     #Reading periods
from datetime import datetime   #Register local dates

def main(serial_port_name):
    #Value reset
    line = 0                            #Initial line in vemppt_register
    initial_date = datetime.now()       #Date register for xls file

    #Main thread
    ser = serial.Serial(serial_port_name, 19200, timeout=10)      #Change here COM port
    try:
        vemppt_message.print_message("MPPT Found","Correct port communication\nData registration will begin",64)

        line = vemppt_register.xls_open(line)

        while True:
            ve_read = ser.readline()
            line = vemppt_parser.parser(ve_read,line)

    except Exception as e:
        logging.exception("An error ocurred")
        vemppt_message.print_message("An error ocurred","Something went wrong!",16)

    finally:
        ser.close()
        vemppt_register.xls_close(initial_date)

if __name__ == '__main__':
    serial_port = 'COM5'
    if len(sys.argv) > 1:
        serial_port = sys.argv[1]
    main(serial_port)
