import boto3
aws_resource = boto3.resource("s3")
bucket = aws_resource.Bucket("week14s3")
response = bucket.create(
    ACL = 'public-read' ,
    CreateBucketConfiguration = {
        'LocationConstraint':'us-east-1'
    }
)

print (response)