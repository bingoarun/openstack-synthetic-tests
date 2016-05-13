from OpenstackAuth import getClient
import urllib
import ConfigParser
glance = getClient('glance')

#http://docs.openstack.org/developer/python-glanceclient/apiv2.html#create
def imageCreate(name="SynthTestImage",is_public='False', disk_format='qcow2', container_format='bare'):
    image = glance.images.create(name=name,is_public=is_public, disk_format=disk_format, container_format=container_format)
    Config = ConfigParser.ConfigParser()
    config_path = "../../conf/config.ini"
    Config.read(config_path)
    glance.images.upload(image.id, open(Config.get('Glance','image_location'), 'rb'))
    return image.id
    #glance.images.upload(image.id,open('/tmp/sample.img', 'rb'))

def imageList():
	return list(glance.images.list())[0:]

def imageGet(image_id):
    return glance.images.get(image_id)

