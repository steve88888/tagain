# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecttitle',
            name='expertise',
            field=models.CharField(max_length=50, choices=[(b'All', b'All'), (b'Business and Commerce', b'Business and Commerce'), (b'Architecture, Construction, Urban Design', b'Architecture, Construction, Urban Design'), (b'Fashion & Style', b'Fashion & Style'), (b'Computer Science and Information Technology', b'Computer Science and Information Technology'), (b'Healthcare', b'Healthcare'), (b'Retail & Sales', b'Retail & Sales'), (b'Food & Restaurant', b'Food & Restaurant'), (b'Charity and fundraising organising', b'Charity and fundraising organising'), (b'Research and Thesis', b'Research and Thesis')]),
        ),
        migrations.AlterField(
            model_name='projecttitle',
            name='location',
            field=models.CharField(max_length=50, choices=[(b'All', b'All'), (b'Melbourne', b'Melbourne'), (b'Brunswick', b'Brunswick'), (b'WorldWide', b'WorldWide')]),
        ),
    ]
