import click
from ds3 import ds3


@click.command()
@click.argument('pool-name')
@click.argument('bucket-name')
def main(pool_name, bucket_name):
    print("Staging objects from pool {} to for bucket {}".format(pool_name, bucket_name))
    client = ds3.createClientFromEnv()

    blob_response = client.get_blobs_on_pool_spectra_s3(ds3.GetBlobsOnPoolSpectraS3Request(pool_name))

    objects = [obj['Name'] for obj in blob_response.result['Objectist']
               if obj['InCache'] == 'false'
               and obj['Bucket'] == bucket_name]

    buffer = []

    for objName in objects:
        buffer.append(objName)

        if len(buffer) >= 100000:
            print("Emitting staging job with ")
            request = ds3.StageObjectsJobSpectraS3Request(bucket_name, buffer)
            stage_job_response = client.stage_objects_job_spectra_s3(request)
            buffer = []
            print("Stage job {} created".format(stage_job_response['JobId']))
