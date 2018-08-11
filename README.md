# Weltraum
## Log GPS data from USB module in real time
```
Author:  Omar Metwally, MD
         omar@analog.earth
License: Analog Labs
Source:  https://github.com/AnalogLabs/weltraum
```

## Usage

### 1. Get USB GPRS module path
```
dmesg | grep tty
```
(On my machine, this is /dev/ttyACM0)

### 2. Run the weltraum.py script
```
sudo python3 weltraum.py
```
Superuser is required because this script logs latitude, longitude, altitude, velocity, and distance traveled to file.

Accurancy of distance traveled depends on GPS signal quality.

### 3. Run on system boot (optional)
```
cd ~
sudo vim .bashrc
    (add this line to the bottom:)
    python /home/pi/Desktop/weltraum/weltraum.py 
```

