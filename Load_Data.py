import psycopg2


if __name__ == "__main__":

	#connect to database
	con = psycopg2.connect(dbname='Staging', 
						   user='postgres', 
						   host='localhost',
						   password='kamkar')
	cur = con.cursor()

	try:

		cur.execute("""DROP TABLE IF EXISTS tmp""")

		#create temporary table
		cur.execute(""" 

			CREATE TABLE tmp (
			medallion  				TEXT,
			hack_license   			TEXT,
			vendor_id     			TEXT,
			rate_code    			SMALLINT,
			store_and_fwd_flag    	TEXT,
			pickup_time     		TIMESTAMP,
			dropoff_time  			TIMESTAMP,
			passenger_count    		SMALLINT,
			trip_time   			INTEGER,
			trip_distance    		REAL,
			pickup_longitude    	REAL,
			pickup_latitude    		REAL,
			dropoff_longitude   	REAL,
			dropoff_latitude    	REAL
			 );
			""")

		#loop through each csv file
		for i in range(1,13):

			filename = ('C:/Users/michael/Desktop/Programming/python/'
				     + 'NYC_Taxi_Cab_year/trip_data/trip_data_' + str(i) + '.csv')


			#copy csv file to temporary table
			cur.execute(""" 

					COPY tmp
					FROM %s
					WITH (format CSV, HEADER);

					""", [filename],)
			print('loaded' + str(i))

		con.commit()


	except psycopg2.DatabaseError as error:
		print(error)

	finally:
		if con is not None:
			con.close()