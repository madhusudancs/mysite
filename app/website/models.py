# Copyright 2012 Madhusudan C.S.
#
# This file models.py is part of my site madhusudancs.info.
#
# This program which runs madhusudancs.info is free software: you can
# redistribute it and/or modify it under the terms of the GNU General
# Public License as published by the Free Software Foundation, either
# version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import datetime

from django.db import models
from djangotoolbox import fields

from website import forms


class ListField(fields.ListField):
    def formfield(self, **kwargs):
        return models.Field.formfield(self, forms.StringListField, **kwargs)


class Post(models.Model):
    url_name = models.CharField(max_length=1024)
    title = models.CharField(max_length=1024)
    summary = models.TextField(blank=True)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True, auto_now_add=True)
    published_on = models.DateTimeField(auto_now=False, auto_now_add=False,
                                        blank=True)
    tags = ListField()
    links = ListField()

    # Code taken from Django docs.
    def was_published_recently(self):
        return self.published_on >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = '-published_on'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

