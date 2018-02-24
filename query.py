import mysql.connector, sys

def executeSQL(conn, queryTerm):
    cursor = conn.cursor()
    query = queryTerm
    cursor.execute(query)
    result = cursor.fetchall()    
    for row in result:
     print row

hostname = ''
username = ''
password = ''
database = ''

try:
   sys.argv[1]
except IndexError:
   print "Error - missing query "
   sys.exit(1)
else:
   queryWord =""
   for arg in sys.argv[1:]:
    queryWord += arg+" "

connection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
executeSQL(connection,queryWord)
connection.close()


