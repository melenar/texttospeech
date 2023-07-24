import json
import boto3 # To use the AWS API

def lambda_handler(event, context):
    
    sns_service = boto3.client('sns')
    
    topic_arn = "arn:aws:sns:us-east-1:754350794853:finalinternalteam"
    subject = "EC2 state change Notification"
    message = "Hello Sir,\nWe wanted to inform your ec2 instance has been terminated.\nThank you."
    
    # to publish the message
    sns_service.publish(
        TopicArn = topic_arn,
        Subject = subject,
        Message = message)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
