import boto3
s3_resource=boto3.client("s3")
objects = s3 resource.list_objects(Bucket = "week14s3"["contents"])
print(len(objects))
if len(objects)>0:
    print("objects exsits")
for object in objects:
    print(object(key))