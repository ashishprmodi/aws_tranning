import boto3
ids = ['i-0b5762dd66e735b01']
ec2 = boto3.resource('ec2')
#ec2.instances.filter(InstanceIds = ids).stop() #for stopping an ec2 instance

ec2.instances.filter(InstanceIds = ids).terminate() #for terminating an ec2 instance