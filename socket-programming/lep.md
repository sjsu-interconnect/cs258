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
- Also, define a reasonable string representation of the object in its ```toString()``` function
- Check ```ObjectOutputStream``` and ```ByteArrayOutputStream``` to send the object

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
