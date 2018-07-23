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

### 2. Log latitude and longitude to file
```
sudo python3 log_gps.py {description}
where {description} is an optional argument to label
GPS coordinates written to file
```

### 3. Run on Pi boot (optional)
```
cd ~
sudo vim .bashrc
    (add this line to the bottom:)
    python /home/pi/Desktop/weltraum/log_gps.py 
```

