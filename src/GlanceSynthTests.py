from OpenstackAuth import getClient
import urllib

glance = getClient('glance')

#http://docs.openstack.org/developer/python-glanceclient/apiv2.html#create
def imageCreate():
    url="http://download.cirros-cloud.net/0.3.3/cirros-0.3.3-x86_64-disk.img"
    sample_image=urllib.urlopen(url).read()
    image = glance.images.create(name="SynthtestImage1",is_public='False', disk_format='qcow2', container_format='bare')
    print image.status
    glance.images.upload(image.id, open('/home/arusekar/Downloads/sample.img', 'rb'))
    print image.status

    #glance.images.upload(image.id,open('/tmp/sample.img', 'rb'))


#print list(glance.images.list())[0:]

imageCreate()