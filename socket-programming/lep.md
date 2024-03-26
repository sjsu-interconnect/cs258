# The Leader Election Problem

## What is The Leader Election Problem?
- In distributed computing, leader election is the process of designating a single process as the organizer of some task distributed among several computers (nodes).
- [Reference](https://en.wikipedia.org/wiki/Leader_election#)


## Definition
A valid leader election algorithm must meet the following conditions:

1. Termination: the algorithm should finish within a finite time once the leader is selected. In randomized approaches this condition is sometimes weakened (for example, requiring termination with probability 1).
2. Uniqueness: there is exactly one processor that considers itself as leader.
3. Agreement: all other processors know who the leader is.

## Generating Unique ID
- A Universally Unique Identifier (UUID) is a 128-bit label used for information in computer systems.
- When generated according to the standard methods, UUIDs are, for practical purposes, unique.
- [Reference](https://en.wikipedia.org/wiki/Universally_unique_identifier)
- [Java Implementation](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html)

## Node Configuration
- We assume an asynchronous non-anonymous ring.
- Each node has exactly two neighbors.
  - Your code should include both client and server functionalities. 
    - As a server, you will wait for another node to connect to your node.
    - As a client, you will connect to another node.
  - You will exchange a pair of IP address and port number outside of the code in class.
  - You prepare a simple text file ```config.txt``` in the same directory as the code. The configuration file should look like:
    ```
    10.1.1.1,5001
    10.1.1.2,5001
    ```
    - The first line should include your IP address (as a server).
    - The second line is the info exchanged with another student (as a client).
  - When you run the code, the configuration file should be used to initialize the connections. (You may want to set a reasonable length of sleep time to wait for a server node to be up.)

## Connection
- Once you establish a socket connection, please maintain the connection between the neighbors for further communications. (Do not accept or ask for a new connection.)

## Multithreading
- When you ```accept``` a connection, the server process needs to be run in a separate thread.
- This is because, if the single thread program has ```accept``` and ```connect``` in a sequence (as follows), there is no one to start the client connection, while waiting as a server with the ```accept```
```
1: server.accept()
2: client.connect()
```
- After a connection is established, you can use single threading (or keep the multiple threads with a shared memory).

## Algorithm
- Your node performs the $O(n^2)$ algorithm. 
- Read the first two paragraphs under under [the _Asynchronous ring_ section](https://en.wikipedia.org/wiki/Leader_election#Asynchronous_ring[3]) in the Wikipedia reference article.
- Sending direction
  - You should receive messages as a Server and send messages as a Client.
- Once you, as a client, are connected to a server, you should send a message with your uuid (without any comparison) as the initial message. This only happens once.

## Message Format
- You must define a ```Message``` class, which have two member variables:
  - ```java.util.UUID uuid```: indicating the sender's UUID. Note: This ID should be the same throughout the leader election process. (e.g. ```123e4567-e89b-42d3-a456-556642440000```)
  - ```int flag```: representing if the leader is already elected.
    - ```0``` if it is still in the process of leader election
    - ```1``` if a leader is already elected. In this case, the ID in the same message should be the one of the leader. 
- Check ```ObjectOutputStream``` to send the object
- Use ```serialVersionUID = 4201L``` 
  
  > If a serializable class does not explicitly declare a serialVersionUID, then the serialization runtime will calculate a default serialVersionUID value for that class based on various aspects of the class, as described in the Java(TM) Object Serialization Specification. However, it is strongly recommended that all serializable classes explicitly declare serialVersionUID values, since the default serialVersionUID computation is highly sensitive to class details that may vary depending on compiler implementations, and can thus result in unexpected InvalidClassExceptions during deserialization. Therefore, to guarantee a consistent serialVersionUID value across different java compiler implementations, a serializable class must declare an explicit serialVersionUID value. It is also strongly advised that explicit serialVersionUID declarations use the private modifier where possible, since such declarations apply only to the immediately declaring class--serialVersionUID fields are not useful as inherited members. Array classes cannot declare an explicit serialVersionUID, so they always have the default computed value, but the requirement for matching serialVersionUID values is waived for array classes. ([reference](https://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html))
- This class should be outside of a user-defined package, if exists.

## Termination
- When enough time passes, every node in the ring (including your node) should have stopped sending messages (Termination condition) and had the same ID in a member variable named ```leaderID``` (Uniqueness and Agreement conditions).

## Log
- When a process receives a message, it should clearly show, on a log file ```log.txt```,
  - ```uuid``` in the message
  - ```flag```
  - if the process's uuid is larger than the message's uuid (1 if larger; 0 if same; -1 if smaller)
  - if this process is in state 0 (still trying to find a leader) or state 1 (it knows the leader's ID).
    - If it is in state 1, show the leader's ID
- When a process ignores the message, it should clearly show, on a log file, that the received message was ignored.
- When a process sends a message, it should clearly show, on a log file, 
  - ```uuid``` in the message
  - ```flag```

