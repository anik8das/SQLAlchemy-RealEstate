

from sqlalchemy import create_engine, Column, Text, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.sqltypes import DateTime, Numeric, Enum
import enum

# Enum for house status
class listedEnum(enum.Enum):
    sold = 1
    listed = 2

# Connecting to DB
engine = create_engine('sqlite:///database.db',
    echo=True)
engine.connect()

Base = declarative_base() 

# Declaring Schemas for required tables (There are no repeated elements, tables are normalized)
class AgentData(Base):
    __tablename__ = 'AgentData'
    agentID = Column(Integer, primary_key=True)
    agentName = Column(Text)
    phoneNumber = Column(Text)
    email = Column(Text)

class HouseData(Base):
    __tablename__ = 'HouseData'
    houseID = Column(Integer, primary_key = True)
    sellerName = Column(Text)
    numberOfRooms = Column(Numeric)
    numberOfBathrooms = Column(Numeric)
    listingPrice = Column(Numeric)
    zipcode = Column(Text)
    office = Column(Text)
    listingAgentID = Column(Integer, ForeignKey(AgentData.agentID), )
    status = Column(Text,Enum(listedEnum))
    dateListed = Column(DateTime)

class SoldHouses(Base):
    __tablename__ = 'SoldHouses'
    houseID = Column(Integer, ForeignKey(HouseData.houseID), primary_key=True)
    # Indexing on Agent ID and Sale price as those will be queried the most frequently 
    sellingAgentID = Column(Integer, ForeignKey(AgentData.agentID), index = True)
    soldPrice = Column(Numeric, index = True)
    dateSold = Column(DateTime)

# Creating tables
Base.metadata.create_all(bind=engine) 
Session = sessionmaker(bind=engine)
session = Session()
