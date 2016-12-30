# oiler
Project for measuring oil level on pi zero using ultra sound sensors

# steps

- use `lsusb` to identify the vendor and product ids
- put the parameters into the script (or later a configuration file)
- apperently (according to http://www.allnet.de/fileadmin/transfer/products/111901.pdf)
  - the first (from *right* to *left*) byte describes the sum of
  - the flollowing two bytes LOW and HIGH hexadecimal representation of the distance measurement
  - the fourth byte is always `0xFF`


