from openstack import connection
import httplib, urllib
class tenant_create:
	def __init__(self):
		print "Class instantiated"

	def create_connection(self,auth_url,project,name,password):
		return connection.Connection(auth_url=auth_url,project=project,name=name,password=password)
		

obj = tenant_create()
conn = obj.create_connection("http://centospackstack:5000/v2.0","tata","tata","Root@123")
try:
	print conn.compute.list_images()
except Exception: 
  pass
