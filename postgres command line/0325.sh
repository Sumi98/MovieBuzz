# command line code for postgres

# cd CS411_Project/IMDBSmall

# run postgres on command line
psql postgres

CREATE DATABASE imdbsmall;
CREATE USER group50 WITH PASSWORD '411group50';
ALTER ROLE group50 SET client_encoding TO 'utf8'; 
ALTER ROLE group50 SET default_transaction_isolation TO 'read committed'; 
ALTER ROLE group50 SET timezone TO 'GMT-5';
