provider "aws" {
    region = "us-east-1"
    access_key = "AKIA5QA7AUXVCHYNB7GF"
    secret_key = "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" 
}

resource "aws_instance" "web" {
    ami           = "ami-0b5eea76982371e91"
    instance_type = "t2.micro"
    subnet_id = "subnet-0496c1b09ddd1bf1b"
    security_groups = ["sg-04dae266186375f62"]

    tags = {
      Name = "first_Instance"
    }

}
