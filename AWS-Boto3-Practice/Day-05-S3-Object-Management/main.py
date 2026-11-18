import boto3
import os

# AWS Configuration
region = "ap-south-1"

# Create S3 Client
s3_client = boto3.client(
    "s3",
    region_name=region
)

# Function 1: Upload File to S3
def upload_file():

    bucket_name = input("Enter S3 bucket name: ")

    file_path = input("Enter local file path: ")

    s3_file_name = input("Enter S3 object key: ")

    if not os.path.isfile(file_path):
        print("Error: Local file does not exist!")
        return

    try:
        s3_client.upload_file(
            file_path,
            bucket_name,
            s3_file_name
        )

        print("\nFile uploaded successfully!")

    except Exception as e:
        print("\nUpload Error:", e)


# Function 2: Download File from S3
def download_file():

    bucket_name = input("Enter S3 bucket name: ")

    s3_file_name = input("Enter S3 object key: ")

    download_path = input("Enter local download path: ")

    try:
        s3_client.download_file(
            bucket_name,
            s3_file_name,
            download_path
        )

        print("\nFile downloaded successfully!")

    except Exception as e:
        print("\nDownload Error:", e)


# Function 3: List Objects in S3 Bucket
def list_objects():

    bucket_name = input("Enter S3 bucket name: ")

    try:
        response = s3_client.list_objects_v2(
            Bucket=bucket_name
        )

        print("\nFiles available in S3 bucket:")

        if "Contents" in response:

            for obj in response["Contents"]:
                print(obj["Key"])

        else:
            print("Bucket is empty!")

    except Exception as e:
        print("\nError:", e)


# Main Menu
print("\n===== S3 OBJECT MANAGEMENT =====")

print("1. Upload File")
print("2. Download File")
print("3. List Objects")

choice = input("\nEnter your choice: ")

if choice == "1":
    upload_file()

elif choice == "2":
    download_file()

elif choice == "3":
    list_objects()

else:
    print("Invalid choice!")
