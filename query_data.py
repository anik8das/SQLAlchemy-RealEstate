from sqlalchemy import create_engine, Column, Integer, ForeignKey, func, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.sqltypes import Numeric 
from create import HouseData, AgentData, SoldHouses
import numpy as np
import warnings
warnings.filterwarnings("ignore") # To ignore Decimal warnings in SQLLite

Base = declarative_base() 

# Defining the schema for the commission table to be generated
class CommissionData(Base):
    __tablename__ = 'CommissionData'
    agentID = Column(Integer, ForeignKey(AgentData.agentID), primary_key=True)
    commission = Column(Numeric)

# Function to calculate and return commission for a given sale price
def calculateCommission(soldPrice):
    soldPrice = (float(soldPrice))
    if(soldPrice<100000):
        return 0.1*soldPrice
    elif(soldPrice < 200000):
        return 0.075*soldPrice
    elif(soldPrice < 500000):
        return 0.06*soldPrice
    elif(soldPrice < 1000000):
        return 0.05*soldPrice
    else:
        return 0.04*soldPrice

# Connecting to DB
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(bind=engine) 
Session = sessionmaker(bind=engine)
session = Session()

# Query to get sales by offices in descending order (top 5)
qry1 = session.query(
         HouseData, SoldHouses
         ).filter(
         HouseData.houseID == SoldHouses.houseID,
    ).group_by(
         HouseData.office
    ).order_by(
        desc(SoldHouses.soldPrice)
    ).limit(5).all()

# Query to get sales by agent in descending order (top 5)
qry2 = session.query(
         SoldHouses, AgentData
         ).filter(
         SoldHouses.sellingAgentID == AgentData.agentID,
    ).group_by(
         AgentData.agentID
    ).order_by(
        desc(SoldHouses.soldPrice)
    ).limit(5).all()

# Query to get sales by agent (all)
qry3 = session.query(
         SoldHouses, AgentData
         ).filter(
         SoldHouses.sellingAgentID == AgentData.agentID,
    ).group_by(
         AgentData.agentID
    ).all()

# Query to get house listing and selling data
qry4 = session.query(
    SoldHouses, HouseData
    ).filter(
        SoldHouses.houseID == HouseData.houseID
    ).all()

# Query to get average selling price of houses
qry5 = session.query(func.avg(SoldHouses.soldPrice)).all()

print("\nTop 5 Offices with the most sales (Office | Total Sales):")
for instance in qry1:
    print(instance[0].office, instance[1].soldPrice)

print("\nTop 5 Agents with the most sales and their respective contact info (AgentID | Agent Name | Total Sales | Phone Number | Email):")
for instance in qry2:
    print(instance[1].agentID, instance[1].agentName, instance[0].soldPrice, instance[1].phoneNumber, instance[1].email)

timeGap = []
for instance in qry4:
    timeGap.append((instance[0].dateSold - instance[1].dateListed).days)
print("\nAverage time that a House is on the market:", np.mean(timeGap), 'days')


print('\nAverage selling price of houses sold:', qry5[0][0], "USD")

# Calculating and inserting commission for each agent 
commissionArr = []
for instance in qry3:
    commissionDict = {}
    agentID = instance[1].agentID
    commission = calculateCommission(instance[0].soldPrice)
    commissionDict["agentID"] = agentID
    commissionDict["commission"] = commission
    commissionArr.append(commissionDict)

for item in commissionArr:
    obj = CommissionData(agentID = item['agentID'], commission = item["commission"])
    session.add(obj)
    session.commit()

# Querying the commission table
qry6 = session.query(
    CommissionData
    ).all()

print("\nCommission Table (AgentID | Commission):")
for instance in qry6:
    print(instance.agentID, instance.commission)
