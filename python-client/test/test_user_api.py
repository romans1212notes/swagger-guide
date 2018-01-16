# coding: utf-8

"""
    Swagger Petstore

    This is a sample server Petstore server.  You can find out more about     Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).      For this sample, you can use the api key `special-key` to test the authorization     filters.

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.user_api import UserApi


class TestUserApi(unittest.TestCase):
    """ UserApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.user_api.UserApi()

    def tearDown(self):
        pass

    def test_create_user(self):
        """
        Test case for create_user

        Create user
        """
        pass

    def test_create_users_with_array_input(self):
        """
        Test case for create_users_with_array_input

        Creates list of users with given input array
        """
        pass

    def test_create_users_with_list_input(self):
        """
        Test case for create_users_with_list_input

        Creates list of users with given input array
        """
        pass

    def test_delete_user(self):
        """
        Test case for delete_user

        Delete user
        """
        pass

    def test_get_user_by_name(self):
        """
        Test case for get_user_by_name

        Get user by user name
        """
        pass

    def test_list_users(self):
        """
        Test case for list_users

        
        """
        pass

    def test_login_user(self):
        """
        Test case for login_user

        Logs user into the system
        """
        pass

    def test_logout_user(self):
        """
        Test case for logout_user

        Logs out current logged in user session
        """
        pass

    def test_update_user(self):
        """
        Test case for update_user

        Updated user
        """
        pass


if __name__ == '__main__':
    unittest.main()