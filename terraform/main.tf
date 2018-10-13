
resource "aws_instance" "my-test-instance" {
  ami           = "${data.aws_ami.amazonami.id}"
  instance_type = "${var.ec2_instance_type}"
  key_name      = "${var.ec2_key_name}"
  user_data     = "${file("userdata.sh")}"

  tags {
    Name = "RV"
  }

  security_groups = [
    "${aws_security_group.allow_ssh1.name}",
  ]

  lifecycle {
    ignore_changes = ["user_data"]
  }
}
