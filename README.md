# Readonly Role Inventory Fetcher

This project automates the process of creating an AWS CloudFormation stack that generates a read-only IAM role with permissions to access EC2, S3, and other AWS resources. It then uses a Python script to fetch and display the inventory of resources created by that stack.

## 🛠️ How it works

1. **CloudFormation Template**: 
   - Creates an IAM role with the `ReadOnlyAccess` policy.
   - The role can be assumed by AWS services like EC2.

2. **Python Script**: 
   - Takes the CloudFormation stack name as input.
   - Connects to AWS and fetches details of resources created by the stack (e.g., EC2 instances, S3 buckets).

## ⚙️ How to Use

1. **Deploy the CloudFormation Template**:
   - Upload the CloudFormation YAML file (`readonly-role-template.yaml`) to the AWS Console or use the provided stack link below to create the stack.
   - [Click here to launch the CloudFormation stack](https://ap-south-1.console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/quickcreate?templateURL=https://cf-template-0101.s3.ap-south-1.amazonaws.com/readonly-role.yaml)

2. **Run the Python Script**:
   - Ensure your environment has the necessary IAM permissions (e.g., an EC2 instance with the right role).
   - Run the `list_stack_resources.py` script.
   - Enter the CloudFormation stack name when prompted.
   - The script will display the resources created by the stack.

## 📝 Requirements

- Python 3.x
- `boto3` library (install with `pip install boto3`)
- AWS credentials (default IAM role or instance profile)

## 📂 Files

- `readonly-role-template.yaml`: CloudFormation template to create a read-only IAM role.
- `list_stack_resources.py`: Python script to fetch resources created by the stack.

---
