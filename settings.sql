-- settings.sql

CREATE DATABASE kinlink_db;
CREATE USER kinlinkuser WITH PASSWORD 'kinlink';
GRANT ALL PRIVILEGES ON DATABASE kinlink_db TO kinlinkuser;