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
    OsobaTableDict = []
    for row in result.all():
      OsobaTableDict.append(row._mapping)
    return OsobaTableDict