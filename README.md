# HelloWorldFlask
A Hello World example of using Swagger, Connexion, and Flask to make a AWS Lambda function using a API first approach.

## Prerequisites:
You will need to install:
[Connexion](https://github.com/zalando/connexion)

## Setup:

First step is to clone the repository. Copy the link given by Clone with SSH and type:
```
git clone git@github.com:wongJonathan/HelloWorldFlask.git
```
into the terminal.

cd into the newly created folder. Inside should be:
* app.py
* requirements.txt
* serverless.yml
* swagger.yaml

Assuming AWS credentials are setup correctly running:
```
AWS_ACCOUNT=dev serverless deploy
```
in the terminal will deploy your app.py to the AWS server. The terminal will print out a link (example: https://g1hb5a5b98.execute-api.us-west-2.amazonaws.com/dev/). Copying it and pasting it into your address bar and adding hello/ (https://g1hb5a5b98.execute-api.us-west-2.amazonaws.com/dev/hello) will print out hello world on your screen.

To run locally run:
```
AWS_ACCOUNT=dev sls wsgi serve
```

