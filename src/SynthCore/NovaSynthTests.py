
from OpenstackAuth import getClient

nova=getClient('nova')

print nova.flavors.list()



