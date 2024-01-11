from scratchclient import ScratchSession

session = ScratchSession("GoChipStudios", "sgh123Go_chip!") #enter account's credentials


connection = session.create_cloud_connection(948038834)
connection.set_cloud_variable("Hi", "16") #To set a cloud variable
#connection.get_cloud_variable("VARIABLENAMEHERE") #To get a cloud variable
