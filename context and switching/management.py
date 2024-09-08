from contextlib import contextmanager

# same as writing with __enter__ and __exit__

@contextmanager
def db():
    print("entering the context")
    yield "connection"
    print("exiting the context")

with db() as con:
    print(con)