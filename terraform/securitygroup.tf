resource "aws_security_group" "allow_ssh1" {
  name        = "allow-inbound-22-80-alloutbound"
  description = "Allow SSH inbound traffic"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags {
    CreatedBy   = "Terraform"
    Environment = "Dev"
    Name        = "RV EC2 SG"
    Purpose     = "SG for EC2 Instance"
  }
}
