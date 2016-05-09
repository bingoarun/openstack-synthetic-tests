from OpenstackAuth import getClient

keystone=getClient('keystone')

#print keystone.token.get()