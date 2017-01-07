from openstack import connection
conn = connection.Connection(auth_url="http://centospackstack:5000/v2.0",
                             project_name="tata",
                             username="tata",
                             password="Root@123")
for image in conn.compute.images():
   print(image)