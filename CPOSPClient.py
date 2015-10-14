import os
import sys
import time
import logging
from novaclient import client as novaclient
from collections import OrderedDict
import collections
import installSoftware


# Option for CLI interface that i look into: http://docs.openstack.org/developer/cliff/introduction.html
#http://docs.openstack.org/developer/cliff/classes.html#cliff.app.App




#Check username etc.
#Authenticate
# Username, Tenant_name, project_name, 
# Nr. Workers
#Return dict




#From MOLNS possible to use?
'''
##########################################
class OpenStackBase(ProviderBase):
    """ Abstract class for OpenStack. """
    
    SSH_KEY_EXTENSION = ".pem"
    PROVIDER_TYPE = 'OpenStack'

def OpenStackProvider_default_key_name():
    user = os.environ.get('USER') or 'USER'
    return "{0}_molns_sshkey_{1}".format(user, hex(int(time.time())).replace('0x',''))
##########################################



class OpenStackProvider(OpenStackBase):
    """ Provider handle for an open stack service. """

    OBJ_NAME = 'OpenStackProvider'
    
    MAX_IMAGE_CREATION_WAITTIME = 1800


    CONFIG_VARS = OrderedDict(
        [
        ('nova_username',
            {'q':'OpenStack username', 'default':os.environ.get('OS_USERNAME'), 'ask':True}),
        ('nova_password',
            {'q':'OpenStack password', 'default':os.environ.get('OS_PASSWORD'), 'ask':True, 'obfuscate':True}),
        ('nova_auth_url',
            {'q':'OpenStack auth_url', 'default':os.environ.get('OS_AUTH_URL'), 'ask':True}),
        ('nova_project_id',
            {'q':'OpenStack project_name', 'default':os.environ.get('OS_TENANT_NAME'), 'ask':True}),
        ('neutron_nic',
            {'q':'Network ID (leave empty if only one possible network)', 'default':None, 'ask':True}),    
        ('floating_ip_pool',
            {'q':'Name of Floating IP Pool (leave empty if only one possible pool)', 'default':None, 'ask':True}),
        ('nova_version',
            {'q':'Enter the version of the OpenStack NOVA API', 'default':"2", 'ask':True}),
        ('key_name',
            {'q':'OpenStack Key Pair name', 'default':OpenStackProvider_default_key_name(), 'ask':True}),
        ('group_name',
            {'q':'OpenStack Security Group name', 'default':'molns', 'ask':True}),
        ('ubuntu_image_name',
            {'q':'ID of the base Ubuntu image to use', 'default':None, 'ask':True}),
        ('molns_image_name',
            {'q':'ID of the MOLNs image (leave empty for none)', 'default':None, 'ask':True}),
        ('default_instance_type',
            {'q':'Default Instance Type (Flavor)', 'default':None, 'ask':True}),
        ('login_username',
            {'default':'ubuntu', 'ask':False})
        ])

 def get_config_credentials(self):
        """ Return a dict with the credentials necessary for authentication. """
        return {
            'user' : self.config['nova_username'],
            'key' : self.config['nova_password'],
            'tenant_name' : self.config['nova_project_id'],
            'authurl' : self.config['nova_auth_url']
            }

'''


