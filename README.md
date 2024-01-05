# MySQL Auto-credentials configurator for Python

Automatically connect your Python program with your MySQL database by running this python script and entering your credentials in the asking output.


## How to run:

Clone the project and copy the ```credent.py``` to your project folder.

Then install the ```mysql.connector``` library by creating a virtual environment through powershell in your project directory by the below commands:
- For Windows:
```powershell
python -m venv venv
venv/Scripts/activate.ps1
```
- For Linux / macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```
To install the library:
```python
pip install mysql-connector-python
```
Then simply run the ```credent.py``` in the virtual environment which you created by:

```bash
  python credent.py
```

Follow all the steps the script says.

That's It! You have configured the MySQL credentials.

Now move to your main python program and enter the following lines to connect it to the mysql credentials which you entered before.
```python
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'mysql_cred_data'))        
from cred import connect_to_database

connection = connect_to_database()
```
To connect the cursor, you can:
```python
mycursor = connection.cursor()
```

Now You have successfully connected your python program to your MySQL Database!

## Further Configurations

Now you should see a new directory in your project directory called ```mysql-cred-data```. This is where all your MySQL credentials are stored. You can edit the ```cred.py``` file or any config files according to your needs. Or you can simply run the ```cred.py``` once again to re-configure your connection.


## Author

- Sidharth Prabhu

