import boto3
ec2_resource = boto3.resource("ec2")
ec2_resource.create_instances(ImageId = 'ami-089a545a9ed9893b6',
    InstanceType = 't2.micro',
    MaxCount = 1,
    MinCount = 1)