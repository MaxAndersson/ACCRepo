import os
import novaclient
from novaclient.client import Client
import time
import paramiko
from paramiko import SSHClient as client

class CPOSPServer(object):
    """Abstract Class"""

    NOVA_VERSION = '2'
    _client = None
    _config = None
    _server_config = None


    def __init__(self, name, context_commands, server_config):
        if(self._client == None):
            print 'Please run the CPOSPServer.factory(client_config=os.eviron) method first to configure the client'
            return None
        self._commands = context_commands
        self._server_config = server_config
    #    if(self._check_server_name(name) == False):
    #        print 'There is already an instance running with name: {}'.format(name)
    #        return None


        return self

    def boot(self):
        try:
            self._server = self._client.servers.create(**self._server_config)
        except Exception as e:
            raise Exception('Booting Problem: {}'.format(e))

        return True
    def _check_floating_ip_assignment(self,server):
        try:
            floating_ip = [ip for ip in self._client.floating_ips.list() if ip.instance_id == self._server.id ].pop().ip
            return floating_ip
        except:
            return None

    def _check_floating_ips_reuse(self):
        return [ip for ip in self._client.floating_ips.list() if ip.instance_id == None]

    def _get_floating_ip(self,pool):
            ip  = self._check_floating_ips_reuse()
            if ip != []:
                return ip.pop()
            else:
                ip = self._client.floating_ips.create(pool)
                return ip
    def _deploy_with_context():
        try:
            self._ssh = client()
            self._ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self._ssh.connect(ip,
                            username = 'ubuntu',
                            key_filename ='akey.pem')

        except Exception as e:
            raise e
        for command in commands:
        try:
            print 'EXECUTEING: {}'.format(command)
            (stdin,stdout,stderr) = ssh.exec_command(command)
            if(stderr != None):
                raise Exception(stderr)
                #print stdout.read()
                #print stderr.read()

        except Exception as e:
            print 'Something went wrong while executeing commands:'.format(e)


    def _attach_floating_ip(self, pool = 'ext-net'):
            while(self._server.status != 'ACTIVE'):
                print 'Server Not Active Yet, Retrying in {} secounds'.format(3)
                time.sleep()
            if(self._check_floating_ip_assignment(self._server) != None):
                raise Exception('Server already has an floating IP')
            ip = self._get_floating_ip(pool)
            try:
                self._server.add_floating_ip(ip.ip)
                return ip.ip

            except Exception as e:
                raise Exception("Failed to attach a floating IP to the controller.\n{0}".format(e))
            return ip.ip

    def _attach_security_group(self):
        return
    def get_client(self):
        return _client

    def _set_client(self,client):
        _client = client
    def _get_key_pair(self, name = 'CPOSP_key'):
        try:
            return self._client.keypairs.find(name = name)
        except:
            return self._client.keypairs.create(name)
    @classmethod
    def factory(cls,client_config = None):
        if client_config == None:
            client_config = os.environ
            cls._config = {
            'username' : client_config['OS_USERNAME'],
            'api_key' : client_config['OS_PASSWORD'],
            'project_id' : client_config['OS_TENANT_NAME'],
            'auth_url' : client_config['OS_AUTH_URL'],
            }
        else:
            cls._client = client_config
        try:
            cls._client = Client(cls.NOVA_VERSION, **cls._config)
            #print cls._client
            return True
        except Exception as e:
            print 'Client connection could not be established: {}'.format(e)
            return False


class CPOSPMaster(CPOSPServer):
    """docstring for CPOSPMaster """

    def __init__(self,name = 'CPOSPMaster',user = 'CPOSP',password= 'CPOSP', vHost = 'CPOSP'):
        self._server_config = self.get_server_config_defaults() ## or take user input from client

        super(CPOSPMaster,self).__init__(name,
        self.__get_context(user,password,vHost),
        self._server_config)
        self.__user = user
        self.__password = password
    def get_server_config_defaults(self):
        return {
    'name': 'CPOSPMaster',
    'key_name' : self._get_key_pair().name,
    'flavor' : self._client.flavors.find(name='m1.medium'),
    'image' :self._client.images.find(name='Ubuntu Server 14.04 LTS (Trusty Tahr)'),
    }

    def __get_context(self,user, password,vHost):
        return  [
                'sudo apt-get update -y',
                'sudo apt-get install rabbitmq-server -y',
                'sudo rabbitmqctl add_user {0} {1}'.format(user,password),
                'sudo rabbitmqctl add_vhost {0}'.format(vHost),
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
