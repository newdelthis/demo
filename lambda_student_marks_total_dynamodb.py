import json
import boto3
import csv
from decimal import Decimal   

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('StudentResults')

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    response = s3.get_object(Bucket=bucket, Key=key)
    lines = response['Body'].read().decode('utf-8').splitlines()

    reader = csv.reader(lines)

    student_marks = {}

    # Read input
    for row in reader:
        student, subject, marks = row
        marks = int(marks)

        if student not in student_marks:
            student_marks[student] = []

        student_marks[student].append(marks)

    # Write ONLY 3 attributes to DynamoDB
    for student, marks_list in student_marks.items():
        total = sum(marks_list)
        average = total / len(marks_list)   

        table.put_item(
            Item={
                'student': student,
                'total': Decimal(str(total)),        
                'average': Decimal(str(average))    
            }
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Stored with 3 columns: student, total, average')
    }