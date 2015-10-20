
sudo apt-get update -y
echo "127.0.0.1       localhost CPOSP CPOSP.local" | sudo tee --append /etc/hosts > /dev/null
sudo apt-get install rabbitmq-server -y
sudo rabbitmqctl add_user CPOSP CPOSP
sudo rabbitmqctl add_vhost CPOSP
sudo rabbitmqctl set_permissions -p CPOSP CPOSP ".*" ".*" ".*"'
