# Design a news feed system like twitter. Users can follow other users, post messages and see messages the people they follow post. System needs to be highly scalable

Was thinking about this question with Leon, it was actually a lot of fun.

Some parts are trivial, like api for following and posting messages and we both felt that the heart of the question (which we haven't really soled well) is displaying the top messages from people you follow.

There are a few questions that came up during our conversation and I wanted to take a look and answer them here.

## Cassandra VS mongo 
We were thinking about how to store the messages data. 
We want to optimize for fast reads and support a high scale.

I suggestd Mongo because we don't need sql and it's supposed to have a very good scale, and if we're ok with eventual consistancy it can outperform traditional relational dbs. 

Cassandra has higher availability as it has multiple master node in a cluster at all times whereas mongodb has one master and if it goes down a slave takes over (which can take some time).

Writes are faster in Cassandra as there are multiple writes

Data model - mongo is a document - so a json. Cassandra uses a table structure (rows and columns).

## mongo sharded queries-  how do they work

there's a Mongos router that takes in a query. Most efficiantly, when querying multiple shards, we can provide a shard key on a collection and so queries are routed to the correct shard.

