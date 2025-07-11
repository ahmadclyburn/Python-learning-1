import mysql.connector
class DataConnector:
 def __init__(self, host, user, password, database):
    try:
        self.connection = mysql.connector.connect(
            host ="localhost",
            user ="root",
            password ="yearup24",
            database = "dealershipworkshop"
        )
        print("Connection successful!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
 def close(self):
    if self.connection.is_connected():
        self.connection.close()
        print("Connection to the database has been closed.")

if __name__ == "__main__":
    connector = DataConnector("localhost", "root", "yearup2024", "dealershipworkshop")
    # You can add more checks or queries here if needed
    connector.close()