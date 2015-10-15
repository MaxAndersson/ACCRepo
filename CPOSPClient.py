import os
import sys
import time
import logging
#from novaclient import client as novaclient
#from collections import OrderedDict
#import collections
#import installSoftware

#OPTION 1
# Option for CLI interface that i look into: http://docs.openstack.org/developer/cliff/introduction.html
#http://docs.openstack.org/developer/cliff/classes.html#cliff.app.App
#sudo pip install cliff
#https://github.com/kennethreitz/clint
#Far det icke att fungera.. kollar mer senare.

#OPTION 2
#http://click.pocoo.org/5/

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

#Easywayout.
from sys import argv

def get_config_values():
    prompt = '> '
    #####  -------  CONFIG --------- #####

    print "CONFIG setup"
    # user
    print "What is your username?" 
    user = raw_input(prompt)

    #USERNAME
    print "What is your key?" 
    key = raw_input(prompt)

    #PASSWORD
    print "What is your tenant_name?" 
    tenant_name = raw_input(prompt)

    #TENANT_NAME
    print "What is your authurl?" 
    authurl = raw_input(prompt)

    config_dict = {"username" : user, "api_key": key, "project_id": tenant_name, "auth_url": authurl}



    print """
    user: %r 
    key %r 
    auth_url: %r 
    authurl %r 
    """ % (user, key, tenant_name, authurl)

    print config_dict

    #####  -------  SERVER CONFIG --------- #####

    print "IMAGE config setup"
    # Image
    print "What image do you want to use? Suggested: [Ubuntu Server 14.04 LTS (Trusty Tahr)]" 
    image = raw_input(prompt)

    # flavor
    print "What flavor do you want to use? Suggested: [m1.medium]" 
    flavor = raw_input(prompt)

    # network
    print "What network do you want to use? Suggested: [ACC-Course-net]" 
    network = raw_input(prompt)

    # Image
    print "What keypair do you want to use?" 
    keypair = raw_input(prompt)

    server_config_dict = {"image" : image, "flavor": flavor, "network": network, "key_name": keypair}



    print """
    image: %r 
    flavor %r 
    network: %r 
    keypair %r 
    """ % (image, flavor, network, keypair)

    print server_config_dict


    #####  -------  SLAVE CONFIG --------- #####

    print "Slave config setup"
    # Image
    print "What image do you want to use for your slave setup? Suggested:[Ubuntu Server 14.04 LTS (Trusty Tahr)]" 
    image = raw_input(prompt)

    # flavor
    print "What flavor do you want to use for your slave setup? Suggested: [m1.medium]" 
    flavor = raw_input(prompt)

    # network
    print "What network do you want to use? Suggested: [ACC-Course-net]" 
    network = raw_input(prompt)

    # Image
    print "What keypair do you want to use?" 
    keypair = raw_input(prompt)

    # Amount of slaves that you wish to spawn
    print "How many slaves do you want to setup for processing your data?" 
    slave_amount = raw_input(prompt)


    slave_config_dict = {"image" : image, "flavor": flavor, "network": network, "key_name": keypair, "slave_amount": slave_amount}



    print """
    image: %r 
    flavor %r 
    network: %r 
    keypair %r 
    slave_amount %r
    """ % (image, flavor, network, keypair, slave_amount)

    print slave_config_dict


# POTENTIALLY skip all the Client setup and run it more purely as a service

    
    #####  -------  PIPE CONFIG --------- #####
    # What kind of
    print "How many slaves do you want to setup for processing your data?" 
    slave_amount = raw_input(prompt)            # We might wanna overrule this? Maybe 1 worker for 20 and 5 for 1000 or something...


    print "What is the path to your files?" 
    all_cellprofiler_files = raw_input(prompt)

    slave_config_dict = {"slave_amount" : slave_amount, "all_cellprofiler_files": all_cellprofiler_files}


#return server_config_dict, slave_config_dict, config_dict, slave_config_dict



if __name__ == '__main__':
    get_config_values()


