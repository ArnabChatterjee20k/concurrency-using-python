import asyncio

async def hello():
    await asyncio.sleep(3)
    return "hello"

data = asyncio.run(hello())
print(data)