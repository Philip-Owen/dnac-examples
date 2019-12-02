from dnacentersdk import api
from getpass import getpass

dnac = api.DNACenterAPI(base_url='ip-or-url:443',
                        username='',  # dnac username
                        password=getpass(),
                        verify=False  # bypass SSL verification
                        )

# Add device to DNAC
dnac_output = dnac.devices.add_device(cliTransport="ssh",  # ssh or telnet
                                      ipAddress=["ip(s)"],  # List of IP(s)
                                      userName="",  # cli username
                                      password="",  # cli password
                                      snmpVersion="v3",
                                      snmpUserName="",  # snmp v3 username
                                      snmpMode="AuthenticationandPrivacy",
                                      snmpAuthProtocol="sha",
                                      snmpAuthPassphrase="",  # snmp v3 auth pass
                                      snmpPrivProtocol="aes128",
                                      snmpPrivPassphrase="",  # snmp v3 priv pass
                                      snmpRetry=3,
                                      snmpTimeout=5,
                                      )

# Grab task ID from the add device process
taskId = dnac_output['response']['taskId']

# Get task ID information from DNAC
check_task = dnac.task.get_task_by_id(taskId)

# Check that task completed sucessfully
if check_task['response']['isError']:
    print(check_task['response']['failureReason'])
else:
    print('Device added to DNA Center.')
