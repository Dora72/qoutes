# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re, bcrypt


class QuoteManager(models.Manager):
    def validate_quote(self,post):
        isValid = True
        if len(post.get("author"))<4:
            isValid = False
        if len(post.get("message"))<11:
            isValid = False
        return isValid

class UserManager(models.Manager):
    def validateUser(self,post):
            is_valid = True
            errors = []
            if len(post.get('name')) == 0:
               errors.append('Name  cannot be blank')
               is_valid = False
            user = User.objects.filter(email=post.get('email')).first()
            if user:
                   errors.append('Email is already in use.')
                   is_valid = False

            if not re.search(r'[^@]+@[^@]+\.[^@]+', post.get('email')):
                is_valid = False
                errors.append('You must provide a valid email address')
            if len(post.get('password')) < 4:
                is_valid = False
                errors.append('Password  must  have three characters.')
                is_valid = False
            if post.get('password') != post.get('password_confirmation'):
                is_valid = False
                errors.append('Your passwords do not match!')
                is_valid = False
            return {'status': is_valid, 'errors': errors}

    def createUser(self,post):
            return User.objects.create(
                    name=post.get('name'),
                    email=post.get('email'),
                    password=bcrypt.hashpw(post.get('password').encode(), bcrypt.gensalt()))

    def login_user(self, post):
        user = User.objects.filter(email=post.get('email')).first()
        if user and bcrypt.checkpw(post.get('password').encode(), user.password.encode()):
            print 'user information correct in login'
            return {'status': True, 'user': user}
        else:
            return {'status': False, 'message': 'invalid credentials'}


            # user = self.filter(email=post.get('email')).first()
             # if user and bcrypt.hashpw(post.get('password').encode(), user.password.encode()) == user.password:
             #     return (True, user)
             # return (False)


class User(models.Model):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Quote(models.Model):
    author = models.CharField(max_length=200)
    message = models.TextField()
    user = models.ForeignKey(User,related_name='quotes')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = QuoteManager()

class Favorite(models.Model):
    user = models.ForeignKey(User,related_name='favorites')
    quote = models.ForeignKey(Quote,related_name='favorites')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
