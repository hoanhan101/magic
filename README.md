# magic

A Makefile is provided in the project repository to quickly setup and develop the project. Note that the project use python 3.8 and poetry for dependency management. Make sure you have these installed in your local machine first.

Now, to install the project dependencies:
```
make setup
```

To start the project:
```
make up
```
However, this assumes that you have `data.csv` in your current directory. To run the dataset from anywhere, simply issue:
```
poetry run python app.py --filepath={{your_dataset_filepath}}
```

To run the project's unit tests:
```
make test
```

For more make's targets, simply issue a `make` or `make help`.
