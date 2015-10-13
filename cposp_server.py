import os
from novaclient.client import Client
from enum import Enum


class CPOSPServer:
    """docstring for CPOSServer"""

    NOVA_VERSION = '2'
    _client = None
    _config = None
    def __init__(self, name, context_commands, server_config):
        if(self._client == None):
            print 'Please run the CPOSPServer.factory(client_config=os.eviron) method first to configure the client'
            return None
        if(_check_server_name(name) == False):
            print 'There is already an instance running with name: {}'.format(name)
            return None
        if(_validate_config(server_config) == False):
            print ''
            # Boot secquence
            # attach ip

        return self
    @classmethod
    def _validate_config(sever_config):


    def __boot(self,sever_config):

        return

    def _attach_floating_ip(self):
        return
    def get_client():
        return _client

    def _set_client(client):
        _client = client

    @classmethod
    def factory(cls,client_config = os.environ):
        cls._config = {
        'username' : client_config['OS_USERNAME'],
        'api_key' : client_config['OS_PASSWORD'],
        'proejct_id' : client_config['OS_TENANT_NAME'],
        'auth_url' : client_config['OS_AUTH_URL'],
        }
        try:
            cls._client = Client(cls.NOVA_VERSION, **cls._config)
            print cls._client
            return True
        except Exception as e:
            print 'Client connection could not be established: {}'.format(e)
            return False

    @classmethod
    def _check_server_name(name):
        try:
             if(self._client.servers.find(name=name) == None):
                 return True
             else:
                 return False
        except Exception as e:
            raise Exception('Something went wrong while checking for server name avalability')


class CPOSPMaster(CPOSPServer):
    """docstring for CPOSPMaster """

    def __init__(self,name,user = 'CPOSP',password= 'CPOSP', vHost = 'CPOSP'):
        super(self).__init__(name,__get_context(user,password,vHost))
        self.__user = user
        self.__password = password


    def __get_context(user, password,vHost):
        return  [
                'sudo apt-get update -y',
                'sudo apt-get install rabbitmq-server -y',
                'sudo rabbitmqctl add_user {0} {1}'.format(user,password),
                'sudo rabbitmqctl add_vhost {0}'.format(vHost)
                'sudo rabbitmqctl set_permissions -p {0} {1} ".*" ".*" ".*"'.format(vHost,user)
               ]

class CPOSPSlave(CPOSPServer):
    """docstring for CPOSPSlave """

    def __init__(self,name):
        super(self).__init__(name)

    def __get_context(user):
        return  [
                'sudo apt-get update -y',
                'sudo apt-get install python-pip -y',
                'sudo apt-get install rabbitmq-server -y',
                'sudo pip install celery',
                #'celery worker -A tasks',
               ]
