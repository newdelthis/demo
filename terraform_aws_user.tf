terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}

resource "aws_iam_user" "cdac_user" {
  name = "cdac"
}

resource "aws_iam_access_key" "cdac_key" {
  user  = aws_iam_user.cdac_user.name
}
