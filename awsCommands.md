# AWS commands for ec2 and s3
## Install aws-cli and kaggle-cli
```bash
sudo apt-get install aws-cli kaggle-cli
```
## AWS-cli
### Setup aws-cli config
```bash
aws config
```
Add your account id and security key
The ec2 instance should be located in the same location as the s3 bucket. If you already have a s3 bucket, then get the location from the link of you bucket.
Else set the location to where your ec2 is currently started. To improve file transfer speed the ec2 instance and s3 bucket should be in the same location.

As the standard output file format set json!
