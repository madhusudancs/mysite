# Copyright 2012 Madhusudan C.S.
#
# This file urls.py is part of my site madhusudancs.info.
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

from django.conf.urls import defaults
from django.contrib import admin

admin.autodiscover()

urlpatterns = defaults.patterns('',
    defaults.url(r'^$', 'app.website.views.home', name='home'),
    defaults.url(r'^(?P<url_name>[\w-]*)$', 'app.website.views.post', name='post'),
    defaults.url(r'^staging/admin/', defaults.include(admin.site.urls)),
)
