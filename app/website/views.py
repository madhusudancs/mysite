# Copyright 2012 Madhusudan C.S.
#
# This file views.py is part of my site madhusudancs.info.
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

from django import shortcuts

from website import models

def home(request):
    return shortcuts.render_to_response('website/home.html')

def post(request, url_name):
    p = shortcuts.get_object_or_404(models.Post, pk=poll_id)
    return shorcuts.render_to_response('website/post.html', {'post': p})
