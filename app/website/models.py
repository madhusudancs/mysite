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

from django.db import models
from djangotoolbox import fields

class Post(models.Model):
    url_name = models.CharField(max_length=1024)
    title = models.CharField(max_length=1024)
    summary = models.TextField(blank=True)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True, auto_now_add=True)
    published_on = models.DateTimeField(auto_now=False, auto_now_add=False)
    tags = fields.ListField()
    links = fields.ListField()

