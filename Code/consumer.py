import json
import re
import time
from kafka import KafkaConsumer
from random import randint

# Set up Kafka consumer to read from 'twitter' topic
consumer = KafkaConsumer(
    'twitter',
    bootstrap_servers='ed-kafka:29092',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

def cleanTweet(tweet: str) -> str:
    tweet = re.sub(r'http\S+', '', str(tweet))
    tweet = re.sub(r'bit.ly/\S+', '', str(tweet))
    tweet = tweet.strip('[link]')

    # remove users
    tweet = re.sub('(RT\\s@[A-Za-z]+[A-Za-z0-9-_]+)', '', str(tweet))
    tweet = re.sub('(@[A-Za-z]+[A-Za-z0-9-_]+)', '', str(tweet))

    # remove punctuation
    my_punctuation = '!"$%&\'()*+,-./:;<=>?[\\]^_`{|}~•@â'
    tweet = re.sub('[' + my_punctuation + ']+', ' ', str(tweet))

    # remove numbers
    tweet = re.sub('([0-9]+)', '', str(tweet))

    # remove hashtags
    tweet = re.sub('(#[A-Za-z]+[A-Za-z0-9-_]+)', '', str(tweet))

    return tweet


# Read from Kafka and clean each tweet
for message in consumer:
    raw_tweet = message.value
    clean_tweet = cleanTweet(raw_tweet)
    
    # Simulate a delay to mimic streaming
    time.sleep(randint(1, 5))
    
    # Send cleaned tweet to 'cleaned-tweets' topic
    producer.send('cleaned-tweets', clean_tweet)
    producer.flush()
    
    print(f"Cleaned Tweet: {clean_tweet}")
