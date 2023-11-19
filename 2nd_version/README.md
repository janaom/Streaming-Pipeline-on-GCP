# Instructions

This version works on GCP. You need to create a SA and save the json key. 

Create Topics and Subscribtions

![image](https://github.com/janaom/Streaming_Pipeline_on_GCP/assets/83917694/f99aa753-9158-4754-97ac-60da709dd39f)


## Run `publish_2nd_version.py` in the first terminal

This reads a CSV file, and publishes each record in the CSV file as a message to a pub/sub topic.


![image](https://github.com/janaom/Streaming_Pipeline_on_GCP/assets/83917694/801f90c8-43da-43f3-ba71-ba12317d0f10)


## Run process_2nd_version.py in the 2nd temrinal

This code sets up a Beam pipeline that reads data from a pub/sub subscription, processes it, and writes it to a different pub/sub topic.

## Run subscribe_2nd_version in the 3rd terminal

This code sets up a subscriber to receive messages from a specified pub/sub subscription.

![image](https://github.com/janaom/Streaming_Pipeline_on_GCP/assets/83917694/5d53c1e8-745b-4c14-ba0c-23bf4e873329)
