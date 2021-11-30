SQLAlchemy implementation of a real estate company representation. Used Data Normalization for reducing redundancy and Indices to retrieve data more quickly.

- create.py creates the Tables
- insert_data.py inserts the data into the Tables
- query_data.py executes the required queries and creates the commission table. It prints out the required results.<br>

Steps to run:<br>
(Mac)
- python3.6 -m venv venv
- source venv/bin/activate
- pip3 install -r requirements.txt
- python3 create.py
- python3 insert_data.py
- python3 query_data.py<br>

(Windows, substitute python instead of python3 if it isn't recognized)
- python3.6 -m venv venv
- venv\Scripts\activate.bat
- pip3 install -r requirements.txt
- python3 create.py
- python3 insert_data.py
- python3 query_data.py