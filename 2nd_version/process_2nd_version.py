import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions
import os
from google.cloud import storage

if __name__ == "__main__":

  project = 'project-id'
    
    bucket_name = 'your-bucket'

    #the name of your JSON key file
    json_key_filename = 'key.json'

    #create a storage client
    storage_client = storage.Client(project=project)

    #download the JSON key file from the bucket
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(json_key_filename)
    local_json_key_path = '/tmp/' + json_key_filename
    blob.download_to_filename(local_json_key_path)

    #set the GOOGLE_APPLICATION_CREDENTIALS environment variable
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = local_json_key_path

    #add an input subscription id
    input_subscription = 'projects/project-id/subscriptions/Subscribe1'

    output_topic = 'projects/project-id/topics/Topic2'

    options = PipelineOptions()
    options.view_as(StandardOptions).streaming = True

    p = beam.Pipeline(options=options)

    output_file = 'gs://your-bucket/outputs/part'

    pubsub_data = (
        p
        | 'Read from pub sub' >> beam.io.ReadFromPubSub(subscription=input_subscription)
        | 'Write to pub sub' >> beam.io.WriteToPubSub(output_topic)
    )

    result = p.run()
    result.wait_until_finish()
