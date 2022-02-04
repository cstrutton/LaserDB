import time

from pylogix import PLC

if __name__ == '__main__':
    with PLC() as comm:
        comm.IPAddress = '192.168.1.9'
        read = True
        while read:
            try:
                ret = comm.Read('Verify_Barcode')
                if ret.Value:
                    ret = comm.Read('Barcode_String')
                    print(ret.Value)
                    ret = comm.Write('Barcode_OK', True)
                time.sleep(.5)

            except KeyboardInterrupt:
                print('exiting')
                read = False
