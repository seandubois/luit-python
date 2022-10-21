import boto3
client=boto3.client("ec2")
response=client.delete_vpc(
    VpcId='vpc-0a56895082f8d5498'
)
print(response)