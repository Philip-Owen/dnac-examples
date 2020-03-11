import sys
from dnacentersdk import api
import urllib3
urllib3.disable_warnings()

"""
Used to inport devices into DNA Center using the network discovery API.

Takes an IP address and a hostname as arguments to pass in to the sdk
to create the post request.
"""

ip = sys.argv[1]
ipList = f"{ip}-{ip}"
hostname = sys.argv[2]

# Add credentials to dnasdk
dnac = api.DNACenterAPI(base_url='https://Your-IP-Here:443',
                        username='',
                        password='',
                        verify=False  # if needed
                        )

# Add device to DNAC
dnac_output = dnac.network_discovery.start_discovery(discoveryType="Range",
                                                     globalCredentialIdList=[
                                                        # Add global credential id's here
                                                     ],
                                                     preferredMgmtIPMethod="UseLoopBack",
                                                     protocolOrder="ssh",
                                                     retry=0,
                                                     timeout=5,
                                                     ipAddressList=ipList,
                                                     name=hostname
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
