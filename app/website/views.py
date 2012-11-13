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

import itertools
from django import shortcuts

from website import models


def home(request):
    if request.user.is_staff:
        unpub_posts = models.Post.objects.filter(
            published_on__isnull=True).order_by('-modified_on').all()
        pub_posts = models.Post.objects.filter(
            published_on__isnull=False).order_by('-published_on').all()
        posts = list(itertools.chain(unpub_posts, pub_posts))
    else:
        # Show only published posts in the reverse chronological order.
        posts = models.Post.objects.filter(
            published_on__isnull=False).order_by('-published_on').all()

    return shortcuts.render_to_response('website/home.html', {'posts': posts})


def post(request, url_name):
    if request.user.is_staff:
        post = shortcuts.get_object_or_404(models.Post, url_name=url_name)
    else:
        # If the post does not exist or is not published, we should 404.
        post = shortcuts.get_object_or_404(models.Post, url_name=url_name,
                                           published_on__isnull=False)

    return shortcuts.render_to_response('website/post.html', {'post': post})
