### Sync code
Here all the tasks are getting done by only task 1 function

### Simple Cooperative concurrency
Here the distribution is getting done equally

### Simple Cooperative concurrency with a delay
Here we added delay in the task loop before giving the control to the parent task caller using yield. As a result the task are getting blocked and the other task cant start
The blocking call can be db ,networks,etc