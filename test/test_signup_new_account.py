# -*- coding: utf-8 -*-

def test_signup_new_account(app):
    username = "user_test"
    password = "test"
    app.james.ensure_user_exists(username, password)