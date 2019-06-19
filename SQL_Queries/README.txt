To clean the data, we must look at the medallion, hack_license, and
pickup_time columns. A medallion is unique to a single yellow cab 
vehicle, and a hack_license is unique to single cab driver. 
Multiple hack_licenses can use a medallion (multiple drivers using 
one vehicle), and a hack_license can use multiple medallions 
(a driver can use multiple vehicles). However, a particular 
medallion AND/OR hack_license cannot have two rows containing
the same pickup_time. In other words, a vehicle AND/OR driver cannot 
be fulfilling two fares at the same time.

There are three cases of duplicates in this dataset

1.) Multiple rows with the same medallion, hack_license, & pickup_time
2.) Multiple rows with the same medallion & pickup_time
3.) Multiple rows with the same hack_license & pickup_time

In each case, the duplicates have different dropoff_times (although this
technically makes them not duplicates, I would still like to use the term).
My plan is to put these duplicates into a seperate tables for each case,
remove the duplicates from the main temporary table, then figure out
which of the duplicates to put back into the main table. 

Case 1.) Keep the row with the largest dropoff_time, unless it conflicts
	 with another row with the same (medallion hack_license). If
         the dropoff_time > pickup_time of another column, use the smaller
	 dropoff_time.

Case 2.) There are two different drivers using the same vehicle at the same 
	 time. I need to figure out who was driving the vehicle before and 
	 after the fare of question, and hopefully that will clarify which 
	 driver was driving the particular vehicle.

Case 3.) A single driver is using two different vehicles at the same time.
	 I need to figure out which vehicle the driver was using before 
	 and after the ride of question, and hopefully that will clarify 
	 which vehicle the driver was using. 

