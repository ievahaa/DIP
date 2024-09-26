import sqlite3

# Izveido savienojumu ar datubāzi (ja datubāze nepastāv, tā tiks izveidota)
conn = sqlite3.connect('dip.db')

# Izveido kursoru
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
# Izveido tabulu Aizdomās turamie
cursor.execute('''
CREATE TABLE IF NOT EXISTS aizdomas_turamie (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    aizd_vards TEXT,
    aizd_uzvards TEXT
)
''')

# Izveido tabulu Sērijas
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


jautajumi = {
    "sezonas_nr": "Kura sezona?",
    "serijas_nr": "Kura serija?",
    "beigtais": "Kas ir upuris? s/v",
    "vainigais": "Kas ir vainīgais? s/v",
    "ierocis": "Kas bija ierocis?",
    "motivs": "Kāds bija motīvs?"
}
atbildes = {}

# Iterē cauri jautājumiem un prasa lietotājam atbildes
for atslēga, jautajums in jautajumi.items():
    atbilde = input(jautajums + " ")
    atbildes[atslēga] = atbilde

# Savienojums ar datubāzi
conn = sqlite3.connect('dip.db')
cursor = conn.cursor()

# SQL pieprasījums datu ievietošanai
cursor.execute('''
    INSERT INTO Serijas (sezonas_nr, serijas_nr, beigtais, vainigais, ierocis, motivs)
    VALUES (?, ?, ?, ?, ?, ?)
''', (atbildes["sezonas_nr"], atbildes["serijas_nr"], atbildes["beigtais"], atbildes["vainigais"], atbildes["ierocis"], atbildes["motivs"]))

# Apstiprina izmaiņas un aizver savienojumu
conn.commit()
conn.close()

print("Izskatās, ka izdevās")