import sqlite3
from models.model import Reservation

DATABASE_NAME = 'hotel_reservation.db'

def initialize_database():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.execute('PRAGMA foreign_keys = ON') 
    conn.close()

def create_tables():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    
    create_reservations_table = '''
    CREATE TABLE IF NOT EXISTS reservations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        room_type TEXT NOT NULL,
        check_in_date DATE NOT NULL,
        check_out_date DATE NOT NULL,
        guest_name TEXT NOT NULL, 
        email TEXT NOT NULL,
        total_cost REAL NOT NULL,
        reservation_status TEXT NOT NULL
    );
    '''
    
    cursor.execute(create_reservations_table)
    conn.commit()
    conn.close()


def connect_to_database():
    return sqlite3.connect(DATABASE_NAME)


def create_reservation(reservation):
    conn = connect_to_database()
    cursor = conn.cursor()

    insert_query = '''
    INSERT INTO reservations (room_type, check_in_date, check_out_date, guest_name, email, total_cost, reservation_status)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    '''
    
    cursor.execute(insert_query, (reservation.room_type, reservation.check_in_date, reservation.check_out_date, reservation.guest_name, reservation.email, reservation.total_cost, reservation.reservation_status))
    reservation_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return reservation_id


def get_reservation_by_id(reservation_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    
    select_query = '''
    SELECT * FROM reservations WHERE id = ?
    '''
    
    cursor.execute(select_query, (reservation_id,))
    reservation_row = cursor.fetchone()

    if reservation_row:
        column_names = [description[0] for description in cursor.description]

        reservation_dict = dict(zip(column_names, reservation_row))
    else:
        reservation_dict = None
    
    conn.close()
    
    return reservation_dict