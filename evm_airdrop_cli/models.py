## models.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Airdrop(Base):
    __tablename__ = 'airdrops'

    id = Column(Integer, primary_key=True)
    evm_chain = Column(String)
    number_of_tokens = Column(Integer)
    is_successful = Column(Boolean, default=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    def __init__(self, evm_chain: str, number_of_tokens: int):
        self.evm_chain = evm_chain
        self.number_of_tokens = number_of_tokens

    def __repr__(self):
        return f"<Airdrop(evm_chain='{self.evm_chain}', number_of_tokens='{self.number_of_tokens}', is_successful='{self.is_successful}', timestamp='{self.timestamp}')>"
