CREATE USER app WITH PASSWORD 'app';
CREATE DATABASE app WITH OWNER app ENCODING 'UTF8';
GRANT ALL PRIVILEGES ON DATABASE app TO app;
