DROP DATABASE IF EXISTS Battery_Management;
CREATE DATABASE IF NOT EXISTS Battery_Management;
USE Battery_Management;

CREATE TABLE Family (
    name VARCHAR(50) PRIMARY KEY
);

-- Modified User table with family name as the relationship
CREATE TABLE User (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    family_name VARCHAR(50) NOT NULL,
    name VARCHAR(35) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(20) NOT NULL,
    FOREIGN KEY (family_name) REFERENCES Family(name) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Modified Device table to be owned by families identified by name
CREATE TABLE Device (
    device_id INT PRIMARY KEY AUTO_INCREMENT,
    family_name VARCHAR(50) NOT NULL,
    name VARCHAR(25) NOT NULL,
    brand VARCHAR(25) NOT NULL,
    type ENUM('Remote', 'Camera', 'Toy', 'Flashlight', 'Car key', 'Game Controller', 'Watch/Clock', 'Mouse/CompPeripherals', 'Scale', 'Other') NOT NULL DEFAULT 'Other',
    number_of_cells TINYINT NOT NULL DEFAULT 2,
    battery_size ENUM('AA', 'AAA', 'D2', 'CR2032', 'CR2025', 'CR2016', 'LR44', 'LR41', '9V', 'Other') NOT NULL DEFAULT 'AAA',
    weight_sensitive BOOL DEFAULT FALSE,
    FOREIGN KEY (family_name) REFERENCES Family(name) ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE (family_name, name, brand, type, number_of_cells, battery_size, weight_sensitive)
);

CREATE TABLE Pack (
    pack_id INT PRIMARY KEY AUTO_INCREMENT,
    brand ENUM('Duracell Ultra', 'Duracell', 'Eveready', 'AmazonBasics', 'Panasonic', 'Energizer', 'Nippo', 'Sony', 'PowerCell', 'Godrej', 'Amaron', 'Other') NOT NULL DEFAULT 'Other',
    number_of_cells TINYINT NOT NULL DEFAULT 1,
    battery_size ENUM('AA', 'AAA', 'D2', 'CR2032', 'CR2025', 'CR2016', 'LR44', 'LR41', '9V', 'Other') NOT NULL DEFAULT 'AAA',
    UNIQUE (brand, number_of_cells, battery_size)
);

CREATE TABLE Store (
    name VARCHAR(50) PRIMARY KEY
);

-- Modified Purchased table to track family purchases using family name
CREATE TABLE Purchased (
    purchase_id INT PRIMARY KEY AUTO_INCREMENT,
    pack_id INT NOT NULL,
    store_name VARCHAR(50) NOT NULL,
    family_name VARCHAR(50) NOT NULL,
    user_id INT NOT NULL,  -- To track which family member made the purchase
    price INT NOT NULL,
    purchase_date DATE NOT NULL,
    expiry_date DATE NOT NULL,
    FOREIGN KEY (pack_id) REFERENCES Pack(pack_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (store_name) REFERENCES Store(name) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (family_name) REFERENCES Family(name) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (user_id) REFERENCES User(user_id) ON DELETE CASCADE ON UPDATE CASCADE
);




CREATE TABLE Log (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    device_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    disposed BOOL DEFAULT FALSE,
    FOREIGN KEY (device_id) REFERENCES Device(device_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Battery table for storing individual battery details
CREATE TABLE Battery (
    battery_id INT PRIMARY KEY AUTO_INCREMENT,
    purchase_id INT NOT NULL,
    log_id INT,
    FOREIGN KEY (purchase_id) REFERENCES Purchased(purchase_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (log_id) REFERENCES Log(log_id) ON DELETE SET NULL ON UPDATE CASCADE
);

-- Triggers to manage the logs and batteries
DELIMITER //

CREATE PROCEDURE InsertLogEntry(IN deviceId INT, IN startDate DATE)
BEGIN
    -- Close any existing open log for the specified device
    UPDATE Log
    SET end_date = startDate
    WHERE device_id = deviceId AND end_date IS NULL;

    -- Insert the new log entry
    INSERT INTO Log (device_id, start_date, end_date)
    VALUES (deviceId, startDate, NULL);
END;
//

DELIMITER ;


DELIMITER //

CREATE TRIGGER insert_batteries_after_purchase_insert
AFTER INSERT ON Purchased
FOR EACH ROW
BEGIN
    DECLARE i INT DEFAULT 0;
    DECLARE cells INT;

    -- Retrieve the number of cells for the given pack_id
    SELECT number_of_cells INTO cells 
    FROM Pack 
    WHERE pack_id = NEW.pack_id;

    -- Insert a row into Battery for each cell
    WHILE i < cells DO
        INSERT INTO Battery (purchase_id) VALUES (NEW.purchase_id);
        SET i = i + 1;
    END WHILE;
END;

//

DELIMITER ;


DELIMITER $$

CREATE FUNCTION DISPOSE_BATTERY_FUNC(family_name VARCHAR(100), battery_size VARCHAR(50), no_of_cells INT)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE updated_count INT DEFAULT 0;

    -- Update `disposed` for the specified number of cells
    UPDATE log
    NATURAL JOIN battery
    NATURAL JOIN purchased
    NATURAL JOIN pack
    SET disposed = 1
    WHERE family_name = family_name 
      AND battery_size = battery_size 
      AND disposed = 0
      AND end_date IS NOT NULL;

    -- Count the number of rows affected
    SET updated_count = ROW_COUNT();

    RETURN updated_count;
END$$

DELIMITER ;

UPDATE log
    NATURAL JOIN battery
    NATURAL JOIN purchased
    NATURAL JOIN pack
    SET disposed = 1
    WHERE family_name = 'Williams' 
      AND battery_size = 'AA' 
      AND disposed = 0
      AND end_date IS NOT NULL;