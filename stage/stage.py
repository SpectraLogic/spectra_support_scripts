import click
from ds3 import ds3


@click.group()
def support():
    pass


@click.command()
def clear_suspect_blobs():
    print("Clearing all suspect blobs on tape")
    client = ds3.createClientFromEnv()
    blob_ids = suspect_blob_ids(client)

    buffer = []
    for blob_id in blob_ids:
        buffer.append(blob_id)
        if len(buffer) >= 1000:
            clear_blobs(client, buffer)
            buffer = []
    clear_blobs(client, buffer)


def clear_blobs(client, blob_list):
    response = client.clear_suspect_blob_tapes_spectra_s3(ds3.ClearSuspectBlobTapesSpectraS3Request(blob_list))
    if response.response.status_code != 200:
        print("Failed to send clear suspect blob command")
        exit(1)


def suspect_blob_ids(client):
    total_objects = 0
    page_size = 100
    response = client.get_suspect_blob_tapes_spectra_s3(ds3.GetSuspectBlobTapesSpectraS3Request(page_length=page_size))
    for blob in response.result['SuspectBlobTapeList']:
        total_objects += 1
        yield blob['BlobId']

    page_offset = 1
    while total_objects < response.paging_total_result_count:
        response = client.get_suspect_blob_tapes_spectra_s3(ds3.GetSuspectBlobTapesSpectraS3Request(page_length=page_size, page_offset=page_offset))
        for blob in response.result['SuspectBlobTapeList']:
            total_objects += 1
            yield blob['BlobId']


@click.command()
@click.argument('pool-name')
@click.argument('bucket-name')
def stage(pool_name, bucket_name):
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


support.add_command(clear_suspect_blobs)
support.add_command(stage)
