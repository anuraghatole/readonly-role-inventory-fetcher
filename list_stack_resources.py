import boto3

# Ask the user to enter the name of the CloudFormation stack
stack_name = input("Enter your CloudFormation Stack Name: ")

# Create a CloudFormation client using default credentials (like instance role)
cf = boto3.client('cloudformation')

try:
    # Try to get the list of resources created by the given stack
    response = cf.describe_stack_resources(StackName=stack_name)
    resources = response['StackResources']
except Exception as e:
    # If something goes wrong (like wrong name), show the error and stop the script
    print("Error getting stack details:", e)
    exit()

# Print details of each resource found in the stack
for resource in resources:
    print("\nResource Type:", resource['ResourceType'])               # Type of the resource (like EC2, S3, etc.)
    print("Logical ID:", resource['LogicalResourceId'])              # Logical ID used in CloudFormation template
    print("Physical ID:", resource['PhysicalResourceId'])            # Actual resource ID in AWS (like instance ID)
