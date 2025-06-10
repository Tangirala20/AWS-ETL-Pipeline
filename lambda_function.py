import boto3
import pandas as pd
import io 

s3_buck = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    obj = s3_buck.get_object(Bucket=bucket, Key=key)
    df = pd.read_csv(io.BytesIO(obj['Body'].read()))

    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    df['sex'] = df['sex'].apply(lambda x: 0 if x.lower() == 'male' else 1)
    
    opt = io.StringIO()
    df.to_csv(opt, index=False, header=False)
    opt.seek(0)
    
    bio = io.BytesIO(opt.getvalue().encode('utf-8'))
    
    s3_buck.upload_fileobj(bio, Bucket=bucket, Key='processed-output.csv')
    print("Input Bucket: ", bucket)
