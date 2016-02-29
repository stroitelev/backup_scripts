"""
----------------------------------------------------------------
A script to restore mysql databases through the mysql utility 
and receive backup file from AWS S3.

Program: Mysql Database Restore
Author: Pavel Stroitelev
Date: February 29, 2016
Revision: 1.0
----------------------------------------------------------------
"""

import os
import boto3
import datetime
import subprocess

# set the default values
db_host = 'localhost'
db_name = 'some_database'
db_user = 'some_user'
db_password = 'some_password'
backup_local_path = r'/var/local/backups/mysql/'
backup_file = db_name + '_' + datetime.datetime.now().strftime("%Y%m%d") + '.sql'
bucket_name = 'bucket-backups'
bucket_subdir = 'mysql/'

def main():
    # check and create local backup folder
    if not os.path.exists(backup_local_path):
        os.makedirs(backup_local_path)
    # use AWS S3
    s3 = boto3.resource('s3')
    # set bucket name
    bucket = s3.Bucket(bucket_name)
    # download backup file from S3
    bucket.download_file(bucket_subdir + backup_file, backup_local_path + backup_file)
    # restore database
    subprocess.call('mysql -u %s -p%s %s < %s%s' %(db_user, db_password, db_name, backup_local_path, backup_file), shell=True)
 
if __name__ == '__main__':
  main()