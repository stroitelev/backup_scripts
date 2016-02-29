# Small scripts for backup and restore mysql databases and storing backup files in AWS S3.

s3_mysql_backup.py - script for backup mysql databases and sending backup files to AWS S3 for storing them.
s3_mysql_restore.py - script for restore mysql database from backup file who is stored on AWS S3 bucket. 

For working need install Boto 3 and configure AMI access to AWS.

For install Boto 3 you can use pip:

 # pip install boto3

Configure access to AWS:

 # aws configure

AWS Access Key ID []: YOUR_ACCESS_KEY

AWS Secret Access Key []: YOUR_SECRET_KEY

Default region name []: YOUR_REGION

More info about Boto 3 and working with AWS you can find here:

https://boto3.readthedocs.org/en/latest/guide/quickstart.html

https://github.com/boto/boto3
