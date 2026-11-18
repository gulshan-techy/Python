import boto3

# AWS Region
region = "ap-south-1"

# Create S3 Client
s3_client = boto3.client(
    "s3",
    region_name=region
)

# Function 1: List All S3 Buckets
def list_buckets():

    response = s3_client.list_buckets()

    print("\nAvailable S3 Buckets:")

    if not response["Buckets"]:
        print("No buckets found.")

    else:
        for bucket in response["Buckets"]:
            print(bucket["Name"])

# Function 2: Create S3 Bucket
def create_bucket():

    bucket_name = input("Enter a unique bucket name: ")

    try:
        s3_client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                "LocationConstraint": region
            }
        )

        print("\nBucket created successfully!")

    except Exception as e:
        print("\nError:", e)

# Main Program
print("1. List S3 Buckets")
print("2. Create S3 Bucket")

choice = input("\nEnter your choice: ")

if choice == "1":
    list_buckets()

elif choice == "2":
    create_bucket()

else:
    print("Invalid choice!")
