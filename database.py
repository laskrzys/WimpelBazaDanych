from sqlalchemy import create_engine, text
import os
connectionString = os.environ['connectionString']
engine = create_engine(connectionString,
                      connect_args={
                        "ssl": {
                          "ssl_ca": "/etc/ssl/cert.pem"
                        }
                      })

def returnOsobaTableDict():
  with engine.connect() as conn:
    result = conn.execute(text("select * from Osoba"))
    #"select * from Osoba WHERE id = :val"
    #val = id (3 etc)
    OsobaTableDict = []
    for row in result.all():
      OsobaTableDict.append(row._mapping)
    return OsobaTableDict

def addosobatodb(osobadata):
  with engine.connect() as conn:
    query = text("INSERT INTO Osoba (Imie, Nazwisko, Email, Telefon) VALUES (:Imie, :Nazwisko, :Email, :Telefon)")
    _Imie=osobadata['Imie']
    _Nazwisko=osobadata['Nazwisko']
    _Email=osobadata['Email']
    _Telefon=osobadata['Telefon']

    conn.execute(statement=query, parameters=dict(Imie=_Imie, Nazwisko=_Nazwisko, Email=_Email,         Telefon=_Telefon))

def droposobaindp(idosoba):
  with engine.cnnecit() as conn:
    query = text("DELETE FROM Osoba WHERE idOsoba = :idosoba")
    _idosoba = idosoba
    print(idosoba)
    conn.execute(statement=query, parameters=dict(idosoba=_idosoba))
