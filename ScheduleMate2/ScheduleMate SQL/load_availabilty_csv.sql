LOAD DATA LOCAL INFILE 'Availability.csv'
INTO TABLE Availability
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;