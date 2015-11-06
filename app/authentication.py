#! /usr/bin/python
""" This module provides functions for authenticating users."""

def login(username, password):
    """ Log the user in """
    print(username, password)
    return True

def logout():
    print('You are now logged out.')
