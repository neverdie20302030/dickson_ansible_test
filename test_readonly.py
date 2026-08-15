import routeros_api

connection = routeros_api.RouterOsApiPool(
    '192.168.100.19',   # replace with your CRS112 IP
    username='admin', # replace with your router username
    password='CCA@2024',
    port=8728,        # default API port
    plaintext_login=True
)

api = connection.get_api()
interfaces = api.get_resource('/interface').get()

for interface in interfaces:
    print(interface)

connection.disconnect()
