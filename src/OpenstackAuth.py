import ConfigParser
from keystoneauth1 import loading
from keystoneauth1 import session
from novaclient import client

Config = ConfigParser.ConfigParser()
config_path="../conf/config.ini"
Config.read(config_path)
version = Config.get('ApplicationSettings','VERSION')
auth_url = Config.get('ApplicationSettings','auth_url')
project_id = Config.get('ApplicationSettings','tenant_id')
username = Config.get('ApplicationSettings','username')
password = Config.get('ApplicationSettings','password')

def getClient():
    loader = loading.get_plugin_loader('password')
    auth = loader.load_from_options(auth_url=auth_url, username=username, password=password, project_id=project_id)
    sess = session.Session(auth=auth)
    myclient = client.Client(version, session=sess)
    return myclient
