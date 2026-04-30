provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "myec2" {
  ami           = "ami-0c02fb55956c7d316" # Amazon Linux 2 (example)
  instance_type = "t2.micro"
  key_name      = "your-existing-key-name"

  tags = {
    Name = "Terraform-EC2"
  }
}
