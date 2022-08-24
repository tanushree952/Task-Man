# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import imp
#from django.conf import settings
from ast import Delete
from asyncio import Task, tasks
from django.db import models
from django.contrib.auth.models import User

class TaskMan(models.Model):
    status_choices = [
    ('C', 'COMPLETED'),
    ('P', 'PENDING'),
    ]
    priority_choices = [
    ('1', '1️⃣'),
    ('2', '2️⃣'),
    ('3', '3️⃣'),
    ('4', '4️⃣'),
    ('5', '5️⃣'),
    ('6', '6️⃣'),
    ('7', '7️⃣'),
    ('8', '8️⃣'),
    ('9', '9️⃣'),
    ('10','🔟'),
    ]
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=2 , choices=status_choices)
    user  = models.ForeignKey(User, on_delete= models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=2 , choices=priority_choices)
    action_task = models.ForeignKey("Action", null=True,blank=True,on_delete=models.DO_NOTHING)


    class Meta:
        ordering = ["-user",]
        db_table='cnext_taskman'

class Action(models.Model):
    CREATE = 0
    UPDATE = 1
    DELETE = 2
    action_choices = (
        (CREATE, 0),
        (UPDATE, 1),
        (DELETE, 2),
    )
    task = models.IntegerField(choices=action_choices)
    user  = models.ForeignKey(User, on_delete= models.DO_NOTHING, blank=True,null=True)
    #created_by = models.ForeignKey(on_delete=models.DO_NOTHING, null=True, blank=True) 
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True,editable=True)
    #updated_by = models.ForeignKey(on_delete=models.DO_NOTHING, related_name="%(app_label)s_%(class)s_updated_by", null=True, blank=True)  
    updated_on = models.DateTimeField(auto_now_add=True,null=True,blank=True,editable=True)
    #modified_by = models.ForeignKey(on_delete=models.DO_NOTHING, related_name="%(app_label)s_%(class)s_updated_by", null=True, blank=True)
    deleted_on = models.DateTimeField(auto_now_add=True,null=True,blank=True,editable=True)
    class Meta:
        ordering = ["-user"]
        db_table="cnext_taskman_action"