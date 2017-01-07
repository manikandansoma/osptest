from openstack import connection
class stack_action:
	def create_stack(self,conn,name):
		st = conn.orchestration.create_stack(name)
		st_file = open("/root/heat01.txt")

