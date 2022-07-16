#  Reliable, Scalable and Maintainable Applications

**Reliability:** The system should continue to work correctly(performing the correct function at the desired level of performance) even in the face of adversity(hardware or sofware faults and even human error).

**Scalability:** As the system grows(in data volume, traffic volume, or complexity), there should be reasonable ways of dealing with that growth.

**Maintainability:** Over time, many different people will work on the system, both maintaining current behaviour and adapting the system to new use cases, they should all be able to work on it productively.
<br />
<br />
<hr>

## Reliability
Typical expectations include:
- Application performs the function that the user expected.
- Tolerate user mistakes
- Good performance
- Prevents authorized access and abuse

Systems that anticipate faults and cope with them are called *fault-tolerant or resilient*.

Fault: A compenent of the system deviating from it's spec. <br>
Failure: System stops providing the required service to the user <br>

You should generally prefer tolerating faults over preventing faults.
- **Hardware Faults:**  Until recently, redundancy of hardware components was sufficient. As data volumes and computing demands have increased, rate of hardware faults has also increased. So there is a move towards systems that tolerate loss of machines using software fault tolerance techniques A system that tolerates machine failures can be patched one node at a time without requiring down time (rolling upgrade).
- **Software Errors:** Errors within the system. Can be prevented/reduced by 
    - carefully thinking about the assumptions and interactions in the system
    - thorough testing
    - process isolation - allow processes to crash and restart
    - measuring and monitoring
- **Human Error:** Humans are unreliable. Reduce these by,
  -  Minimize opportunities for error
  -  decouple environments - production like sandbox to experiment
  -  thorough testing, automated testing, unit tests for corner cases.
  -  allow quick and easy recovery - rollbacks, configuration backups.
  -  clear monitoring and performance metrics

<hr >

## Scalability
System's ability to cope with increased load.
<br><br>

### Describing Load:
 it's described using a few numbers which are called load parameters. Choice of load parameters depends on the architecture of your system. A few are,
  - requests/second to a web server
  - ratio of reads to writes
  - number of simultaneously active users
  - hit rate on cache

<br>

### Twitter Example:
Twitter's main operations are,
1.  Post Tweet: A user can publish a new message to their followers 0 4.6k requests/sec on average, over 12k requests/sec at peak.
2.  Home timeline: A user can view tweets posted by the people they follow (300k requestss/sec)

12k writes per second is easy to handle but Twitter's main problem is fan-out - each user is followed by many others. There are 2 ways of implementing these 2 operations,
1.  Query Tweets Real-Time - Insert new tweet to a global collection. When a user requests their home timeline, lookup all the people they follow, find all the tweets for each of those users and merge them sorted by time. In a relational database, it can be done using SQL JOINs.
2.  Pre-compute Home Timeline - Maintain a cache for each user's timeline, when a user posts a tweet, lookup followers and put it into follower's cached timeline.

Approach 1 struggled to keep up with the laod of home timeline queries. <br>
Approach 2 requires a lot of extra work. On average, a tweet is delivered to 75 followers, so 4.6k tweets per second becomes 345k writes per second to home timeine cache. If a user has millions of followers, a single tweet => 300m writes to the cache. 

Twitter moved to an hybrid of both approaches. Tweets continue to be fanned out to home timelines but a small number of users with a very large number of followers are fetched separately and merged with that user's home timeline when it is read, like in approach 1.
<br><br>

### Describing Performance:
How to investigate what happens when load increases?
1. Increase load parameters, keep system resources unchanged
2. Increase load parameters, find out how much you need to increase system resources to keep performance unchanged.

Performance is described differently in different systems,
- In batch processing systems like hadoop, we care about throughput
  > Throughput - the number of records processed per second or total time it takes to run a job on a dataset of a certain size

- In an online system, usually service's response time is more important
  > Response Time - time between a client sending a request and receiving a response.
  > Latency - Duration that a request is waiting to be handled


Response times vary slightly for each request, so it's not taken as a single number, but as a *distribution* of values. It's common to see average response time used as a metric but  it's not a good metric as it doesn't tell you how many users experienced a delay.

It's usually better to use *percentiles* to describe response times
- Median - arrange response times in increasing order and take the middle value. It is the 50th percentile number (50p). Meaning 50% of requests were under this value.
- Percentiles 95th, 99th and 99.9th (p95, p99 and p999) are good to figure out how bad your outliners are.

  
Amazon describes response time requirements for internal services in terms of the 99.9th percentile because the customers with the slowest requests are often those who have the most data. The most valuable customers.

*Service level objectives* (SLOs) and *Service Level Agreements *(SLAs) are contracts that define the expected performance and availability of a service. An SLA may state the median response time to be less than 200ms and a 99th percentile under 1s. These metrics set expectations for clients of the service and allow customers to demand a refund if the SLA is not met.

### Approaches for Coping with Load
- *Scaling up or Vertical scaling -* Moving to more powerful machines
- *Scaling out or Horizontal scaling -* Distributing load across multiple smaller machines - cheaper
- *Elastic systems -* Automatically add computing resources when it detects a load increase - useful if load is unpredictable.

<hr>

## Maintainability
The majority of the cost of software is in its ongoing maintenance. There are three design principles for software systems:
- *Operability -* Make it easy for operation teams to keep the system running.
- *Simplicity -* Easy for new engineers to understand the system by removing as much complexity as possible.
- *Evolvability* - Make it easy for engineers to make changes to the system in the future.

### Operability: making life easy for operations
A good operations team is responsible for
- Monitoring and quickly restoring service if it goes into bad state
- Tracking down the cause of problems
- Keeping software and platforms up to date
- Keeping tabs on how different systems affect each other
- Anticipating future problems
- Establishing good practices and tools for development
- Perform complex maintenance tasks, like platform migration
- Maintaining the security of the system
- Defining processes that make operations predictable
- Preserving the organisation's knowledge about the system

### Simplicity: managing complexity
When complexity makes maintenance hard, budget and schedules are often overrun. There is a greater risk of introducing bugs.

Making a system simpler means removing accidental complexity, as non inherent in the problem that the software solves (as seen by users).

One of the best tools we have for removing accidental complexity is abstraction that hides the implementation details behind clean and simple to understand APIs and facades.

### Evolvability: making change easy
Agile working patterns provide a framework for adapting to change.

>*Functional requirements -* what the application should do. <br>
>*Nonfunctional requirements* - general properties like security, reliability, compliance, scalability, compatibility and maintainability.



 