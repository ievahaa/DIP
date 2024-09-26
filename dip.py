import sqlite3

# Izveido savienojumu ar datubāzi (ja datubāze nepastāv, tā tiks izveidota)
conn = sqlite3.connect('dip.db')
cursor = conn.cursor()

# Izveido tabulu Policisti
cursor.execute('''
CREATE TABLE IF NOT EXISTS Policisti (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    vards TEXT NOT NULL,
    uzvards TEXT NOT NULL,
    dienesta_pakape TEXT NOT NULL
)
''')
# Izveido tabulu aizdomas_turamie
cursor.execute('''
CREATE TABLE IF NOT EXISTS aizdomas_turamie (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    aizd_vards TEXT,
    aizd_uzvards TEXT
)
''')

# Izveido tabulu Serijas
cursor.execute('''
CREATE TABLE IF NOT EXISTS Serijas (
    sezonas_nr INTEGER,
    serijas_nr INTEGER,
    beigtais TEXT,
    vainigais TEXT,
    ierocis TEXT,
    motivs TEXT,
    policista_ID INTEGER,
    aizdomas_turama_id INTEGER,
    PRIMARY KEY (Sezonas_nr, Serijas_nr),
    FOREIGN KEY (policista_ID) REFERENCES Policisti(ID),
    FOREIGN KEY (aizdomas_turama_ID) REFERENCES aizdomas_turamie(ID)
)
''')
def datu_ievade():

    jautajumi = {
        "sezonas_nr": "Kura sezona?",
        "serijas_nr": "Kura sērija?",
        "beigtais": "Kas ir upuris (s/v)?",
        "vainigais": "Kas ir vainīgais (s/v)?",
        "ierocis": "Kas bija ierocis?",
        "motivs": "Kāds bija motīvs?"
    }
    atbildes = {}

    for atslēga, jautajums in jautajumi.items():
        atbilde = input(jautajums + " ")
        atbildes[atslēga] = atbilde

    conn = sqlite3.connect('dip.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO Serijas (sezonas_nr, serijas_nr, beigtais, vainigais, ierocis, motivs)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (atbildes["sezonas_nr"], atbildes["serijas_nr"], atbildes["beigtais"], atbildes["vainigais"], atbildes["ierocis"], atbildes["motivs"]))
    
    conn.commit()
    conn.close()
    return atbildes

def datu_izvade():
    conn = sqlite3.connect('dip.db')
    cursor = conn.cursor()

    sezonas_nr = input("Ievadi sezonas numuru: ")
    serijas_nr = input("Ievadi sērijas numuru: ")
    print()
    # Nolasa konkrētās sērijas datus
    cursor.execute('''
        SELECT sezonas_nr, serijas_nr, beigtais, vainigais, ierocis, motivs 
        FROM Serijas
        WHERE sezonas_nr = ? AND serijas_nr = ?
    ''', (sezonas_nr, serijas_nr))

    serija = cursor.fetchone()

    # Izvada prasītās sērijas datus, ja tie eksistē
    if serija:
        print(f"Sērija: S{serija[0]} E{serija[1]}")
        print(f"Upuris: {serija[2]}")
        print(f"Vainīgais: {serija[3]}")
        print(f"Ierocis: {serija[4]}")
        print(f"Motīvs: {serija[5]}")
        print()
    else:
        print("Dati par šo sēriju nav atrasti.")

    conn.close()

def izvelies():
    while True:
        izvele = input("Vai vēlies datus ievadīt vai nolasīt? i/n: \n").lower()
        if izvele == "i":
            return datu_ievade()
        elif izvele == "n":
            return datu_izvade()
        else:
            print("Nesapratu tavu izvēli, mēģini vēlreiz.")

izvelies()
print("Izskatās, ka izdevās")