import json
import boto3

def send_email(email_ids, msg_body):
    ses = boto3.client('ses')

    subject = 'Message from XY'
    sender = 'shubhmanav2@gmail.com'
    print(msg_body)
    
    for email_id in email_ids:
        response = ses.send_email(
            Source=sender,
            Destination={'ToAddresses': [email_id]},
            Message={
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': msg_body}}    }   )

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    s3_bucket = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']

    response = s3.get_object(Bucket=s3_bucket, Key=file_name)
    msg_body = response['Body'].read().decode('utf-8')

    response = s3.get_object(Bucket='mailinglistforfinalproject', Key='mailer.txt')
    email_ids = response['Body'].read().decode('utf-8').splitlines()

    send_email(email_ids, msg_body)

    return {
        'statusCode': 200,
        'body': json.dumps('Done with Lambda!')
    }