from openstack import connection
class tenant_create:
	def __init__(self):
		print "Class instantiated"

	def create_connection(auth_url,project,name,password):
		return connection.Connection(auth_url=auth_url,project=project,name=name,password=password)
		

obj = tenant_create()
conn = obj.create_connection("http://centospackstack:5000/v2.0","admin","admin","openstack")
print(conn)
#for image in conn.compute.images():
#	print(image.name)
