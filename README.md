# Streaming_Pipeline_on_GCP


## PubSub Streaming Architecture
![image](https://github.com/janaom/Streaming_Pipeline_on_GCP/assets/83917694/889166ce-862d-42a7-927e-66d3d4eaf2ed)

## publish.py 
publish.py script publishes messages to a Google Cloud Pub/Sub topic
  - This code publishes messages to a Google Cloud Pub/Sub topic.
  - It imports necessary modules, sets up project and topic information, and authenticates using a service account.
  - It reads input data from a file and publishes each line of the file as a message to the Pub/Sub topic.
  - The publishing process is controlled by a loop, and a 1-second delay is added between each message publication.

## process.py
process.py script uses Apache Beam to process data from a Google Cloud Pub/Sub subscription and write the processed data to another Pub/Sub topic. Then comes the Beam pipeline, it is reading data from PubSub using input_subscription and writing it to output_topic
  - This code uses Apache Beam to process data from a Google Cloud Pub/Sub subscription and write the processed data to another Pub/Sub topic.
  - It imports necessary modules from Apache Beam, sets up pipeline options and authentication using a service account.
  - It defines a pipeline that reads data from a Pub/Sub subscription, applies any necessary transformations, and writes the processed data to a Pub/Sub topic.
  - The pipeline is executed, and the code waits until the pipeline execution is finished.

## subscribe.py
subscribe.py script creates a Google Cloud Pub/Sub subscriber and receives messages from a specified subscription
  - This code creates a Pub/Sub subscriber that continuously listens for messages from a specified subscription and processes them when received.
  - It imports necessary modules, sets up authentication using a service account, and specifies the subscription to listen to.
  - It defines a callback function that is called whenever a message is received. In this case, the function simply prints the received message.
  - The subscriber is set up to continuously listen for messages from the subscription using the callback function.
  - The script enters an infinite loop with a 60-second delay between iterations to keep the subscriber listening for new messages.

## Summary
In summary, the project involves publishing messages to a Pub/Sub topic, processing those messages using Apache Beam, and subscribing to a different topic to consume and perform actions on the processed messages.
