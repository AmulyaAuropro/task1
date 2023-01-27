provider "aws" {
    region = "us-east-1"
    access_key = "AKIAQBOKRNRFG62GQ43S"
    secret_key = "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" 
}

resource "aws_instance" "web" {
    ami           = "ami-0aa7d40eeae50c9a9"
    instance_type = "t2.micro"
    subnet_id = "subnet-073aa277934df7bf9"
    security_groups = ["sg-0547cad79f183323c"]

    tags = {
      Name = "first_Instance"
    }

}
