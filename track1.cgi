#!/usr/bin/python

import cgi, cgitb 
import mysql.connector as mariadb
form = cgi.FieldStorage()

print "Content-type:text/html\r\n\r\n"

var = form.getvalue("f_id")
if var[0]=='M':
	f_type="Medical"
elif var[0]=='L':
	f_type="Leave_app"
elif var[0]=='P':
	f_type="Project_file"
elif var[0]=='R':
	f_type="Railway_conces"

c1="aqua"
c2="aqua"
c3="aqua"
c4="aqua"
status = "under process"
mariadb_connection = mariadb.connect(user='pps', password='pps', database='student')

cursor = mariadb_connection.cursor(buffered=True)
cursor.execute("select * from {0} where ID='{1}'".format(f_type,var))
passwd=cursor.fetchone()


if passwd == None:
		print '''<h3>No such file exits !!.<br>
			Enter valid file ID.</h3><br><br>'''
		print '<form action="index.html" method="post" >'
		print '<input id="f1" type="submit" value="Go Back"><br>'
		print '</form>'
else:
		
		print '<html>'
		print '<head>'
		print '<title>File Status</title>'
		print '''<meta name="viewport" content="width=device-width, initial-scale=1">
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<meta name="keywords" content="">
		<link href='//fonts.googleapis.com/css?family=Open+Sans:400,300,300italic,400italic,600,600italic,700,700italic,800,800italic' rel='stylesheet' type='text/css'>
		<link href="css/style.css" rel="stylesheet" type="text/css" media="all" />'''
		print '</head>'
		if f_type=="Medical":
			if passwd[1]=="1":
				c1="red";
			if passwd[2]=="1":
				c2="red";
			if passwd[3]=="1":
				c3="red";
			if passwd[4]=="1":
				c4="red";
				status="completed"
			print '<body>'
			print '''<div class="header">
				<h1>File Track</h1>
			</div>
                         
			<div class="content">
				<div class="content1">
					<h2>File ID: %s</h2>
				</div>
				<div class="content2">
		
					<div class="content2-header1">
						<p>Status : <span>%s</span></p>
					</div>
		
					<div class="clear"></div>
			</div>
			<div class="content3">
				<div class="shipment">
				
						<div class="process">
				   	 	<div class="imgcircle" style="background-color:%s;">
						<img src="images/admin.png" alt="process order">
				    	</div>
							<span class="line" style="background-color:aqua;"></span>
							<p>Processing Order</p>
						</div>
						<div class="quality">
							<div class="imgcircle" style="background-color:%s;">
						<img src="images/admin.png" alt="quality check">
				    	</div>
							<span class="line" style="background-color:aqua;"></span>
							<p>Quality Check</p>
						</div>
						<div class="dispatch">
							<div class="imgcircle" style="background-color:%s;">
						<img src="images/admin.png" alt="dispatch product">
				    	</div>
							<span class="line" style="background-color:aqua;"></span>
							<p>Dispatched Item</p>
						</div>
						<div class="delivery">
							<div class="imgcircle" style="background-color:%s;">
						<img src="images/admin.png" alt="delivery">
							</div>
							<p>Product Delivered</p>
						</div>
						<div class="clear"></div>
					</div>

			</div>'''%(var,status,c1,c2,c3,c4)
			print '<body>'
		elif f_type=="Leave_app":
			print 'hello'
		print '</html>'


