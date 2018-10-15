# rv

###################################################################################################
Task:

Design and code a simple app that exposes the following HTTP based APIs

a)Saves/updates the given user's name and date of birth in the database:
Request: PUT /hello/John{"dateOfBirth":"2001-01-01"
Response: 204 No Content

b)Returns a hello/birthday message for given user:
Request: GET /hello/John
Response: 200 OK

-when John's birthday is in 5 days:
{"message": "Hello, John! Your birthday is in 5 days"}

-when John's birthday is today:
{"message": "Hello,John! Happy birthday!"}

###################################################################################################
Infrastructure diagram:

![alt text](https://github.com/horia-cloud/rv/blob/master/architecture/infrastructure%20diagram.jpg)

Note: the diagram describe the ideal case, when AWS Direct Connect is enabled on an account,
in order to simplify things(avoid using a bastion server for connecting on the private subnet) 
as DirectConnect is not available on my account - the terraform code will deploy the ec2 instance 
in the public subnet and ALB and Autoscaling group will not be created
###################################################################################################

Docker hub image horiacloud/rv-docker is an automated build image based on the git repo(https://github.com/horiacloud/rv-docker)

Container will pull the image from Docker hub and run the container at startup of the EC2 instance:    
BUILD Docker image: $ docker pull horiacloud/rv-docker  
RUN docker image: $ docker run -p 80:80 -it --rm --name rv horiacloud/rv-docker  

###################################################################################################
