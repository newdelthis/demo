import json
import boto3
import csv
import io

s3 = boto3.client('s3')

def lambda_handler(event, context):

    # Get bucket and file name from event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Avoid infinite loop if Lambda reads its own output file
    if key == "total_sales.csv":
        return

    # Read uploaded CSV file
    response = s3.get_object(Bucket=bucket, Key=key)
    lines = response['Body'].read().decode('utf-8').splitlines()

    reader = csv.DictReader(lines)

    total_sales = 0

    for row in reader:
        total_sales += int(row['quantity']) * int(row['price'])

    print("Total Sales:", total_sales)

    # Create output CSV in memory
    output = io.StringIO()
    writer = csv.writer(output)

    writer.writerow(["Total_Sales"])
    writer.writerow([total_sales])

    # Upload result file to same bucket
    s3.put_object(
        Bucket=bucket,
        Key="total_sales.csv",
        Body=output.getvalue()
    )

    return {
        "statusCode": 200,
        "total_sales": total_sales
    }
