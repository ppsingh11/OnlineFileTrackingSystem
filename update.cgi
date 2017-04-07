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
f_id=form.getvalue('file_id')
post=form.getvalue('post')
acc=form.getvalue('accept')
print acc
print post
print f_id
if f_id!=None:
	mariadb_connection = mariadb.connect(user='pps', password='pps', database='student')
	
	cursor = mariadb_connection.cursor(buffered=True)
	cursor.execute("select * from  Registartion_detail where F_ID='{0}' ".format(f_id))
	st=cursor.fetchone()
	if st == None:
		print '''<h3>No such file exits !!.<br>
			Enter valid file ID.</h3><br><br>'''
		
	else :
		
		
		if post[0]=='H':
			post="HOD"
		elif post[0]=='R':
			post="REGISTRAR"
		elif post[0]=='A':
			post="ASSISTANT"
		elif post[0]=='D' and post[1]=='I':
			post="DIRECTOR"
		elif post[0]=='D':
			post="DEAN"
		print '<h3><center>File details</center></h3>'
		print '<h4><center>File_id : %s</center></h4>' %(st[0])
		print '<h4><center>Name : %s</center></h4>' %(st[1])
		print '<h4><center>Institute_id : %s</center></h4>' %(st[2])
		print '<h4><center>Branch : %s</center></h4>' %(st[3])	
		print '<h4><center>semester : %s</center></h4>' %(st[4])
		print '<h4><center>Email Id : %s</center></h4>' %(st[5])
		print '<h4><center>Contact Number: %s</center></h4>' %(st[6])
		print post
		print '<br><br>'
		print '<center>'
		
		print '<form action="accept.cgi" method="get" >'
		print '<input id="fid" type="submit" value="Accept & Forward"><br>'
		print '<input type="hidden" value="A" name="accept" >'
		print '<input type="hidden" value=%s  name="post" >'%(post)
		print '<input type="hidden" value=%s  name="file" >'%(f_id)
		print '</form>'
		print '<form action="#" method="post" >'
		print '<input id="fid1" type=text name="f_id" placeholder="Reason for Rejection" required><br>'
		print '<input id="fid" type="submit" value="Reject"><br>'
		print '</form>'
		print '</center>'
	
else:
	print 'wrong id'




print '</body>'
print '</html>'


