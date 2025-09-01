provider "aws" {
  region = "us-east-1"
}

# Insecure: open security group
resource "aws_security_group" "allow_all" {
  name        = "allow_all_sg"
  description = "Open SG for demo"

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"] # 🔴 Checkov will flag this
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Insecure: S3 bucket without encryption
resource "aws_s3_bucket" "demo" {
  bucket = "demo-unencrypted-bucket-12345"
  acl    = "public-read" # 🔴 Also flagged by Checkov
}