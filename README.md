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
Terraform:  

Clone this repo on an box which has aws access to create a ec2 instances and read&write on s3. As a best practice an IAM role should be assigned to the box or use SAML api, Secret access keys should be used as last resort - not secure, just for testing

Init, plan and run:
terraform init

terraform plan -out "rv.output"

terraform apply "rv.output"

It should create an EC2 instance and a SG(inbound:22,80 - outbound all) which will be attached to the EC2 instance.After the instance will be created it will run the "userdata.sh" which will install Docker,Git and it will start a container based on docker hub repo(rv-docker)

Verify if "terraform.tfstate" has been uploaded in the s3 bucked specified earlier

###################################################################################################

Docker hub image horiacloud/rv-docker is an automated build image based on the git repo(https://github.com/horiacloud/rv-docker)

Container will pull the image from Docker hub and run the container at startup of the EC2 instance:    
BUILD Docker image: $ docker pull horiacloud/rv-docker  
RUN docker image: $ docker run -p 80:80 -it --rm --name rv horiacloud/rv-docker  

###################################################################################################

![alt text](https://github.com/horiacloud/rv/blob/master/screenshots/container2.jpg)
