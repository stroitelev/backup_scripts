"""
-----------------------------------------------------------------
A script to backup mysql databases through the mysqldump utility 
and send to AWS S3 for storing.

Program: Mysql Database Backup
Author: Pavel Stroitelev
Date: February 29, 2016
Revision: 1.0
-----------------------------------------------------------------
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

def mysql_db_list():
    db_list = subprocess.check_output("mysql -h %s -u %s -p%s -s -N -e 'show databases'" %(db_host, db_user, db_password), shell=True)
    db_list = db_list.strip().split('\n')
    return db_list

def mysql_db_backup(db_list):
    for database in db_list:
        if database == 'information_schema':
            continue
        if database == 'performance_schema':
            continue
        print(database)
        subprocess.call('mysqldump -h %s -u %s -p%s %s > %s%s' %(db_host, db_user, db_password, database, backup_local_path, backup_file), shell=True)

def main():
    # check and create local backup folder
    if not os.path.exists(backup_local_path):
        os.makedirs(backup_local_path)
    # get databases list
    db_list = mysql_db_list()
    # create backups
    mysql_db_backup(db_list)
    # use AWS S3
    s3 = boto3.resource('s3')
    # check and create bucket for backup
    try:
        bucket = s3.create_bucket(Bucket=bucket_name)
    except:
        bucket = s3.Bucket(bucket_name)
    # upload backup files to S3
    bucket.upload_file(backup_local_path + backup_file, bucket_subdir + backup_file)
 
if __name__ == '__main__':
  main()