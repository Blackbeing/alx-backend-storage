-- MYSQL triggers

CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users FOR EACH ROW
WHEN NEW.email <> OLD.email
SET NEW.valid_email = 0;
