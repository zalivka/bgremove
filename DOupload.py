import boto3
from botocore.client import Config

def uploadDO(file_path, uploadTo):
    session = boto3.session.Session()
    client = session.client('s3',
        region_name=uploadTo.get('region_name'),  
        endpoint_url=uploadTo.get('endpoint_url'),
        aws_access_key_id=uploadTo.get('aws_access_key_id'),
        aws_secret_access_key=uploadTo.get('aws_secret_access_key'),
        config=Config(s3={'addressing_style': 'virtual'})
    )

    # Upload file
    try:
        region_name = uploadTo.get('region_name')
        bucket_name = uploadTo.get('bucket')
        object_name = uploadTo.get('object_name')
        client.upload_file(
            file_path,  # Local file path
            bucket_name,  # Bucket name
            object_name,  # Object name in bucket
            ExtraArgs={'ACL': 'public-read'}  # Make file publicly accessible
        )
        print("Upload successful")
        return {
            "status": "success",
            "url": f"https://{bucket_name}.{region_name}.digitaloceanspaces.com/{object_name}",
        }
    except Exception as e:
        print(f"Upload failed: {str(e)}")
        return {
            "status": "error",
            "error": str(e)
        }
    

# uploadTo = {'input': {'link': 'https://rmbg.fra1.digitaloceanspaces.com/20250305_013120_ac35f508.jpg'}, 
            
#             'uploadTo': {'region_name': 'fra1', 
#                          'endpoint_url': 'https://fra1.digitaloceanspaces.com', 
#                          'aws_access_key_id': 'DO00A68ZPATT2M7W6EJF', 
#                          'aws_secret_access_key': '368lcCHa3Xff7LtmN1+Y8tc9p+Pw/86FwpZ507qx2V8', 
#                          'bucket': 'rmbg', 
#                          'object_name': 'lel.jpg'}}


uploadTo = {'region_name': 'fra1', 
                         'endpoint_url': 'https://fra1.digitaloceanspaces.com', 
                         'aws_access_key_id': 'DO00A68ZPATT2M7W6EJF', 
                         'aws_secret_access_key': '368lcCHa3Xff7LtmN1+Y8tc9p+Pw/86FwpZ507qx2V8', 
                         'bucket': 'rmbg', 
                         'object_name': 'lel.jpg'}