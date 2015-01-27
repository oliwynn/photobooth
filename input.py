import usb.core
import usb.util

# find our device
dev = usb.core.find(idVendor=0x04b3, idProduct=0x3107)

# was it found?
if dev is None:
    print 'Device not found'
else:
    print 'Device connected'

