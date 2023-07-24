#!/usr/bin/python3

import cgi
import boto3

print("content-type: text/html")
print()
x = cgi.FieldStorage("t")
text = x.getvalue("t")
service = boto3.client("polly")
service2 = boto3.client("s3")
response2=service.start_speech_synthesis_task(
    OutputFormat="mp3",
    OutputS3BucketName="outputaftertextuploadfrompolly",
    Text="File ~anaconda3\lib\site-packagesbotocore\client.py:530, in ClientCreator._create_api_method.<locals>._api_call(self, *args, **kwargs)",
    VoiceId="Joanna"
)

task=response2['SynthesisTask']['TaskId']
while True :
    response2=service.get_speech_synthesis_task(
        TaskId=task
    )
    if not (response2['SynthesisTask']['TaskStatus'] == "scheduled") :
        break
task=task+".mp3"
theobject=service2.get_object(Bucket="outputaftertextuploadfrompolly", Key=task)
location = service2.get_bucket_location(Bucket="outputaftertextuploadfrompolly")['LocationConstraint']
url="https://%s.s3.amazonaws.com/%s/%s" % (location, "outputaftertextuploadfrompolly", task)


print("Click on the below link to listen to the generated audio\n" + url)