import boto3
from botocore.client import Config

def upload_to_do(file_path):
    # Initialize DigitalOcean Spaces client
    session = boto3.session.Session()
    client = session.client('s3',
        region_name='fra1',  # Frankfurt region
        endpoint_url='https://fra1.digitaloceanspaces.com',
        aws_access_key_id='DO801BGYJ494939JV33C',
        aws_secret_access_key='T0JGJF+HMJQqV+PByCUI9FsrQviOuhznq7NdLO+27d8',
        config=Config(s3={'addressing_style': 'virtual'})
    )

    # Upload file
    try:
        client.upload_file(
            file_path,  # Local file path
            'testitems',  # Bucket name
            'applied.png',  # Object name in bucket
            ExtraArgs={'ACL': 'public-read'}  # Make file publicly accessible
        )
        print("Upload successful")
        return {
            "status": "success",
            "url": "https://testitems.fra1.digitaloceanspaces.com/applied.png",
        }
    except Exception as e:
        print(f"Upload failed: {str(e)}")
        return {
            "status": "error",
            "error": str(e)
        }
    

# upload_to_do('res/applied.png')