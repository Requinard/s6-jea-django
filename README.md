# Kwetter DJANGO

## How to run

you'll need the following

- A docker swarm
- Access to the manager node

Make sure you are working on a manager node (use `docker-machine env {machine}`) and run the  following command

`docker stack deploy -c docker-compose.yml kwetter`

This starts the application, database and message queues. Next up you'll need to apply migrations. We do this by entering an app in the swarm.

`docker exec -ti kwetter_app.1.$(docker service ps -f 'name=kwetter_app.1' kwetter_app -q --no-trunc | head -n1) /bin/bash`

This drops you in a shell. Run the following commands:

`python manage.py makemigrations`
`python manage.py migrate`

Now your database has the correct schemas! On to message queues!

To get message queue clusters running properly, you'll need to connect them to the cluster first.

run `docker exec -ti kwetter_queue-disc1.1.$(docker service ps -f 'name=kwetter_queue-disc1.1' kwetter_queue-disc1 -q --no-trunc | head -n1) /bin/bash`

and run

```sh
rabbitmqctl stop_app
rabbitmqctl join_cluster rabbit@stats
rabbitmqctl start_app
```

and now for the ram queue.

run `docker exec -ti kwetter_queue-ram1.1.$(docker service ps -f 'name=kwetter_queue-ram1.1' kwetter_queue-ram1 -q --no-trunc | head -n1) /bin/bash`


```sh
rabbitmqctl stop_app
rabbitmqctl join_cluster rabbit@stats
rabbitmqctl start_app
```

Now navigate to `{swarm ip}:15672`. Under nodes there should be three items. Message clustering is now done

Access the application through: `{swarm ip}:8000`