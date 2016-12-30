import usb.core
import usb.util

def main():
    device = usb.core.find(idVendor=0x1a86, idProduct=0x7523)
    device.reset()

    print device

    if device.is_kernel_driver_active(0):
        reattach = True
        device.detach_kernel_driver(0)
 
    print "Start"
    # use the first/default configuration
    device.set_configuration()

    # first endpoint
    endpoint = device[0][(0,0)][0]

    print endpoint
    # read a data packet
    data = None
    while True:
    #for x in range(0, 10):
        #print "ASDF %d" % x
        try:
            #print "Trying hard..."
            data = device.read(endpoint.bEndpointAddress, 0x4)
                                  # endpoint.wMaxPacketSize)
            print data
            #print "At %d getting %r" % (x, data)

            #RxData = ''.join([chr(x) for x in data])
            #print RxData

        except usb.core.USBError as e:
            print "And failing"
            print e
            data = None
            if e.args == ('Operation timed out',):

                continue

    usb.util.dispose_resources(device)

if __name__ == '__main__':
  main()
