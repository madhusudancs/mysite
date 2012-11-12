import pickle

from datetime import datetime
from time import mktime

from website import models

for p in models.Post.objects.all():
    p.delete()

data = pickle.load(open('/media/professional/blogdata/myoldblog.txt', 'r'))
entries = data['entries']

for e in entries:
    dt = datetime.fromtimestamp(mktime(e['published_parsed']))
    text = e['summary']
    p = models.Post.objects.create(
        title=e['title'], url_name=e['link'].rsplit('/', 1)[1],
        summary='%s%s' % (text.split('</p>')[0], '</p>'), text=text, published_on=dt)
    p.tags
    tags = e.get('tags', None)
    if tags:
        p.tags.extend([t['term'] for t in e['tags']])
    p.save()

