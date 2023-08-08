from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Airdrop, Base

class Database:
    def __init__(self, db_url: str = 'sqlite:///airdrops.db'):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add_airdrop(self, airdrop: Airdrop):
        session = self.Session()
        session.add(airdrop)
        session.commit()

    def get_all_airdrops(self):
        session = self.Session()
        return session.query(Airdrop).all()
