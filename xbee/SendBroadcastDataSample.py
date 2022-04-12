# Copyright 2017, Digi International Inc.
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
import numpy as np
from digi.xbee.devices import XBeeDevice
import time
# TODO: Replace with the serial port where your local module is connected to.
PORT = "COM7"
# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 9600

DATA_TO_SEND = "Hello XBee!"

txCount = 0




def main():
    print(" +------------------------------------------------+")
    print(" | XBee Python Library Send Broadcast Data Sample |")
    print(" +------------------------------------------------+\n")

    device = XBeeDevice(PORT, BAUD_RATE)

    try:
        device.open()
        dataPointCuttOff = 10;
        frameSize = 4;

        print("Sending broadcast data: %s..." % DATA_TO_SEND)
        txCount = 0
        while(True):


            sampl = np.random.uniform(low=0.5, high=13.3, size=(frameSize,))
            sampl = [str(s)[0:dataPointCuttOff] for s in sampl]
            sample  = ' '.join(sampl)
            sample = " Frame:" + str(txCount) +" => " +sample

            start = time.time()
            device.send_data_broadcast(sample)
            end = time.time()
            
            txCount = txCount + 1;

            
            print(txCount, "in" , end - start)

        print("Success")

    finally:
        if device is not None and device.is_open():
            device.close()


if __name__ == '__main__':
    main()
