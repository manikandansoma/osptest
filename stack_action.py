from openstack import connection
class stack_action:
	def create_stack(self,conn):
		st = conn.orchestration.create_stack()
		st_file = open("/root/heat01.txt")

