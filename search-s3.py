import boto3
resource = boto3.resource("s3")
bucket_list = list(resource.buckets.all())
print(len(bucket_list))

for bucket in resource.buckets.all():
    print(bucket.name)
