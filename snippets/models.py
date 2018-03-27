# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.core.validators import RegexValidator

class user(models.Model):
    user_name_regex = RegexValidator(regex=r'^[a-zA-Z0-9_.-]+$',
                                 message="User Name must the alphanumeric and only ('.', '-') are allowed as an special character ")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    user_id = models.IntegerField(auto_created=True, editable=False, primary_key=True)
    user_name = models.CharField(validators=[user_name_regex], editable=False, unique=True, max_length=20, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    email_id = models.EmailField(max_length=100, blank=False, unique=True, null=False)
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=False, null=False)  # validators should be a list
    facebook_id = models.CharField(blank=True, null=True, max_length=100)
    twitter_id = models.CharField(blank=True, null=True, max_length=100)
    creation_dt = models.DateTimeField(null=False, blank=False)
    last_chg_usr = models.CharField(max_length=10, null=False, default='ops')
    owner = models.ForeignKey('auth.User', related_name='user', on_delete=models.CASCADE)
    last_chg_dt = models.DateTimeField(auto_now=True, null=False)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        super(user, self).save(*args, **kwargs)

    class Meta:
        ordering = ('user_name', 'name', 'email_id', )


class user_wallet(models.Model):
    wallet_id = models.IntegerField(auto_created=True, editable=False, primary_key=True)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    money = models.FloatField()
    loyalty_points = models.FloatField()
    last_chg_usr = models.DateTimeField(null=False, default='ops')
    last_chg_dt = models.DateTimeField(auto_now=True, null=False)
    owner = models.ForeignKey('auth.User', related_name='user_wallet', on_delete=models.CASCADE)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        super(user, self).save(*args, **kwargs)

    class Meta:
        ordering = ('wallet_id', 'user_id', 'money', 'loyalty_points',)



class type_of_tr(models.Model):

    tot_id = models.IntegerField(auto_created=True, editable=False, primary_key=True)
    short_desc = models.CharField(max_length=10, blank=False, null=False)
    full_desc = models.CharField(max_length=200, blank=False, null=False)
    format = models.CharField(max_length=200, blank=False, null=False)
    last_chg_usr = models.DateTimeField(null=False, default='ops')
    last_chg_dt = models.DateTimeField(auto_now=True, null=False)
    owner = models.ForeignKey('auth.User', related_name='type_of_tr', on_delete=models.CASCADE)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        super(user, self).save(*args, **kwargs)

    class Meta:
        ordering = ('tot_id', 'short_desc', 'full_desc', 'format',)


class tr_status_map(models.Model):
    map_id = models.IntegerField(auto_created=True, editable=False, primary_key=True)
    description = models.CharField(blank=True, null=True, max_length=25)
    last_chg_usr = models.DateTimeField(null=False, default='ops')
    last_chg_dt = models.DateTimeField(auto_now=True, null=False)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        super(user, self).save(*args, **kwargs)

    class Meta:
        ordering = ('map_id',)



class transactions(models.Model):
    tr_id = models.IntegerField(auto_created=True, editable=False, primary_key=True)
    wallet_id = models.ForeignKey(user_wallet, on_delete=models.CASCADE)
    tot_id = models.ForeignKey(type_of_tr, on_delete=models.CASCADE)
    description = models.CharField(blank=True, null=True, max_length=100)
    map_id = models.ForeignKey(tr_status_map, on_delete=models.CASCADE)
    last_chg_usr = models.DateTimeField(null=False, default='ops')
    last_chg_dt = models.DateTimeField(auto_now=True, null=False)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        super(user, self).save(*args, **kwargs)

    class Meta:
        ordering = ('tr_id', 'tot_id',)


class transaction_stats(models.Model):
    tr_st_id = models.IntegerField(auto_created=True, editable=False, primary_key=True)
    tr_id = models.ForeignKey(transactions, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(auto_now=True)
    last_chg_usr = models.DateTimeField(null=False, default='ops')
    last_chg_dt = models.DateTimeField(auto_now=True, null=False)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        super(user, self).save(*args, **kwargs)

    class Meta:
        ordering = ('tr_st_id',)



class active_tr_usr(models.Model):
    wallet_id = models.ForeignKey(user_wallet, on_delete=models.CASCADE)
    tr_id = models.ForeignKey(transactions, on_delete=models.CASCADE)
    tr_st_id = models.ForeignKey(transaction_stats, on_delete=models.CASCADE)
    last_chg_usr = models.DateTimeField(null=False, default='ops')
    last_chg_dt = models.DateTimeField(auto_now=True, null=False)
    owner = models.ForeignKey('auth.User', related_name='active_tr_usr', on_delete=models.CASCADE)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        super(user, self).save(*args, **kwargs)

    class Meta:
        ordering = ('wallet_id',)



class transaction_top_10(models.Model):
    tr_id = models.ForeignKey(transactions, on_delete=models.CASCADE)
    wallet_id = models.ForeignKey(user_wallet, on_delete=models.CASCADE)
    tot_id = models.ForeignKey(type_of_tr, on_delete=models.CASCADE)
    description = models.CharField(blank=True, null=True, max_length=100)
    last_chg_usr = models.DateTimeField(null=False, default='ops')
    last_chg_dt = models.DateTimeField(auto_now=True, null=False)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        super(user, self).save(*args, **kwargs)

    class Meta:
        ordering = ('tr_id', 'tot_id',)



class transaction_failed(models.Model):
    tr_fld_id = models.IntegerField(auto_created=True, editable=False, primary_key=True)
    tr_id = models.ForeignKey(transactions, on_delete=models.CASCADE)
    description = models.CharField(blank=True, null=True, max_length=100)
    last_chg_usr = models.DateTimeField(null=False, default='ops')
    last_chg_dt = models.DateTimeField(auto_now=True, null=False)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        super(user, self).save(*args, **kwargs)

    class Meta:
        ordering = ('tr_fld_id', 'tr_id',)
