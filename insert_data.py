
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date
from create import HouseData, AgentData, SoldHouses

# Connecting to DB
engine = create_engine('sqlite:///database.db',
    echo=True)
engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

# Listing house data to be inserted
houses = [
    {'houseID': 1,'sellerName': 'Aniket','numberOfRooms': 2,'numberOfBathrooms': 1,'listingPrice': 392234, 'zipcode': '10102', 'office': 'New York','listingAgentID': 1, 'status': 'sold', 'dateListed': date.fromisoformat('2017-12-02')},
    {'houseID': 2,'sellerName': 'Ha','numberOfRooms': 3,'numberOfBathrooms': 2,'listingPrice': 786334, 'zipcode': '90021', 'office': 'Los Angeles','listingAgentID': 2, 'status': 'listed', 'dateListed': date.fromisoformat('2015-11-01')},
    {'houseID': 3,'sellerName': 'Nikita','numberOfRooms': 2.5,'numberOfBathrooms': 1,'listingPrice': 193564, 'zipcode': '02102', 'office': 'Boston','listingAgentID': 3, 'status': 'listed', 'dateListed': date.fromisoformat('2017-02-23')},
    {'houseID': 4,'sellerName': 'Hovik','numberOfRooms': 2.5,'numberOfBathrooms': 1.5,'listingPrice': 233627, 'zipcode': '94322', 'office': 'San Francisco','listingAgentID': 4, 'status': 'listed', 'dateListed': date.fromisoformat('2016-10-05')},
    {'houseID': 5,'sellerName': 'Sona','numberOfRooms': 1,'numberOfBathrooms': 1,'listingPrice': 168564, 'zipcode': '98114', 'office': 'Seattle','listingAgentID': 2, 'status': 'sold', 'dateListed': date.fromisoformat('2015-05-15')},
    {'houseID': 6,'sellerName': 'Phuong','numberOfRooms': 1.5,'numberOfBathrooms': 1,'listingPrice': 101000, 'zipcode': '02742', 'office': 'Boston','listingAgentID': 5, 'status': 'listed', 'dateListed': date.fromisoformat('2016-04-30')},
    {'houseID': 7,'sellerName': 'Ara','numberOfRooms': 1,'numberOfBathrooms': 1,'listingPrice': 157035, 'zipcode': '94363', 'office': 'San Francisco','listingAgentID': 1, 'status': 'listed', 'dateListed': date.fromisoformat('2018-11-04')},
    {'houseID': 8,'sellerName': 'Chloe','numberOfRooms': 4,'numberOfBathrooms': 3,'listingPrice': 450332, 'zipcode': '02541', 'office': 'Boston','listingAgentID': 3, 'status': 'sold', 'dateListed': date.fromisoformat('2016-03-12')},
    {'houseID': 9,'sellerName': 'Esther','numberOfRooms': 2,'numberOfBathrooms': 1,'listingPrice': 230123, 'zipcode': '10234', 'office': 'New York','listingAgentID': 5, 'status': 'listed', 'dateListed': date.fromisoformat('2015-09-30')},
    {'houseID': 10,'sellerName': 'Gabriel','numberOfRooms': 1,'numberOfBathrooms': 1,'listingPrice': 70000, 'zipcode': '02123', 'office': 'Boston','listingAgentID': 3, 'status': 'listed', 'dateListed': date.fromisoformat('2014-12-04')},
    {'houseID': 11,'sellerName': 'Fellipe','numberOfRooms': 2,'numberOfBathrooms': 1.5,'listingPrice': 250120, 'zipcode': '94563', 'office': 'San Francisco','listingAgentID': 4, 'status': 'sold', 'dateListed': date.fromisoformat('2015-04-23')},
    {'houseID': 12,'sellerName': 'Mateus','numberOfRooms': 2.5,'numberOfBathrooms': 2,'listingPrice': 190345, 'zipcode': '10246', 'office': 'New York','listingAgentID': 1, 'status': 'listed', 'dateListed': date.fromisoformat('2016-02-23')},
    {'houseID': 13,'sellerName': 'Ariane','numberOfRooms': 2,'numberOfBathrooms': 1,'listingPrice': 286334, 'zipcode': '90221', 'office': 'Los Angeles','listingAgentID': 5, 'status': 'sold', 'dateListed': date.fromisoformat('2017-02-01')},
    {'houseID': 14,'sellerName': 'Mackenzie','numberOfRooms': 4,'numberOfBathrooms': 3,'listingPrice': 586334, 'zipcode': '33101', 'office': 'Miami','listingAgentID': 3, 'status': 'sold', 'dateListed': date.fromisoformat('2014-05-21')},
    {'houseID': 15,'sellerName': 'Ivana','numberOfRooms': 3,'numberOfBathrooms': 2,'listingPrice': 386334, 'zipcode': '600742', 'office': 'Chicago','listingAgentID': 6, 'status': 'sold', 'dateListed': date.fromisoformat('2017-12-09')},
    ]

# Inserting data into the table
for item in houses:
    obj = HouseData(houseID = item['houseID'], sellerName = item["sellerName"], numberOfRooms = item["numberOfRooms"], numberOfBathrooms = item["numberOfBathrooms"], listingPrice = item["listingPrice"], zipcode = item["zipcode"], office = item["office"], listingAgentID = item["listingAgentID"], status = item["status"], dateListed = item["dateListed"])
    session.add(obj)
    session.commit()

# Agent data to be inserted
agents = [
    {'agentID': 1,'agentName': 'Paul', 'phoneNumber': '9281990746', 'email': 'paul@real-estate.com'},
    {'agentID': 2,'agentName': 'Ingrid', 'phoneNumber': '4961990746', 'email': 'ingrid@real-estate.com'},
    {'agentID': 3,'agentName': 'Corin', 'phoneNumber': '6538990746', 'email': 'corin@real-estate.com'},
    {'agentID': 4,'agentName': 'Gaurish', 'phoneNumber': '5038960746', 'email': 'gaurish@real-estate.com'},
    {'agentID': 5,'agentName': 'Parker', 'phoneNumber': '3498990746', 'email': 'parker@real-estate.com'},
    {'agentID': 6,'agentName': 'Gacoka', 'phoneNumber': '3508990746', 'email': 'gacoka@real-estate.com'},
]

# Inserting data into table
for item in agents:
    obj = AgentData(agentID = item['agentID'], agentName = item["agentName"], phoneNumber = item["phoneNumber"], email = item["email"])
    session.add(obj)
    session.commit()

# Selling house data to be inserted
transactions = [
    {'houseID': 1,'sellingAgentID': 1, 'soldPrice': 333113.5, 'dateSold': date.fromisoformat('2018-02-12')},
    {'houseID': 5,'sellingAgentID': 4, 'soldPrice': 132728, 'dateSold': date.fromisoformat('2016-01-10')},
    {'houseID': 8,'sellingAgentID': 2, 'soldPrice': 440120, 'dateSold': date.fromisoformat('2017-01-04')},
    {'houseID': 11,'sellingAgentID': 3, 'soldPrice': 200000, 'dateSold': date.fromisoformat('2015-11-20')},
    {'houseID': 13,'sellingAgentID': 5, 'soldPrice': 235000, 'dateSold': date.fromisoformat('2017-12-20')},
    {'houseID': 14,'sellingAgentID': 6, 'soldPrice': 470000, 'dateSold': date.fromisoformat('2015-01-02')},    
    {'houseID': 15,'sellingAgentID': 2, 'soldPrice': 300000, 'dateSold': date.fromisoformat('2018-01-01')},
]

# Inserting data into table
for item in transactions:
    obj = SoldHouses(houseID = item['houseID'], sellingAgentID = item["sellingAgentID"], soldPrice = item["soldPrice"], dateSold = item["dateSold"])
    session.add(obj)
    session.commit()
