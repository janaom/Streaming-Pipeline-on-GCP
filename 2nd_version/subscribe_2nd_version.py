from google.cloud import pubsub_v1
import time
import os
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

    
    #subscription id
    subscription_path = "projects/project-id/subscriptions/Subscribe2"
    
    subscriber = pubsub_v1.SubscriberClient()
 
    def callback(message):
        print(('Received message: {}'.format(message)))    
        message.ack()

    subscriber.subscribe(subscription_path, callback=callback)

    while True:
        time.sleep(60)
