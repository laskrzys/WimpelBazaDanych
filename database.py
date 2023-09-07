from sqlalchemy import create_engine, text
import os

connectionString = os.environ['connectionString']
engine = create_engine(connectionString,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def returnOsobaTableDict():
  with engine.connect() as conn:
    result = conn.execute(text("select * from Osoba"))
    #"select * from Osoba WHERE id = :val"
    #val = id (3 etc)
    OsobaTableDict = []
    for row in result.all():
      OsobaTableDict.append(row._mapping)
    return OsobaTableDict


def returnStanicaTableDict():
  with engine.connect() as conn:
    result = conn.execute(text("select * from Stanica"))
    StanicaTableDict = []
    for row in result.all():
      StanicaTableDict.append(row._mapping)
    return StanicaTableDict


def addosobatodb(osobadata):
  with engine.connect() as conn:
    query = text(
      "INSERT INTO Osoba (Imie, Nazwisko, Email, Telefon) VALUES (:Imie, :Nazwisko, :Email, :Telefon)"
    )
    _Imie = osobadata['Imie']
    _Nazwisko = osobadata['Nazwisko']
    _Email = osobadata['Email']
    _Telefon = osobadata['Telefon']

    conn.execute(statement=query,
                 parameters=dict(Imie=_Imie,
                                 Nazwisko=_Nazwisko,
                                 Email=_Email,
                                 Telefon=_Telefon))


def droposobaindp(idosoba):
  with engine.connect() as conn:
    query = text("DELETE FROM Osoba WHERE idOsoba = :idosoba")
    _idosoba = idosoba['Id']
    print(idosoba)
    conn.execute(statement=query, parameters=dict(idosoba=_idosoba))


def raport1indb(data):
  with engine.connect() as conn:
    query = text(
      "SELECT COUNT (*) as LiczbaNapraw FROM Uszkodzenie WHERE DataNaprawy >= :dataod AND idCzlonek = :idosoba"
    )
    _idosoba = data['idosoby']
    _dataod = data['dataod']
    result = conn.execute(statement=query,
                          parameters=dict(idosoba=_idosoba, dataod=_dataod))
    results_as_dict = result.mappings().all()
    return results_as_dict


def raport2indb(data):
  with engine.connect() as conn:
    query = text(
      "SELECT COUNT (*) as LiczbaSzkod FROM Uszkodzenie WHERE DataZepsucia >= :dataod AND idCzlonek = :idosoba"
    )
    _idosoba = data['idosoby']
    _dataod = data['dataod']
    result = conn.execute(statement=query,
                          parameters=dict(idosoba=_idosoba, dataod=_dataod))
    results_as_dict = result.mappings().all()
    return results_as_dict


def raport3p1indb():
  with engine.connect() as conn:
    query = text("""
CREATE OR REPLACE VIEW OstatnieZepsucie AS SELECT Przedmiot.Nazwa, Przedmiot.Stan, Przedmiot.idStanica, MAX(Uszkodzenie.DataZepsucia) as ostatniTest FROM Przedmiot JOIN Uszkodzenie USING(idPrzedmiot)	WHERE Przedmiot.Stan = 'smiec' GROUP BY Przedmiot.idPrzedmiot
 """)
    conn.execute(query)


def raport3p2indb(data):
  with engine.connect() as conn:
    query = text("""
    SELECT COUNT(*) as liczbaSmieci FROM OstatnieZepsucie WHERE ostatniTest >= :DataOd AND idStanica = :IDStanicy 
    """)
    _idstanicy = data['idstanicy']
    _dataod = data['dataod']
    result = conn.execute(statement=query,
                          parameters=dict(IDStanicy=_idstanicy,
                                          DataOd=_dataod))
    results_as_dict = result.mappings().all()
    return results_as_dict
