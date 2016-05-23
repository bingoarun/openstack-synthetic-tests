from src.SynthCore import GlanceSynthTests
from src.OutputWriter import NagiosCode
from src.OutputWriter import passiveCheckWriter

image_id=None

def testImageCreate():
    try:
        global image_id
        image_id= GlanceSynthTests.imageCreate()
        status=NagiosCode.var0.value
        status_msg="Image successfully created"
    except:
        status=NagiosCode.var2.value
        status_msg="Some error in creating glance image"
    passiveCheckWriter('glance','glance_image_create',status,status_msg)

def testImageList():
    try:
        image_list=GlanceSynthTests.imageList()
        status = NagiosCode.var0.value
        status_msg = "Image successfully listed"
    except:
        status = NagiosCode.var2.value
        status_msg = "Some error in listing glance images"
    passiveCheckWriter('glance', 'glance_image_list', status, status_msg)



#Test runs
def runAllTests():
    testImageCreate()
    testImageList()

if __name__ == "__main__":
    runAllTests()