import click
from ds3 import ds3


@click.command()
@click.argument('pool-name')
@click.argument('bucket-name')
def main(pool_name, bucket_name):
    print("Staging objects from pool {} to for bucket {}".format(pool_name, bucket_name))
    client = ds3.createClientFromEnv()

    blob_response = client.get_blobs_on_pool_spectra_s3(ds3.GetBlobsOnPoolSpectraS3Request(pool_name))

    ds3_objects = blob_response.result['ObjectList']

    object_names = [obj['Name'] for obj in ds3_objects if obj['Length'] != '0']

    print("Objects to stage {}".format(object_names))

    objects = [ds3.Ds3GetObject(obj) for obj in object_names]

    buffer = []

    for objName in objects:
        buffer.append(objName)

        if len(buffer) >= 100000:
            create_stage_job(buffer, client, bucket_name)
            buffer = []
    create_stage_job(buffer, client, bucket_name)


def create_stage_job(buffer, client, bucket_name):
    print("Emitting staging job")
    request = ds3.StageObjectsJobSpectraS3Request(bucket_name, buffer)
    stage_job_response = client.stage_objects_job_spectra_s3(request)
    print("Stage job {} created".format(stage_job_response['JobId']))
