import sqlite3
import sqlite3

# Izveido savienojumu ar datubāzi (ja datubāze nepastāv, tā tiks izveidota)
conn = sqlite3.connect('dip.db')

# Izveido kursoru
cursor = conn.cursor()

# Izveido tabulu Policisti
cursor.execute('''
CREATE TABLE IF NOT EXISTS Policisti (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Vards TEXT NOT NULL,
    Uzvards TEXT NOT NULL,
    DienestaPakape TEXT NOT NULL
)
''')

# Izveido tabulu Sērijas
cursor.execute('''
CREATE TABLE IF NOT EXISTS Serijas (
    Sezonas_nr INTEGER,
    Serijas_nr INTEGER,
    Beigtais TEXT,
    Vainigais TEXT,
    Ierocis TEXT,
    Motivs TEXT,
    Izmekletajs_ID INTEGER,
    PRIMARY KEY (Sezonas_nr, Serijas_nr),
    FOREIGN KEY (Izmekletajs_ID) REFERENCES Personas(ID)
)
''')

# Apstiprina izmaiņas un aizver savienojumu
conn.commit()
conn.close()

print("Datubāze un tabulas veiksmīgi izveidotas!")
