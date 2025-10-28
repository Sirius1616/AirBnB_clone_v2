-- DATABASE SCHEMA FOR THE PROJECT 

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'Siriusa1.615';

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'root'@'localhost' WITH GRANT OPTION;

GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO hbnb_dev@localhost;


