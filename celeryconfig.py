#Temporary, set up correctly
BROKER_HOST = “173.39.241.238” #IP address of the server B, which is running RabbitMQ and Celery
BROKER_PORT = 5672
BROKER_USER = “ubuntu” #username for RabbitMQ
BROKER_PASSWORD = “ubuntu” #password for RabbitMQ
BROKER_VHOST = “vhost_ubuntu” #host as configured on RabbitMQ server
CELERY_RESULT_BACKEND = "amqp"
CELERY_IMPORTS=("tasks”,)