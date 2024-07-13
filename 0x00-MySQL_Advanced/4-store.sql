-- MySQL triggers
-- AFTER - event, INSERT - when row is inserted, ON - table, FOR EACH ROW - exec trigger for each inserted row
-- NEW - data inserted the triggered this

CREATE TRIGGER dec_item_quantity
AFTER INSERT ON orders FOR EACH ROW
UPDATE items 
SET quantity = quantity - NEW. number
WHERE name = NEW.item_name;


