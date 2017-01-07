#from openstack import connection
class main_action(connect,tenant_action,stack_action):
	def __init__(self,url,project,name,password):
        super(connect, self,self.url=url,self.project=project,self.name=name,self.password=password).__init__()

	obj = main_action(auth_url="http://centospackstack:5000/v2.0",project_name="tata",username="tata",password="Root@123")
	conn = obj.con()
	tenant = obj.create_tenant(conn,self.project)
	stack = obj.create_stack(conn)
