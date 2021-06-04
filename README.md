# Application Template (Python API)
Template used for any Python API servers.

### Installation

First thing, make sure you have [Python 3](https://www.python.org/downloads/) (and pip3) installed to your local computer. 

Next, clone the repo and follow the steps below:

### Installing pipenv

Note that if you have `virtualenv` installed, you will have to uninstall it first to prevent conflicting installations of virtualenv.

To install pipenv, run:

```bash
$ pip3 install pipenv
```

Then install the dependencies for this template app
```bash
$ pipenv install
```

Finally, rename the file `.env-template` to `.env` and update it with your desired configuration.

###  Run the app

Run the following command to launch the application in a virtual environment:
```bash
$ pipenv run api
```
Go to https://127.0.0.1:8001 to browse the template app.

To view the API definition and test its endpoint, go to its Flasgger page at https://127.0.0.1:8001/apidocs/ 
