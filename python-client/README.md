# swagger-client
This is a sample server Petstore server.  You can find out more about     Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).      For this sample, you can use the api key `special-key` to test the authorization     filters.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = swagger_client.UserApi()
body = swagger_client.User() # User | Created user object

try:
    # Create user
    api_instance.create_user(body)
except ApiException as e:
    print("Exception when calling UserApi->create_user: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://petstore.swagger.io/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*UserApi* | [**create_user**](docs/UserApi.md#create_user) | **POST** /user | Create user
*UserApi* | [**create_users_with_array_input**](docs/UserApi.md#create_users_with_array_input) | **POST** /user/createWithArray | Creates list of users with given input array
*UserApi* | [**create_users_with_list_input**](docs/UserApi.md#create_users_with_list_input) | **POST** /user/createWithList | Creates list of users with given input array
*UserApi* | [**delete_user**](docs/UserApi.md#delete_user) | **DELETE** /user/{username} | Delete user
*UserApi* | [**get_user_by_name**](docs/UserApi.md#get_user_by_name) | **GET** /user/{username} | Get user by user name
*UserApi* | [**list_users**](docs/UserApi.md#list_users) | **GET** /user | 
*UserApi* | [**login_user**](docs/UserApi.md#login_user) | **GET** /user/login | Logs user into the system
*UserApi* | [**logout_user**](docs/UserApi.md#logout_user) | **GET** /user/logout | Logs out current logged in user session
*UserApi* | [**update_user**](docs/UserApi.md#update_user) | **PUT** /user/{username} | Updated user


## Documentation For Models

 - [ListUserResponse](docs/ListUserResponse.md)
 - [User](docs/User.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

apiteam@swagger.io

