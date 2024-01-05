Author: Tristen Smith
---
Each line of the csv file is a record of a single ride at a specific Marta station (Atlanta's subway system). Riders enter and exit the subway system by tapping a Breeze Card against a gate at a specific station.
---
This problem opens the marta csv file and sorts the data based on ...
1. Finds the station with the closest # of taps to the average
2. Finds the station with the least # of taps
3. Finds the average # of taps per station

• CSV Format: (Transit day, time, device ID, station ID, use type, serial #)
1. the transit day, in MM/DD/YYYY format.
2. the transit time, in HH:MM:SS format.
3. the device ID, an identifer of the gate at which the rider entered.
4. the station ID, a numeric identifier the station.
5. the use type, whether the rider was entering, exiting, etc.
6. a serial number, the unique identifier of the rider's Breeze Card.
