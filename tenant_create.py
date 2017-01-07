from openstack import connection
class tenantCreate:
	def __init__(self,url,project,name,password):
		self.auth_url=url
		self.project=project
		self.name=name
		self.password=password

	def con(self):
		return connection.Connection(self.auth_url,self.project,self.name,self.password)

	obj = tenantCreate(auth_url="http://centospackstack:5000/v2.0",project_name="admin",username="admin",password="openstack")			
	conn = obj.con()
	for user in conn.identity.list_users():
		print(user)
