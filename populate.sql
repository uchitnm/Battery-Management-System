INSERT INTO Family (name) 
VALUES 
    ('Smith'),
    ('Johnson'),
    ('Williams'),
    ('Brown'),
    ('Davis');

INSERT INTO User (family_name, name, email, password) 
VALUES 
    ('Smith', 'Alice Smith', 'alice.smith@example.com', 'password1'),
    ('Smith', 'Bob Smith', 'bob.smith@example.com', 'password2'),
    ('Smith', 'Charlie Smith', 'charlie.smith@example.com', 'password3'),
    ('Smith', 'Dana Smith', 'dana.smith@example.com', 'password4'),

    ('Johnson', 'Evan Johnson', 'evan.johnson@example.com', 'password5'),
    ('Johnson', 'Faith Johnson', 'faith.johnson@example.com', 'password6'),
    ('Johnson', 'Gina Johnson', 'gina.johnson@example.com', 'password7'),
    ('Johnson', 'Harry Johnson', 'harry.johnson@example.com', 'password8'),

    ('Williams', 'Ivy Williams', 'ivy.williams@example.com', 'password9'),
    ('Williams', 'Jack Williams', 'jack.williams@example.com', 'password10'),
    ('Williams', 'Kelly Williams', 'kelly.williams@example.com', 'password11'),
    ('Williams', 'Liam Williams', 'liam.williams@example.com', 'password12'),

    ('Brown', 'Megan Brown', 'megan.brown@example.com', 'password13'),
    ('Brown', 'Nathan Brown', 'nathan.brown@example.com', 'password14'),
    ('Brown', 'Olivia Brown', 'olivia.brown@example.com', 'password15'),
    ('Brown', 'Paul Brown', 'paul.brown@example.com', 'password16'),

    ('Davis', 'Quinn Davis', 'quinn.davis@example.com', 'password17'),
    ('Davis', 'Rachel Davis', 'rachel.davis@example.com', 'password18'),
    ('Davis', 'Sam Davis', 'sam.davis@example.com', 'password19'),
    ('Davis', 'Tina Davis', 'tina.davis@example.com', 'password20');

-- Devices for the Smith Family
INSERT INTO Device (family_name, name, brand, type, number_of_cells, battery_size, weight_sensitive) 
VALUES 
    ('Smith', 'TV Remote', 'Samsung', 'Remote', 2, 'AAA', FALSE),
    ('Smith', 'Wall Clock', 'Seiko', 'Watch/Clock', 1, 'AA', TRUE),
    ('Smith', 'Game Controller', 'Sony', 'Game Controller', 4, 'AA', FALSE),
    ('Smith', 'Flashlight', 'Maglite', 'Flashlight', 3, 'AAA', TRUE),
    ('Smith', 'Toy Car', 'Hot Wheels', 'Toy', 2, 'AA', FALSE),
    ('Smith', 'Camera Flash', 'Canon', 'Camera', 4, 'AA', FALSE),
    ('Smith', 'Kitchen Scale', 'Etekcity', 'Scale', 2, 'AAA', TRUE),
    ('Smith', 'Car Key', 'Toyota', 'Car key', 1, 'CR2032', FALSE),
    ('Smith', 'Digital Thermometer', 'Braun', 'Other', 2, 'AAA', FALSE),
    ('Smith', 'Wireless Mouse', 'Logitech', 'Mouse/CompPeripherals', 1, 'AA', FALSE);

-- Devices for the Johnson Family
INSERT INTO Device (family_name, name, brand, type, number_of_cells, battery_size, weight_sensitive) 
VALUES 
    ('Johnson', 'Alarm Clock', 'Sony', 'Watch/Clock', 1, 'AA', TRUE),
    ('Johnson', 'Remote Control', 'LG', 'Remote', 2, 'AAA', FALSE),
    ('Johnson', 'Flashlight', 'Duracell', 'Flashlight', 3, 'AAA', TRUE),
    ('Johnson', 'Baby Monitor', 'Philips', 'Other', 4, 'AA', TRUE),
    ('Johnson', 'Wireless Keyboard', 'Apple', 'Mouse/CompPeripherals', 2, 'AAA', FALSE),
    ('Johnson', 'Toy Robot', 'Fisher-Price', 'Toy', 3, 'AAA', FALSE),
    ('Johnson', 'Bathroom Scale', 'Withings', 'Scale', 3, 'AAA', TRUE),
    ('Johnson', 'Digital Camera', 'Nikon', 'Camera', 4, 'AA', FALSE),
    ('Johnson', 'Car Key', 'Ford', 'Car key', 1, 'CR2025', FALSE),
    ('Johnson', 'Smoke Detector', 'Kidde', 'Other', 1, '9V', TRUE);

-- Devices for the Williams Family
INSERT INTO Device (family_name, name, brand, type, number_of_cells, battery_size, weight_sensitive) 
VALUES 
    ('Williams', 'Wall Clock', 'Casio', 'Watch/Clock', 1, 'AA', TRUE),
    ('Williams', 'TV Remote', 'Panasonic', 'Remote', 2, 'AAA', FALSE),
    ('Williams', 'Toy Car', 'Mattel', 'Toy', 2, 'AA', FALSE),
    ('Williams', 'Flashlight', 'Anker', 'Flashlight', 3, 'AAA', TRUE),
    ('Williams', 'Gaming Mouse', 'Razer', 'Mouse/CompPeripherals', 1, 'AA', FALSE),
    ('Williams', 'Wireless Keyboard', 'Logitech', 'Mouse/CompPeripherals', 2, 'AAA', FALSE),
    ('Williams', 'Fitness Tracker', 'Fitbit', 'Other', 1, 'CR2032', TRUE),
    ('Williams', 'Kitchen Scale', 'Ozeri', 'Scale', 3, 'AAA', TRUE),
    ('Williams', 'Digital Thermometer', 'Omron', 'Other', 2, 'AAA', FALSE),
    ('Williams', 'Portable Speaker', 'JBL', 'Other', 4, 'AA', FALSE);

-- Devices for the Brown Family
INSERT INTO Device (family_name, name, brand, type, number_of_cells, battery_size, weight_sensitive) 
VALUES 
    ('Brown', 'Clock Radio', 'Philips', 'Watch/Clock', 1, 'AA', TRUE),
    ('Brown', 'Remote Control', 'Toshiba', 'Remote', 2, 'AAA', FALSE),
    ('Brown', 'Toy Helicopter', 'Air Hogs', 'Toy', 4, 'AA', FALSE),
    ('Brown', 'Flashlight', 'Streamlight', 'Flashlight', 3, 'AAA', TRUE),
    ('Brown', 'Wireless Headphones', 'Sony', 'Other', 2, 'AAA', FALSE),
    ('Brown', 'Car Key', 'Honda', 'Car key', 1, 'CR2025', FALSE),
    ('Brown', 'Bathroom Scale', 'RENPHO', 'Scale', 3, 'AAA', TRUE),
    ('Brown', 'Digital Camera', 'Canon', 'Camera', 4, 'AA', FALSE),
    ('Brown', 'Wireless Mouse', 'Microsoft', 'Mouse/CompPeripherals', 1, 'AA', FALSE),
    ('Brown', 'Remote Control Car', 'Revell', 'Toy', 2, 'AA', FALSE);

-- Devices for the Davis Family
INSERT INTO Device (family_name, name, brand, type, number_of_cells, battery_size, weight_sensitive) 
VALUES 
    ('Davis', 'Desk Clock', 'Timex', 'Watch/Clock', 1, 'AA', TRUE),
    ('Davis', 'TV Remote', 'Hisense', 'Remote', 2, 'AAA', FALSE),
    ('Davis', 'Fitness Scale', 'Weight Gurus', 'Scale', 3, 'AAA', TRUE),
    ('Davis', 'Flashlight', 'Olight', 'Flashlight', 3, 'AAA', TRUE),
    ('Davis', 'Toy Train', 'LEGO', 'Toy', 2, 'AA', FALSE),
    ('Davis', 'Car Key', 'Hyundai', 'Car key', 1, 'CR2032', FALSE),
    ('Davis', 'Digital Thermometer', 'Braun', 'Other', 2, 'AAA', FALSE),
    ('Davis', 'Wireless Keyboard', 'Dell', 'Mouse/CompPeripherals', 2, 'AAA', FALSE),
    ('Davis', 'Portable Fan', 'Honeywell', 'Other', 4, 'AA', TRUE),
    ('Davis', 'Security Camera', 'Blink', 'Camera', 2, 'AA', FALSE);

INSERT INTO Store (name) 
VALUES 
    ('Walmart'),
    ('Target'),
    ('Best Buy'),
    ('Amazon'),
    ('Costco'),
    ('Home Depot');

INSERT INTO Pack (brand, number_of_cells, battery_size) 
VALUES 
    ('Duracell Ultra', 4, 'AA'),
    ('Duracell', 2, 'AAA'),
    ('Eveready', 1, '9V'),
    ('AmazonBasics', 8, 'AAA'),
    ('Panasonic', 4, 'CR2032'),
    ('Energizer', 2, 'AA'),
    ('Sony', 6, 'LR44'),
    ('PowerCell', 10, 'AAA'),
    ('Godrej', 4, 'D2'),
    ('Nippo', 2, 'AA');

-- Example purchases with specific battery sizes for each family

INSERT INTO Purchased (pack_id, store_name, family_name, user_id, price, purchase_date, expiry_date)
VALUES 
    (1, 'Amazon', 'Smith', 1, 299, '2020-02-20', '2025-02-20'),   -- 4 AA cells (Duracell Ultra)
    (1, 'Amazon', 'Smith', 3, 299, '2020-02-20', '2025-02-20'),   -- 4 AA cells (Duracell Ultra)
    (1, 'Amazon', 'Smith', 4, 299, '2020-02-20', '2025-02-20'),   -- 4 AA cells (Duracell Ultra)
    (4, 'Costco', 'Smith', 1, 150, '2019-08-14', '2024-08-14'),   -- 8 AAA cells (AmazonBasics)
    (2, 'Target', 'Smith', 2, 99, '2019-01-15', '2024-01-15'),    -- 2 AAA cells (Duracell)
    (5, 'Best Buy', 'Smith', 1, 150, '2020-01-15', '2025-01-15');  -- 4 CR2032 cells (Panasonic)

INSERT INTO Purchased (pack_id, store_name, family_name, user_id, price, purchase_date, expiry_date)
VALUES 
    (1, 'Walmart', 'Johnson', 6, 299, '2020-03-15', '2025-03-15'),  -- 4 AA cells (Duracell Ultra)
    (1, 'Walmart', 'Johnson', 6, 299, '2020-03-15', '2025-03-15'),  -- 4 AA cells (Duracell Ultra)
    (1, 'Walmart', 'Johnson', 7, 299, '2020-03-15', '2025-03-15'),  -- 4 AA cells (Duracell Ultra)
    (4, 'Target', 'Johnson', 6, 150, '2019-08-14', '2024-08-14'),   -- 8 AAA cells (AmazonBasics)
    (4, 'Target', 'Johnson', 8, 150, '2019-08-14', '2024-08-14'),   -- 8 AAA cells (AmazonBasics)
    (5, 'Best Buy', 'Johnson', 5, 99, '2020-01-15', '2025-01-15'),   -- 1 CR2025 cell (Panasonic)
    (3, 'Amazon', 'Johnson', 7, 99, '2020-05-10', '2025-05-10');     -- 1 9V cell (Eveready)

INSERT INTO Purchased (pack_id, store_name, family_name, user_id, price, purchase_date, expiry_date)
VALUES 
    (1, 'Walmart', 'Williams', 9, 299, '2020-03-15', '2025-03-15'),  -- 4 AA cells (Duracell Ultra)
    (1, 'Walmart', 'Williams', 10, 299, '2020-03-15', '2025-03-15'),  -- 4 AA cells (Duracell Ultra)
    (4, 'Target', 'Williams', 9, 150, '2019-08-14', '2024-08-14'),   -- 8 AAA cells (AmazonBasics)
    (5, 'Best Buy', 'Williams', 11, 99, '2020-01-15', '2025-01-15');   -- 1 CR2032 cell (Panasonic)

INSERT INTO Purchased (pack_id, store_name, family_name, user_id, price, purchase_date, expiry_date)
VALUES 
    (1, 'Walmart', 'Brown', 14, 299, '2020-03-10', '2025-03-10'),  -- 4 AA cells (Duracell Ultra)
    (1, 'Walmart', 'Brown', 15, 299, '2020-03-10', '2025-03-10'),  -- 4 AA cells (Duracell Ultra)
    (1, 'Walmart', 'Brown', 14, 299, '2020-03-10', '2025-03-10'),  -- 4 AA cells (Duracell Ultra)
    (4, 'Target', 'Brown', 15, 150, '2019-08-14', '2024-08-14'),   -- 8 AAA cells (AmazonBasics)
    (5, 'Best Buy', 'Brown', 14, 99, '2020-01-15', '2025-01-15');   -- 1 CR2025 cell (Panasonic)

INSERT INTO Purchased (pack_id, store_name, family_name, user_id, price, purchase_date, expiry_date)
VALUES 
    (1, 'Home Depot', 'Davis', 18, 299, '2020-03-05', '2025-03-05'),  -- 4 AA cells (Duracell Ultra)
    (1, 'Home Depot', 'Davis', 18, 299, '2020-03-05', '2025-03-05'),  -- 4 AA cells (Duracell Ultra)
    (1, 'Home Depot', 'Davis', 18, 299, '2020-03-05', '2025-03-05'),  -- 4 AA cells (Duracell Ultra)
    (4, 'Best Buy', 'Davis', 19, 150, '2019-12-15', '2024-12-15'),     -- 8 AAA cells (AmazonBasics)
    (5, 'Walmart', 'Davis', 20, 99, '2020-01-10', '2025-01-10');       -- 1 CR2032 cell (Panasonic)



------------------------------------------------------------
------NEW INSERTS FOR BATTERY AND LOG TABLES----------------

INSERT INTO Log (device_id,start_date,end_date,disposed)
VALUES
    (6,'2020-02-20','2020-03-20',1),
    (3,'2020-02-20','2020-04-20',1),
    (1,'2019-01-15','2020-01-15',1),
    (8,'2020-01-15','2024-01-17',1);

UPDATE battery SET log_id = 1 WHERE purchase_id = 1;
UPDATE battery SET log_id = 2 WHERE purchase_id = 2;
UPDATE battery SET log_id = 3 WHERE purchase_id = 5;
UPDATE battery SET log_id = 4 WHERE battery_id = 23;

INSERT INTO Log (device_id,start_date,end_date,disposed)
VALUES
    (46,'2020-01-10',NULL,0),
    (42,'2020-03-05','2021-01-05',1),
    (48,'2020-03-05','2020-08-05',1);

UPDATE battery SET log_id = 5 WHERE battery_id = 124;
UPDATE battery SET log_id = 6 WHERE battery_id = 116;
UPDATE battery SET log_id = 6 WHERE battery_id = 117;
UPDATE battery SET log_id = 7 WHERE battery_id = 118;
UPDATE battery SET log_id = 7 WHERE battery_id = 119;

INSERT INTO Log (device_id,start_date,end_date,disposed)
VALUES
    (22,'2019-08-14','2020-07-14',1),
    (26,'2019-08-20','2020-01-14',0),
    (25,'2020-03-15','2020-08-15',1);

UPDATE battery SET log_id = 8 WHERE battery_id = 68;
UPDATE battery SET log_id = 8 WHERE battery_id = 69;
UPDATE battery SET log_id = 9 WHERE battery_id = 70;
UPDATE battery SET log_id = 9 WHERE battery_id = 71;
UPDATE battery SET log_id = 10 WHERE battery_id = 64;