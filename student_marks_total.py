import json
import boto3
import csv
from io import StringIO

s3 = boto3.client('s3')

def lambda_handler(event, context):
    
    # Get bucket and file name from event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    if key == "result.csv":
        return
    
    # Read file from S3
    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read().decode('utf-8')
    
    # Parse CSV
    csv_reader = csv.reader(StringIO(content))
    
    student_marks = {}
    
    for row in csv_reader:
        name, subject, marks = row
        marks = int(marks)
        
        if name not in student_marks:
            student_marks[name] = []
        
        student_marks[name].append(marks)
    
    # Prepare output CSV
    output = StringIO()
    writer = csv.writer(output)
    
    # Header
    writer.writerow(['Name', 'Total', 'Average'])
    
    # Calculate results
    for student, marks_list in student_marks.items():
        total = sum(marks_list)
        avg = round(total / len(marks_list), 2)
        writer.writerow([student, total, avg])
    
    # Save result.csv back to S3
    output_key = "result.csv"
    
    s3.put_object(
        Bucket=bucket,
        Key=output_key,
        Body=output.getvalue()
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Result file created successfully!')
    }