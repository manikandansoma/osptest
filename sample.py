from openstack import connection
conn = connection.Connection(auth_url="http://10.144.243.143:5000/v2.0",
                             project_name="admin",
                             username="admin",
                             password="openstack")
for project in conn.identity.projects():
   print(project.name)