import sys
import os
import swiftclient.client

def main():
    client_config = os.environ
    config = {
                'user' : client_config['OS_USERNAME'],
                'key' : client_config['OS_PASSWORD'],
                'tenant_name' : client_config['OS_TENANT_NAME'],
                'authurl' : client_config['OS_AUTH_URL'],
            }
    conn = swiftclient.client.Connection(auth_version=2, **config)
    return [obj['name'] for obj in conn.get_account()[1]]



if __name__ == '__main__':
    sys.exit(main())
