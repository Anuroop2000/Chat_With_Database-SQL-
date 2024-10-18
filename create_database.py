import sqlite3

def create_concerts_tickets_database():
    conn = sqlite3.connect('concerts_tickets_database.db')
    cursor = conn.cursor()

    # Clear existing tables
    cursor.execute("DROP TABLE IF EXISTS tickets")
    cursor.execute("DROP TABLE IF EXISTS concerts")
    cursor.execute("DROP TABLE IF EXISTS venues")
    cursor.execute("DROP TABLE IF EXISTS customers")
    cursor.execute("DROP TABLE IF EXISTS artists")

    # Create tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS artists (
        Artist_ID INTEGER PRIMARY KEY,
        Artist_Name TEXT,
        Genre TEXT,
        Email TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS venues (
        Venue_ID INTEGER PRIMARY KEY,
        Venue_Name TEXT,
        Location TEXT,
        Capacity INTEGER
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS concerts (
        Concert_ID INTEGER PRIMARY KEY,
        Artist_ID INTEGER,
        Venue_ID INTEGER,
        Concert_Date TEXT,
        Ticket_Price REAL,
        Tickets_Available INTEGER,
        FOREIGN KEY (Artist_ID) REFERENCES artists(Artist_ID),
        FOREIGN KEY (Venue_ID) REFERENCES venues(Venue_ID)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
        Customer_ID INTEGER PRIMARY KEY,
        Customer_Name TEXT,
        Customer_Country TEXT,
        Email TEXT,
        Date_Of_Birth TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS tickets (
        Ticket_ID INTEGER PRIMARY KEY,
        Concert_ID INTEGER,
        Customer_ID INTEGER,
        Purchase_Date TEXT,
        Quantity INTEGER,
        Payment_Method TEXT,
        FOREIGN KEY (Concert_ID) REFERENCES concerts(Concert_ID),
        FOREIGN KEY (Customer_ID) REFERENCES customers(Customer_ID)
    )''')

    # Sample data for artists (ensure unique Artist_IDs)
    artists_data = [
        (1, 'The Weeknd', 'R&B', 'theweeknd@example.com'),
        (2, 'Pitbull', 'Hip Hop', 'pitbull@example.com'),
        (3, 'Coldplay', 'Rock', 'coldplay@example.com'),
        (4, 'Dua Lipa', 'Pop', 'dualipa@example.com'),
        (5, 'Billie Eilish', 'Pop', 'billieeilish@example.com'),
        (6, 'Taylor Swift', 'Pop', 'taylorswift@example.com'),
        (7, 'Drake', 'Hip Hop', 'drake@example.com'),
        (8, 'Ed Sheeran', 'Pop', 'edsheeran@example.com'),
        (9, 'Bruno Mars', 'Pop', 'brunomars@example.com'),
        (10, 'Ariana Grande', 'Pop', 'arianagrande@example.com'),
        (11, 'Katy Perry', 'Pop', 'katyperry@example.com'),
        (12, 'Justin Bieber', 'Pop', 'justinbieber@example.com'),
        (13, 'Shawn Mendes', 'Pop', 'shawnmendes@example.com'),
        (14, 'Maroon 5', 'Pop', 'maroon5@example.com'),
        (15, 'Beyoncé', 'R&B', 'beyonce@example.com'),
        (16, 'Lady Gaga', 'Pop', 'ladygaga@example.com'),
        (17, 'Sam Smith', 'Pop', 'samsmith@example.com'),
        (18, 'Post Malone', 'Hip Hop', 'postmalone@example.com'),
        (19, 'Zayn Malik', 'Pop', 'zayn@example.com'),
        (20, 'Halsey', 'Pop', 'halsey@example.com'),
    ]

    # Sample data for venues
    venues_data = [
        (1, 'Madison Square Garden', 'New York, NY', 20000),
        (2, 'Staples Center', 'Los Angeles, CA', 19068),
        (3, 'The O2', 'London, UK', 20000),
        (4, 'Tokyo Dome', 'Tokyo, Japan', 55000),
        (5, 'Allianz Arena', 'Munich, Germany', 75000),
    ]

    # Sample data for concerts
    concerts_data = [
        (1, 1, 1, '2024-06-10', 150.00, 5000),
        (2, 2, 2, '2024-06-15', 120.00, 3000),
        (3, 3, 3, '2024-06-20', 130.00, 2500),
        (4, 4, 4, '2024-06-25', 180.00, 4000),
        (5, 5, 5, '2024-07-01', 200.00, 6000),
        (6, 6, 1, '2024-07-05', 170.00, 4500),
        (7, 7, 2, '2024-07-10', 110.00, 5500),
        (8, 8, 3, '2024-07-15', 160.00, 3500),
        (9, 9, 4, '2024-07-20', 140.00, 6500),
        (10, 10, 5, '2024-07-25', 190.00, 7000),
        (11, 11, 1, '2024-08-01', 210.00, 3000),
        (12, 12, 2, '2024-08-05', 175.00, 3800),
        (13, 13, 3, '2024-08-10', 160.00, 4200),
        (14, 14, 4, '2024-08-15', 150.00, 3900),
        (15, 15, 5, '2024-08-20', 220.00, 3100),
        (16, 16, 1, '2024-08-25', 180.00, 2500),
        (17, 17, 2, '2024-09-01', 165.00, 2800),
        (18, 18, 3, '2024-09-05', 140.00, 4200),
        (19, 19, 4, '2024-09-10', 190.00, 3500),
        (20, 20, 5, '2024-09-15', 200.00, 3700),
    ]

    # Sample data for customers
    customers_data = [
        (1, 'Alice Johnson', 'USA', 'alice@example.com', '1990-01-15'),
        (2, 'Bob Smith', 'Canada', 'bob@example.com', '1985-05-20'),
        (3, 'Charlie Brown', 'UK', 'charlie@example.com', '1992-03-10'),
        (4, 'David Wilson', 'Australia', 'david@example.com', '1988-12-05'),
        (5, 'Eva Green', 'Germany', 'eva@example.com', '1995-07-25'),
        (6, 'Frank Wright', 'France', 'frank@example.com', '1993-08-30'),
        (7, 'Grace Lee', 'Japan', 'grace@example.com', '1989-11-18'),
        (8, 'Henry Adams', 'USA', 'henry@example.com', '1991-09-22'),
        (9, 'Ivy Clark', 'Brazil', 'ivy@example.com', '1994-02-14'),
        (10, 'Jack White', 'India', 'jack@example.com', '1987-06-07'),
        (11, 'Karen Black', 'USA', 'karen@example.com', '1990-04-16'),
        (12, 'Liam Brown', 'UK', 'liam@example.com', '1986-10-28'),
        (13, 'Mia Davis', 'Canada', 'mia@example.com', '1992-12-09'),
        (14, 'Noah Wilson', 'Australia', 'noah@example.com', '1991-03-14'),
        (15, 'Olivia Smith', 'Germany', 'olivia@example.com', '1988-05-22'),
        (16, 'Peter Johnson', 'France', 'peter@example.com', '1995-07-01'),
        (17, 'Quinn Taylor', 'Japan', 'quinn@example.com', '1993-11-15'),
        (18, 'Rose Thompson', 'Brazil', 'rose@example.com', '1989-09-19'),
        (19, 'Sophia White', 'India', 'sophia@example.com', '1994-03-21'),
        (20, 'Tom Harris', 'USA', 'tom@example.com', '1986-08-17'),
    ]

    # Sample data for tickets
    tickets_data = [
        (1, 1, 1, '2024-06-01', 2, 'Credit Card'),
        (2, 2, 2, '2024-06-02', 1, 'Debit Card'),
        (3, 3, 3, '2024-06-03', 4, 'PayPal'),
        (4, 4, 4, '2024-06-04', 3, 'Credit Card'),
        (5, 5, 5, '2024-06-05', 2, 'Credit Card'),
        (6, 6, 6, '2024-06-06', 1, 'Cash'),
        (7, 7, 7, '2024-06-07', 5, 'Debit Card'),
        (8, 8, 8, '2024-06-08', 2, 'Credit Card'),
        (9, 9, 9, '2024-06-09', 3, 'PayPal'),
        (10, 10, 10, '2024-06-10', 1, 'Credit Card'),
        (11, 11, 11, '2024-06-11', 2, 'Debit Card'),
        (12, 12, 12, '2024-06-12', 4, 'Credit Card'),
        (13, 13, 13, '2024-06-13', 3, 'Cash'),
        (14, 14, 14, '2024-06-14', 5, 'Credit Card'),
        (15, 15, 15, '2024-06-15', 2, 'PayPal'),
        (16, 16, 16, '2024-06-16', 1, 'Credit Card'),
        (17, 17, 17, '2024-06-17', 4, 'Debit Card'),
        (18, 18, 18, '2024-06-18', 2, 'Credit Card'),
        (19, 19, 19, '2024-06-19', 3, 'Cash'),
        (20, 20, 20, '2024-06-20', 1, 'PayPal'),
    ]

    # Insert sample data into tables
    cursor.executemany('INSERT INTO artists VALUES (?, ?, ?, ?)', artists_data)
    cursor.executemany('INSERT INTO venues VALUES (?, ?, ?, ?)', venues_data)
    cursor.executemany('INSERT INTO concerts VALUES (?, ?, ?, ?, ?, ?)', concerts_data)
    cursor.executemany('INSERT INTO customers VALUES (?, ?, ?, ?, ?)', customers_data)
    cursor.executemany('INSERT INTO tickets VALUES (?, ?, ?, ?, ?, ?)', tickets_data)

    conn.commit()
    conn.close()

    print("Concerts and tickets database created successfully!")

if __name__ == "__main__":
    create_concerts_tickets_database()
