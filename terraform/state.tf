terraform {
  backend "s3" {
    bucket = "rv-state-file"
    key    = "terraform.tfstate"
    region = "eu-west-1"
  }
}
