CREATE DATABASE app;
CREATE USER app_user WITH PASSWORD 'app_password';
ALTER ROLE app_user SET client_encoding TO 'utf8';
ALTER ROLE app_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE app_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE app TO app_user;
ALTER DATABASE app OWNER TO app_user;
\c app
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public to app_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public to app_user;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public to app_user;