import pymssql
import getpass

def main():
	database_server = input("Database server: ")
	database = input("Database: ")
	username = input("Windows AD Username: ")
	password = getpass.getpass("Password: ")
	with pymssql.connect(database_server, username, password, database) as conn:
		with conn.cursor(as_dict=True) as cursor:
			cursor.execute('SELECT TOP 10 * FROM dbo.ACCOUNT')
			for row in cursor:
				print("ID={}, Name={}".format(row['ID'], row['NAME']))

if __name__ == '__main__':
	main()