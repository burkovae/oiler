import usb.core
import usb.util

# find our device
dev = usb.core.find(idVendor=0x0424, idProduct=0xec00)

if dev is None:
    raise ValueError('Device not found')

print dev

#if dev.is_kernel_driver_active(0):
#    dev.detach_kernel_driver(0)

#usb.util.claim_interface(dev, 0)

#if dev.is_kernel_driver_active(1):
#    dev.detach_kernel_driver(1)

#usb.util.claim_interface(dev, 1)

#dev.set_configuration()
