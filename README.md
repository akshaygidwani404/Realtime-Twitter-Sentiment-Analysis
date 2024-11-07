# Real-Time Data Pipeline for Twitter Sentiment Analysis

![](https://github.com/akshaygidwani404/Realtime-Twitter-Sentiment-Analysis/blob/main/Images/Realtime-Twitter-Sentiment-Analysis.gif)

## Motivation

In the current era, real-time data analysis holds critical significance for both SMEs and Large Corporations, spanning industries such as Financial services, Legal services, IT operation management services, Marketing, and Advertising. This entails the examination of extensive real-time and historical data to facilitate informed business decisions.

Distinguished by its velocity, volume, and variety, Big data differs from regular data. The development of a distributed data pipeline becomes essential for processing, storing, and analyzing real-time data, distinguishing it from traditional Big data applications.

This personal project aims to apply the principles of large-scale parallel data processing to create a real-time processing pipeline using open source tools. The goal is to efficiently capture, process, store, and analyze substantial data from diverse sources, ensuring scalability and effectiveness.

## Project Description

Leveraging Twitter streaming trends popularity and sentiment analysis proves to be an exceptional choice for constructing a distributed data pipeline. On a daily basis, an impressive volume of approximately 500 million tweets, sourced globally, emerges (as of June, 2024). Out of this vast number, approximately 1%, equivalent to 5 million tweets, becomes publicly accessible.

The data pipeline is ingeniously designed, employing the following components: <b>Apache Kafka</b> as the data ingestion system, <b>Apache Spark</b> as the real-time data processing system, <b>Python Textblob</b> for sentiment analysis using NLP, and <b>Matplotlib</b> for real-time data analytics.

The Twitter data is obtained through the utilization of the Twitter Streaming API and is efficiently streamed to Apache Kafka, enabling seamless accessibility for Apache Spark, which then undertakes data processing and sentiment classification. The analysis of trend's popularity and sentiment is conducted through visualizations using Matplotlib graphs and charts.

## Data Architecture

![link](https://github.com/akshaygidwani404/Realtime-Twitter-Sentiment-Analysis/blob/main/Images/Realtime-Twitter-Sentiment-Analysis.png)

In this data pipeline architecture, the Twitter streaming producer utilizes Kafka to publish real-time tweets to the 'twitter' topic within an Apache Kafka broker. Subsequently, the Apache Spark Streaming Context subscribes to the 'twitter' topic, enabling the ingestion of tweets for further processing.

The Spark engine efficiently leverages Spark Streaming to conduct batch processing on the incoming tweets. Spark then performs preprocessing tasks like cleaning and filtering the tweets prior to performing sentiment classification on the tweets thus making use of the Textblob NLP library. The processed results are then presented in Realtime to the user in visual form using the Python Matplotlib library.

## System Design

### Kafka Twitter Streaming Producer:

The Kafka Twitter Streaming Producer is a crucial component responsible for publishing real-time tweets to the 'tweets-1' topic in the central Apache Kafka broker. Utilizing the twitter4j library for Twitter API integration, this producer captures streaming tweets written in English from various locations worldwide.

### Apache Kafka:

Apache Kafka serves as a distributed publish-subscribe messaging system and a robust queue, adept at handling high volumes of data. Its primary role is to facilitate the seamless transmission of messages between endpoints. Supporting both offline and online message consumption, Kafka ensures data persistence on disk and replicates messages within the cluster to ensure data integrity. It integrates seamlessly with Apache Spark for real-time streaming data analysis.

#### Kafka's Dependency: Apache Zookeeper

A critical dependency of Apache Kafka is Apache Zookeeper, which acts as a distributed configuration and synchronization service. Zookeeper acts as the coordination interface between Kafka brokers and consumers. Storing essential metadata, such as information about topics, brokers, consumer offsets, and more, Zookeeper enables Kafka to maintain a robust and fault-tolerant state, even in the event of broker or Zookeeper failure.

### Apache Spark:

Apache Spark, a high-speed and versatile distributed cluster computing framework, is the foundation of the project. It offers a rich set of higher-level tools, including Spark SQL for SQL and structured data processing, MLlib for machine learning, GraphX for graph processing, and Spark Streaming for real-time data analysis.

#### Spark Core:

The core component of Apache Spark, Spark Core, revolves around Resilient Distributed Datasets (RDDs) as the primary data abstraction. RDDs represent immutable, partitioned collections of elements that can be processed in parallel with fault tolerance. Spark's RDD lineage graph allows for re-computation of missing or damaged partitions due to node failures, ensuring fault-tolerance.

#### Spark Streaming:

Leveraging Spark Core, Spark Streaming performs real-time streaming analysis. The key abstraction used is Discretized Stream or DStream, representing continuous data streams. DStreams consist of a continuous series of RDDs, each containing data from a specific interval. The data processing involves both stateless and stateful transformations on the raw streaming tweets, preparing them for sentiment classification. 

### Python Textblob:

TextBlob is a Python library for processing textual data. It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, and more.