from openstack import connection
import httplib, urllib
class tenant_create:
	def __init__(self):
		print "Class instantiated"

	def create_connection(self,auth_url,project,name,password):
		return connection.Connection(auth_url=auth_url,project=project,name=name,password=password)

	def list_servers(self,conn):
<<<<<<< HEAD
    	print("List Servers:")

    	for server in conn.compute.servers():
=======
    	    print("List Servers:")
    	
    	    for server in conn.compute.servers():
>>>>>>> f70c16791e1fd11199f22dafc37a5ae13a1045a1
    		print(server)
	
obj = tenant_create()
con = obj.create_connection("http://centospackstack:5000/v2.0","tata","tata","Root@123")
obj.list_servers(con)
