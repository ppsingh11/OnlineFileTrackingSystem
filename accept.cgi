#!/usr/bin/python

import cgi, cgitb 
import mysql.connector as mariadb
form = cgi.FieldStorage()

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<link rel="stylesheet" type="text/css" href="login.css">'

print '</head>'
print '<body>'
mariadb_connection = mariadb.connect(user='pps', password='pps', database='student')
	
cursor = mariadb_connection.cursor(buffered=True)
post=form.getvalue('post')
acc=form.getvalue('accept')
file_type=form.getvalue('file')
id=file_type

if file_type[0] == 'M':
	file_type="Medical"
elif  file_type[0] == 'L':
	file_type="Leave_app"
elif  file_type[0] == 'R':
	file_type="Railway_conces"
elif  file_type[0] == 'P':
	file_type="Project_file"
der= "update {0} set {1} = '1' where id='{2}' ".format(file_type,post,id)

cursor.execute(der)
mariadb_connection.commit()
print '<h3 style="color:red"><center>Accepted</center></h3>'
print '</body>'
print '</html>'
