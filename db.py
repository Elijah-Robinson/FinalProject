#Database Setup (db.py):
#Use the sqlite3 library to connect to the SQLite database (reservations.db).
#Implement functions to insert, update, delete, and query data from the database.
import sqlite3

DATABASE = 'reservations.db'

def create_tables():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS reservations (
                    id INTEGER PRIMARY KEY,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    seat_row INTEGER NOT NULL,
                    seat_column INTEGER NOT NULL,
                    e_ticket_number TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )''')
    conn.commit()
    conn.close()

def get_seating_chart():
    seating_chart = [[None for _ in range(4)] for _ in range(12)]
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT first_name, last_name, seat_row, seat_column FROM reservations')
    reservations = c.fetchall()
    for reservation in reservations:
        first_name, last_name, seat_row, seat_column = reservation
        seating_chart[seat_row][seat_column] = f'{first_name} {last_name}'
    conn.close()
    return seating_chart

def add_reservation(first_name, last_name, seat_row, seat_column, e_ticket_number):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''INSERT INTO reservations (first_name, last_name, seat_row, seat_column, e_ticket_number)
                 VALUES (?, ?, ?, ?, ?)''', (first_name, last_name, seat_row, seat_column, e_ticket_number))
    conn.commit()
    conn.close()
