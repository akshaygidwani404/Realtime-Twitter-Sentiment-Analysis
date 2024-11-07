# Import necessary libraries
import tweepy  # For accessing Twitter API
from kafka import KafkaProducer  # For sending data to a Kafka topic
import logging  # For logging data events
from twitter import streaming_tweets  # Import custom module/function to start streaming tweets

# Initialize a Kafka producer to send messages to Kafka topic
producer = KafkaProducer(bootstrap_servers='ed-kafka:29092')  # Kafka server connection
topic_name = 'twitter'  # Kafka topic to which tweets will be sent

# Define a class to listen to tweets using the Twitter Streaming API
class TweetListener(tweepy.StreamingClient):

    # Override the on_data method to process incoming tweet data
    def on_data(self, raw_data):
        # Log the raw data for debugging or monitoring purposes
        logging.info(raw_data)
        # Send the tweet data to the specified Kafka topic
        producer.send(topic_name, value=raw_data)
        # Return True to keep the connection alive
        return True

    # Override the on_error method to handle errors
    def on_error(self, status_code):
        # If rate limited (status code 420), stop streaming by returning False
        if status_code == 420:
            return False

    # Method to start streaming tweets with specific filters
    def start_streaming_tweets(self):
        # Start streaming, with warnings and filter for English-language tweets
        self.filter(stall_warnings=True, languages=["en"])

# Main block to execute when script is run directly
if __name__ == '__main__':
    # Start the tweet streaming process
    streaming_tweets.start_streaming_tweets()
