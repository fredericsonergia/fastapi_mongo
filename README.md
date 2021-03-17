# fastapi-mongo


# how to run it

Be sure you run on python3.8 and up

run on virtual env:

```python

python3.9 -m venv .venv
source .venv/bin/activate

```

install lib with:

```python

(.venv) $ pip install -r requirements.txt

```

mongoDB install on MacOS with brew:

```bash 

$ brew tap mongodb/brew
$ brew install mongodb-community@4.4
$ brew services start mongodb-community@4.4

```

check mongod is running

```bash
$ mongo --version
MongoDB shell version v4.4.3
Build Info: {
    "version": "4.4.3",
    "gitVersion": "913d6b62acfbb344dde1b116f4161360acd8fd13",
    "modules": [],
    "allocator": "system",
    "environment": {
        "distarch": "x86_64",
        "target_arch": "x86_64"
    }
}


```


# Motor Setup 

we'll configure Motor, an asynchronous MongoDB driver, to interact with the database.