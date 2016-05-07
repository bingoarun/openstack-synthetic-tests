from OpenstackAuth import getClient

nova = getClient()
print nova.flavors.list()
