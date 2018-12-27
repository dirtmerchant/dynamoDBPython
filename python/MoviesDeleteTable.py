from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

table = dynamodb.Table('Movies')

table.delete()
