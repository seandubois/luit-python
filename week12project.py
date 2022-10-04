services = []
services.append("dynamoDB")
services.append("ec2")
services.append("vpc")
services.append("s3")
print(services)

print("length of list:", len(services))

services2 = services[:]
services2.remove("vpc")
services2.pop(1)
print(services2)

print("length of list:", len(services2))

print("done")