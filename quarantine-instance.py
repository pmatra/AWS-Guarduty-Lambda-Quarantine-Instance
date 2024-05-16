import boto3
from botocore.exceptions import ClientError
import os
 
def lambda_handler(event, context):
    response = 'Error isolating the instance.'
    try:
        # Set Variables
        instanceID = event['detail']['resource']['instanceDetails']['instanceId']
        security_group_id = os.environ['QUARANTINE_SG']
 
        # Get instance details
        ec2 = boto3.resource('ec2')
        instance = ec2.Instance(instanceID)
 
        # Change instance Security Group attribute
        instance.modify_attribute(Groups=[security_group_id])
        response = 'Incident auto-remediated'
 
    except ClientError as e:
        print(e)
    return response