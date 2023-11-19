import os
import time
from google.cloud import pubsub_v1
from google.cloud import storage

if __name__ == "__main__":
    
    project = 'project-id'

    #pubsub topic
    pubsub_topic = 'projects/project-id/topics/Topic1'

    #the name of your Google Cloud Storage bucket
    bucket_name = 'your-bucket'

    #the name of your JSON key file
    json_key_filename = 'key.json'

    #create a storage client
    storage_client = storage.Client()

    #download the JSON key file from the bucket
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(json_key_filename)
    local_json_key_path = '/tmp/' + json_key_filename
    blob.download_to_filename(local_json_key_path)

    #set the GOOGLE_APPLICATION_CREDENTIALS environment variable
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = local_json_key_path

    #create publisher
    publisher = pubsub_v1.PublisherClient()

    #read the CSV file from the bucket
    file_path = 'gs://{}/counts.csv'.format(bucket_name)
    file_data = storage_client.bucket(bucket_name).blob('counts.csv').download_as_text()

    #split the file data into lines
    lines = file_data.split('\n')

    #skip header
    header = lines[0]
    lines = lines[1:]

    #loop over each record
    for line in lines:
        event_data = line.strip()  #remove trailing newline character
        print('Publishing {0} to {1}'.format(event_data, pubsub_topic))

        #publish the message to the pub/sub topic
        publisher.publish(pubsub_topic, event_data.encode('utf-8'))

        time.sleep(1)

    #delete the downloaded JSON key file
    os.remove(local_json_key_path)
