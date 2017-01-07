from openstack import connection
class tenant_create:
	def __init__(self,url,project,name,password):
		self.auth_url=url
		self.project=project
		self.name=name
		self.password=password

	def cont(self):
		return connection.Connection(self.auth_url,self.project,self.name,self.password)

obj = tenant_create("http://centospackstack:5000/v2.0","admin","admin","openstack")			
conn = obj.cont()
for image in conn.compute.images():
	print(image.name)
