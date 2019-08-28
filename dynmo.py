import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Delete Table
table = dynamodb.Table('users')

table.delete()