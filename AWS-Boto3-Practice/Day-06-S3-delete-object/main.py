import boto3

# AWS Region
region = "ap-south-1"

# Create S3 Client
s3_client = boto3.client(
    "s3",
    region_name=region
)


# Function: Delete S3 Object
def delete_object():

    bucket_name = input("Enter S3 bucket name: ")

    object_key = input("Enter S3 object key: ")

    confirmation = input(
        f"Are you sure you want to delete {object_key}? (yes/no): "
    )

    if confirmation.lower() == "yes":

        try:
            s3_client.delete_object(
                Bucket=bucket_name,
                Key=object_key
            )

            print("\nDelete request completed successfully!")

        except Exception as e:
            print("\nError:", e)

    else:
        print("\nDeletion cancelled!")


# Main Program
print("===== S3 OBJECT DELETION =====")

delete_object()
