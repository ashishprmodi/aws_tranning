import boto3
ec2 = boto3.resource('ec2')

ec2.create_instances(ImageId='ami-0b898040803850657', MinCount=1, MaxCount=1)