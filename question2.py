How do you join 2 tables using SQLAlchemy?
ans:
  through joins
  example:
    CREATE TABLE cities (
	name VARCHAR NOT NULL, 
	population INTEGER, 
	PRIMARY KEY (name)
)
    CREATE TABLE airlines (
	iata VARCHAR(2) NOT NULL, 
	name VARCHAR, 
	primary_hub VARCHAR, 
	PRIMARY KEY (iata), 
	FOREIGN KEY(primary_hub) REFERENCES cities (name)
)
    CREATE TABLE flights (
	airline VARCHAR(2) NOT NULL, 
	flight_num INTEGER NOT NULL, 
	origin VARCHAR, 
	destination VARCHAR, 
	PRIMARY KEY (airline, flight_num), 
	FOREIGN KEY(airline) REFERENCES airlines (iata), 
	FOREIGN KEY(origin) REFERENCES cities (name), 
	FOREIGN KEY(destination) REFERENCES cities (name)
)

    join_query = session.query(City, Airline, Flight)\
                    .join(Airline, Airline.primary_hub == City.name)\
                    .join(Flight, Flight.origin == City.name)

for row in join_query.all():
    print("(")
    for item in row:
        print("   ", item)
    print(")")
