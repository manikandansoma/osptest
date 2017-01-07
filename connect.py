from openstack import connection
class connect:
	def __init__(self,url,project,name,password):
		self.url=url
		self.project=project
		self.name=name
		self.password=password

	def con(self):
		return connection.Connection(self.url,self.project,self.name.self.password)

	

	 

