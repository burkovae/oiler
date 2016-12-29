import usb.core
import usb.util

# find our device
dev = usb.core.find(idVendor=0x0424, idProduct=0xec00)

if dev is None:
    raise ValueError('Device not found')

print dev

#dev.set_configuration()
