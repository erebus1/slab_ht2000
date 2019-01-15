README
======

## Startup
1. make
2. pipenv install
3. [optional] to identify interface:
    
    3.1 udevadm monitor --udev
    
    3.2 plug in co2 meter
    
    3.3 get /hidraw/hidraw[x] 
4. Plug-in co2 meter (if not yet)
5. export DATADOG_TOKEN=[DD-access-key]
6. export HID=<hid path from 3rd step>  (e.g. /dev/hidraw1)
7. sudo -E bash -c 'python main.py' (or add in systemctl)


=========================================

Reverse engineered userspace driver for SLAB HT2000 CO2, temperature and
relative humidity (RH) data logger made by Dongguan Xintai Instrument Co.

Full blogpost about reverse engineering this thing: http://globalblindspot.blogspot.be/2016/08/reverse-engineering-slab-ht2000-co2_11.html

Author: Tom Van Braeckel <tomvanbraeckel@gmail.com>

