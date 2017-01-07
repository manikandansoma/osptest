from openstack import connection
class tenant_action:
	def create_tenant(self,conn,name):
		return conn.identity.create_tenants(name)


	