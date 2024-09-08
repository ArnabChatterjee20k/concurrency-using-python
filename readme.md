1. https://realpython.com/python-async-features/
2. https://medium.com/velotio-perspectives/an-introduction-to-asynchronous-programming-in-python-af0189a88bbb
3. https://medium.com/@pekelny/fake-event-loop-python3-7498761af5e0
4. https://mysteryweevil.medium.com/mastering-python-concurrency-a-practical-guide-fb09077febc0
5. https://stackoverflow.com/questions/14841460/context-switching-with-yield#:~:text=One%20usually%20treats%20yield%20as,possibly%20useful%2C%20it%20yield%20s.
6. https://realpython.com/python-with-statement/
7. https://discuss.python.org/t/add-yield-function-to-python-threading/25669
8. https://www.reddit.com/r/learnpython/comments/rzukrb/what_is_the_idea_of_using_yield_in_python/
9. https://medium.com/@syedyasir441/context-managers-in-python-what-are-they-and-how-you-can-create-one-84791987ad93
10. https://www.youtube.com/watch?v=7lmCu8wz8ro
Async, event loop, coroutines
Multithreading, processing
Async file storage, file handling -> twitter
### using yield
The yield statement turns task() into a generator. A generator function is called just like any other function in Python, but when the yield statement is executed, control is returned to the caller of the function. This is essentially a context switch, as control moves from the generator function to the caller.