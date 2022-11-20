import datetime
import sqlite3


class Database:
    def __init__(self, path):
        self.connection = sqlite3.connect(f"{path}")
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS employee 
            (
                id INTEGER PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                age INTEGER NOT NULL,
                email VARCHAR(50) UNIQUE NOT NULL,
                designation VARCHAR(50),
                doj DATE NOT NULL,
                gender VARCHAR(6) NOT NULL,
                contact VARCHAR(10) UNIQUE NOT NULL,
                address VARCHAR(100) NOT NULL
            );"""
        )
        self.connection.commit()

    def insert_002(self, name, age, email, designation, doj, gender, contact, address):
        self.cursor.execute(
            f"""
            INSERT INTO employee (name, age, email, designation, doj, gender, contact, address)
            VALUES (
                '{name}', '{age}', '{email}', '{designation}', '{doj}', '{gender}', '{contact}', '{address}'
            );
            """
        )

        self.connection.commit()

    def fetch_all_002(self):
        self.cursor.execute("SELECT * FROM employee;")
        rows = self.cursor.fetchall()
        return rows

    def fetch_002(self, id):
        self.cursor.execute(f"SELECT * FROM employee WHERE id={id};")
        rows = self.cursor.fetchone()
        return rows

    def fetch_by_contact_002(self, contact):
        self.cursor.execute(f"SELECT * FROM employee WHERE contact='{contact}';")
        rows = self.cursor.fetchall()
        return rows

    def fetch_by_email_002(self, email):
        self.cursor.execute(f"SELECT * FROM employee WHERE email='{email}';")
        rows = self.cursor.fetchall()
        return rows

    def update_002(
        self, id, name, age, email, designation, doj, gender, contact, address
    ):
        self.cursor.execute(
            f"""
            UPDATE employee
            SET name='{name}', age='{age}', email='{email}', designation='{designation}', doj='{doj}', gender='{gender}', contact='{contact}', address='{address}' WHERE id={id};
            """
        )

    def delete_002(self, id):
        self.cursor.execute(f"DELETE FROM employee WHERE id={id};")
        self.connection.commit()

    def __del__(self):
        self.connection.close()
