from src.SynthCore import GlanceSynthTests

def testImageCreate():
    status_msg=None
    status=None
    try:
        image_id= GlanceSynthTests.imageCreate()
        status="SUCCESS"
        status_msg="Image successfully created"
    except:
        status="ERROR"
        status_msg="Some error in creating glance image"
    print status, status_msg

def testImageList():
    status_msg=None
    status=None
    try:
        image_list=GlanceSynthTests.imageList()
        status = "SUCCESS"
        status_msg = "Image list is successful"
    except:
        status = "ERROR"
        status_msg = "Some error in listing glance image"
    print status, status_msg


testImageCreate()
testImageList()