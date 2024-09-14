sudo apt install postgresql-15-postgis
createdb testdb
CREATE EXTENSION postgis;

CREATE USER <name> WITH PASSWORD '<password>';
ALTER ROLE <name> SET client_encoding TO 'utf8';
ALTER ROLE <name> SET default_transaction_isolation TO 'read committed';
ALTER ROLE <name> SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE testdb TO <name>;

GRANT CREATE ON SCHEMA public TO <name>;
