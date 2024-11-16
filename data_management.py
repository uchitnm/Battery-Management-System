import tkinter.messagebox as msg
import datetime

class USER_TABLE:
    def __init__(self, connection_vector):
        self.connection_vector = connection_vector
        self.cursor = connection_vector.cursor()

    def INSERT_INTO_USER_NEWUSER(self, family_name, username, password, email):
        if not family_name or not username or not password or not email:
            print("All fields are required.")

        try:
            self.cursor.execute(
                "INSERT INTO User (family_name, name, email, password) VALUES (%s, %s, %s, %s)",
                (family_name, username, email, password)
            )
            self.connection_vector.commit()
            print("User added successfully.")

            self.cursor.execute(
                f"Select user_id from user where name = '{username}' and family_name = '{family_name}'")
            return self.cursor.fetchall()[0][0]

        except Exception as e:
            print(f"An error occurred while adding user: {e}")
            self.connection_vector.rollback()

    def SELECT_FROM_USER(self, username):
        try:
            self.cursor.execute(
                "SELECT * FROM User WHERE name = %s", (username,))
            result = self.cursor.fetchall()
            if result:
                return result[0]
            print("User not found.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def close(self):
        self.cursor.close()
        self.connection_vector.close()


class FAMILY_TABLE:
    def __init__(self, connection_vector):
        self.connection_vector = connection_vector
        self.cursor = connection_vector.cursor()

    def INSERT_INTO_FAMILY_NEWFAMILY(self, family_name):
        self.cursor.execute(
            "INSERT INTO Family (name) VALUES (%s)", (family_name,))
        self.connection_vector.commit()

    def SELECT_FROM_FAMILY(self, family_name):
        self.cursor.execute(
            "SELECT * FROM Family WHERE name = %s", (family_name,))
        result = self.cursor.fetchall()

        if result:
            print(result)
            return result[0]
        return None

    def close(self):
        self.cursor.close()
        self.connection_vector.close()


class DEVICE_TABLE:
    def __init__(self, connection_vector):
        self.connection_vector = connection_vector
        self.cursor = connection_vector.cursor()

    def INSERT_INTO_DEVICE_NEWDEVICE(self, family_name, device_name, brand, type, number_of_cells, battery_size, weight_sensitive):
        try:
            self.cursor.execute(
                "INSERT INTO Device (family_name, name, brand, type, number_of_cells, battery_size, weight_sensitive) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (family_name, device_name, brand, type,
                 number_of_cells, battery_size, int(weight_sensitive))
            )
            self.connection_vector.commit()
            print("Device added successfully.")
        except Exception as e:
            print(f"An error occurred while adding device: {e}")
            return None

    def close(self):
        self.cursor.close()
        self.connection_vector.close()


class PURCHASE_TABLE:
    def __init__(self, connection_vector):
        self.connection_vector = connection_vector
        self.cursor = connection_vector.cursor()

    def INSERT_INTO_PURCHASE_NEWPURCHASE(self, brand, number_of_cells, battery_size, price, store, purchase_date, exp_date, family_name, user_id):
        try:
            self.cursor.execute(
                "INSERT INTO Pack (brand, number_of_cells, battery_size) VALUES (%s, %s, %s)",
                (brand, number_of_cells, battery_size)
            )
            self.connection_vector.commit()
            print("Pack added successfully.")
        except Exception as e:
            print('Pack already exists')

        try:
            self.cursor.execute(
                "INSERT INTO Store (name) VALUES (%s)", (store,)
            )
            self.connection_vector.commit()
            print("Store added successfully.")
        except Exception as e:
            print('Store already exists')

        try:
            self.cursor.execute(
                "SELECT pack_id FROM Pack WHERE brand = %s AND number_of_cells = %s AND battery_size = %s",
                (brand, number_of_cells, battery_size)
            )
            pack_id = self.cursor.fetchall()[0][0]
        except Exception as e:
            print(f"An error occurred while fetching pack ID: {e}")
            return  # Early exit in case of error

        try:
            self.cursor.execute(
                "SELECT name FROM Store WHERE name = %s",
                (store,)
            )
            store_name = self.cursor.fetchall()[0][0]
        except Exception as e:
            print(f"An error occurred while fetching store : {e}")
            return  # Early exit in case of error

        purchase_date_str = purchase_date.strftime(
            '%Y-%m-%d')  # Format: YYYY-MM-DD
        expiry_date_str = exp_date.strftime('%Y-%m-%d')

        try:
            self.cursor.execute(
                "INSERT INTO Purchased (pack_id, store_name, family_name, user_id, price, purchase_date, expiry_date) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (pack_id, store_name, family_name, user_id,
                 price, purchase_date_str, expiry_date_str)
            )
            self.connection_vector.commit()
            print("Purchase added successfully.")
        except Exception as e:
            print(f"An error occurred while adding purchase: {e}")

    def close(self):
        self.cursor.close()
        self.connection_vector.close()


class FUNCTIONALITY:
    def __init__(self, connection_vector):
        self.connection_vector = connection_vector
        self.cursor = connection_vector.cursor()

    def SHOW_ALL_DEVICES(self, family_name):
        # Ensures family_name is passed as a single-item tuple (even if it's a single string)
        self.cursor.execute(
            f'SELECT device_id,name FROM Device WHERE family_name ="{family_name}";'
        )
        result = self.cursor.fetchall()
        if result:
            print(result)
            return result
        return None

    def SELECT_ALL_DEVICES(self, family_name):
        self.cursor.execute(
            f'SELECT device_id,name,brand,type,number_of_cells,battery_size,weight_sensitive FROM Device WHERE family_name ="{family_name}";'
        )
        result = self.cursor.fetchall()
        if result:
            return result
        return None

    def SELECT_ALL_BATTERIES(self, family_name):
        self.cursor.execute(
            f"select brand,battery_size,count(*) AS Quantity from battery natural join purchased natural join pack where log_id is null and family_name='{family_name}' group by brand,battery_size;")

        result = self.cursor.fetchall()
        if result:
            return result
        return None

    def SELECT_TODISPOSE_BATTERIES(self, family_name):
        self.cursor.execute(
            f"""
        select battery_size,count(*) from log natural join device natural join battery where family_name='{family_name}' and end_date IS NOT NULL and disposed=0 group by battery_size;
            """
        )
        result = self.cursor.fetchall()
        if result:
            return result
        return None

    def SUGGEST_BATTERY(self, family_name, device_id):
        self.cursor.execute(
            f"SELECT number_of_cells, battery_size from Device WHERE device_id = {device_id};")

        no_of_cells, BATTERY_SIZE = self.cursor.fetchone()
        print("Fetched Data: ", no_of_cells, BATTERY_SIZE)

        self.cursor.execute(
            f"""SELECT COUNT(*) FROM Battery 
                NATURAL JOIN Purchased
                natural join pack
                WHERE family_name = '{family_name}' AND log_id IS NULL AND battery_size = '{BATTERY_SIZE}';""")

        result = self.cursor.fetchone()[0]

        if int(result) >= int(no_of_cells):
            result = True
        else:
            result = False
        return result, BATTERY_SIZE, no_of_cells

    def INSERT_BATTERY(self, family_name, BATTERY_SIZE, no_of_cells, device_id):
        today = datetime.date.today().strftime('%Y-%m-%d')
        self.cursor.callproc('InsertLogEntry', [device_id, today])
        print("Log Inserted")
        print()
        self.cursor.execute(f"""
            SELECT battery_id FROM Battery
            NATURAL JOIN Purchased
            NATURAL JOIN pack
            WHERE family_name = '{family_name}' AND log_id IS NULL AND battery_size='{BATTERY_SIZE}'
            ORDER BY purchase_date
            LIMIT {no_of_cells};""")
        print("Fetched Batteries")
        result = self.cursor.fetchall()
        for i in result:
            self.cursor.execute(
                f"""UPDATE Battery SET log_id = (SELECT log_id FROM Log WHERE device_id = {device_id} AND start_date = '{today}' AND end_date IS NULL AND disposed = 0) WHERE battery_id = {i[0]};""")
            print("Battery Updated")
        self.connection_vector.commit()
        return result

    def SUGGEST_PURCHASE(self, BATTERY_SIZE, device_id):
        self.cursor.execute(
            f"SELECT type from Device WHERE device_id = {device_id};")
        device_type = self.cursor.fetchall()[0][0]
        print("Fetched Data: ", device_type)
        self.cursor.execute(f"""
WITH avg_lifetime AS (
    SELECT 
        d.battery_size,
        pk.brand,
        AVG(
            DATEDIFF(l.end_date, l.start_date)
        ) AS avg_days_lasting
    FROM 
        log l
    JOIN 
        device d ON l.device_id = d.device_id
    JOIN 
        battery b ON l.log_id = b.log_id
    JOIN 
        purchased p ON b.purchase_id = p.purchase_id
    JOIN 
        pack pk ON p.pack_id = pk.pack_id
    WHERE 
        d.type = '{device_type}' AND d.battery_size = '{BATTERY_SIZE}' AND DATEDIFF(l.end_date,l.start_date)>100
    GROUP BY 
        d.battery_size, pk.brand
),
latest_prices AS (
    SELECT
        p.pack_id,
        p.store_name,
        pk.battery_size,
        pk.brand,
        p.price / pk.number_of_cells AS price_per_cell,
        p.price AS total_price
    FROM
        purchased p
    JOIN
        pack pk ON p.pack_id = pk.pack_id
    JOIN (
        SELECT
            pack_id,
            store_name,
            MAX(purchase_date) AS latest_purchase_date
        FROM
            purchased
        GROUP BY
            pack_id, store_name
    ) AS latest_purchase ON p.pack_id = latest_purchase.pack_id
       AND p.store_name = latest_purchase.store_name
       AND p.purchase_date = latest_purchase.latest_purchase_date
),
lowest_price_per_cell AS (
    SELECT DISTINCT
        battery_size,
        store_name,
        brand,
        pack_id,
        price_per_cell,
        total_price
    FROM
        latest_prices
    WHERE
        (battery_size, price_per_cell) IN (
            SELECT
                battery_size, MIN(price_per_cell) AS min_price_per_cell
            FROM
                latest_prices
            GROUP BY
                battery_size, brand
        )
),
price_lifetime_ratio AS (
    SELECT
        lppc.battery_size,
        lppc.brand,
        lppc.store_name,
        lppc.pack_id,
        lppc.price_per_cell,
        lppc.total_price,
        al.avg_days_lasting,
        lppc.price_per_cell / al.avg_days_lasting AS price_per_day_ratio
    FROM
        lowest_price_per_cell lppc
    JOIN
        avg_lifetime al ON lppc.battery_size = al.battery_size AND lppc.brand = al.brand
)
SELECT 
    battery_size,
    brand,
    store_name,
    pack_id,
    price_per_cell,
    total_price,
    avg_days_lasting,
    price_per_day_ratio
FROM 
    price_lifetime_ratio
ORDER BY 
    price_per_day_ratio;
                            """)
        result = self.cursor.fetchall()
        print(result)
        return result

    def SUGGEST_PURCHASE_PRICE_ONLY(self, BATTERY_SIZE):
        self.cursor.execute(f"""
SELECT
    p.pack_id,
    p.store_name,
    pk.brand,
    pk.battery_size,
    MAX(p.purchase_date) AS latest_purchase_date,
    p.price,
    p.price / pk.number_of_cells AS price_per_cell
FROM
    purchased p
JOIN
    pack pk ON p.pack_id = pk.pack_id
JOIN (
    SELECT
        pack_id,
        store_name,
        MAX(purchase_date) AS max_purchase_date
    FROM
        purchased
    GROUP BY
        pack_id, store_name
) AS latest_purchase ON p.pack_id = latest_purchase.pack_id
   AND p.store_name = latest_purchase.store_name
   AND p.purchase_date = latest_purchase.max_purchase_date
WHERE
   pk.battery_size = '{BATTERY_SIZE}'
GROUP BY
    p.pack_id, p.store_name, pk.brand, pk.battery_size, p.price
ORDER BY price_per_cell;
""")
        data = self.cursor.fetchall()
        return data

    def INSERT_PURCHASE(self, pack_id, store_name, glb_family_name, glb_user_id, price, today=None):
        if today is None:
            today = datetime.date.today().strftime(
                '%Y-%m-%d')  # Get today's date if not provided

        split = today.split('-')
        future_date_str = str(
            (int(split[0]))+10) + '-' + str(split[1]) + '-' + str(split[2])

        # Execute your SQL query
        self.cursor.execute(f"INSERT INTO purchased (pack_id, store_name, family_name, user_id, price, purchase_date, expiry_date) "
                            f"VALUES ({pack_id}, '{store_name}', '{glb_family_name}', {glb_user_id}, {price}, '{today}', '{future_date_str}');")
        self.connection_vector.commit()

    def DISPOSE_BATTERY(self, family_name, BATTERY_SIZE):
        self.cursor.execute(f"""
        UPDATE log
            NATURAL JOIN battery
            NATURAL JOIN purchased
            NATURAL JOIN pack
            SET disposed = 1
            WHERE family_name = '{family_name}' 
            AND battery_size = '{BATTERY_SIZE}' 
            AND disposed = 0
            AND end_date IS NOT NULL;
                            """)
