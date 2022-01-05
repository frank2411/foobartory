### Create virtualenv

```shell

python3.8 (or whatever version) -m venv foobartory

source foobartory/bin/activate

pip install -r requirements.txt

pip install -e .

```


### Run the script

```shell

foobartorize

or

foobartorize --factory-name=test-name

```

### Run test suite

```shell
tox
```
