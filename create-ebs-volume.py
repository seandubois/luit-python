import boto3
ec2_client = boto3.client("ec2")
ec2_clinet.create_volume(AvailabilityZone='us-east-2',
    Size=8,
    VolumeType='gp2',
    TagSpecifications=[
        {
            'ResourceType': 'volume',
            'Tags': [
                {
                    'Key': 'Name',
                    'value': 'Tutorial'
                },
            ]
        },
    ]
)