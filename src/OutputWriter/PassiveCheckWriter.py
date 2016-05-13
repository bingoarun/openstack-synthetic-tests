import ConfigParser
import time
from enum import Enum

Config = ConfigParser.ConfigParser()
config_path = "../../conf/config.ini"
Config.read(config_path)

# Nagios output format - [<timestamp>] PROCESS_SERVICE_CHECK_RESULT;<host_name>;<svc_description>;<return_code>;<plugin_output>

class NagiosCode(Enum):
    var0='OK'
    var1='WARNING'
    var2='CRITICAL'
    var3='UNKNOWN'



def getFile(service):
    svc_file=Config.get('NagiosExternalCommandFile', service)
    try:
        myfile=open(svc_file,'a')
        return myfile
    except (OSError, IOError) as e:
        print e



def passiveCheckWriter(service,svc_desc, return_code, plugin_output):
    service_file=getFile(service)
    epoch_time=str(int(time.time()))
    nagios_hostname=service+"_synthetic_tests"
    nagios_txt="[%s] PROCESS_SERVICE_CHECK_RESULT;%s;%s;%s;%s" % (epoch_time,nagios_hostname,svc_desc,return_code,plugin_output)
    service_file.write(nagios_txt+"\n")
