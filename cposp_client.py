import os
import sys
import time
import logging
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
