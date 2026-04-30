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

resource "aws_s3_bucket" "date_bucket" {
  bucket = "27-04-2026-atul"
}

# Added block to upload the file
resource "aws_s3_object" "file_upload" {
  bucket = aws_s3_bucket.date_bucket.id
  key    = "hello.txt"
  source = "hello.txt"
}
