-- DATABASE TEST SCHEMA FOR THE PROJECT

CREATE DATABASE IF NOT EXISTS hbnb_test_db;

CREATE USER IF NOT EXISTS hbnb_test@localhost IDENTIFIED WITH hbnb_test_pwd;

GRANT ALL PRIVILEGES ON hbnb_test_db to hbnb_test@localhost WITH GRANT OPTION;

GRANT SELECT FOR hbnb_test ON performance_schema.*;