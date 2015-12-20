# coding: utf-8

from django.core.management.base import BaseCommand
from core.models import *

class Command(BaseCommand):
    def handle(self, *args, **options):
        TOPICS = [
            'Crisis in Syria',
            'Boston Marathon Bombings',
            'Debt Ceiling Crisis'
        ]

        ALTS = {
            'Crisis in Syria': [
                '2011 Syrian Uprising',
                '2011 Syrian civil war',
                '2011 Syrian protests',
                '2011 Syrian revolt',
                '2011 Syrian revolution',
                '2011 protests in Syria',
                '2011 syrian upraising',
                '2011 syrian uprising',
                '2011 syrian war',
                '2011-12 Syrian uprising',
                '2011-2012 Syria uprising',
                '2011-2012 Syrian Uprising',
                '2011-2012 Syrian civil war',
                '2011-2012 Syrian uprising',
                '2011-2012 syrian uprising',
                '2011-2012 uprising in Syria',
                '2011–2012 Syrian Revolution',
                '2011–2012 Syrian Uprising',
                '2011–2012 Syrian civil war',
                '2011–2012 Syrian uprising',
                '2012 Syrian civil war',
                '2012 Syrian conflict',
                '2012 Syrian uprising',
                '2012 Syrian war',
                '2012 syria uprising',
                '2012 syrian unrest',
                'Battle of Syria',
                'Civil War in Syria',
                'Civil war in Syria',
                'Jasmine Revolution in Syria',
                'Muhammad Radwan',
                'Rami al-Sayed',
                'Syria 2011 uprising',
                'Syria civil war',
                'Syria unrest',
                'Syria war, 2013',
                'Syrian Civil War (2011–present)',
                'Syrian Civil War, November 2012 – March 2013',
                'Syrian Civil war',
                'Syrian Revolution 2011',
                'Syrian Revolution of 2011',
                'Syrian Uprising',
                'Syrian Uprising 2011',
                'Syrian civil war',
                'Syrian civil war (2011-present)',
                'Syrian crisis',
                'Syrian uprising (2011-2012)',
                'Syrian uprising (2011-present)',
                'Syrian uprising (2011–present)',
                'Syrian uprising 2011',
                'Syrian uprising 2011/12',
                'Syrian vigilante groups',
                'Syrian war (2011–2013)',
                'The civil war in Syria',
                'Uprising in Syria',
                'War in Syria',
            ],
            'Boston Marathon Bombings': [
                '2013 Boston Bombing',
                '2013 Boston Bombings',
                '2013 Boston Marathon Bombing',
                '2013 Boston Marathon Bombings',
                '2013 Boston Marathon attack',
                '2013 Boston Marathon attacks',
                '2013 Boston Marathon bombing',
                '2013 Boston Marathon bombings',
                '2013 Boston Marathon explosion',
                '2013 Boston Marathon explosions',
                '2013 Boston attack',
                '2013 Boston attacks',
                '2013 Boston bombing',
                '2013 Boston bombings',
                '2013 Boston explosion',
                '2013 Boston explosions',
                'Bombings at the Boston Marathon',
                'Boston &quot;terror&quot; blasts',
                'Boston Bombing',
                'Boston Bombings',
                'Boston Marathon 2013 Explosion',
                'Boston Marathon Bombing',
                'Boston Marathon Bombings',
                'Boston Marathon Explosion',
                'Boston Marathon Explosions',
                'Boston Marathon attack',
                'Boston Marathon attacks',
                'Boston Marathon blasts',
                'Boston Marathon bomb attack',
                'Boston Marathon bombers',
                'Boston Marathon bombing',
                'Boston Marathon bombing, 2013',
                'Boston Marathon bombings, 2013',
                'Boston Marathon explosion',
                'Boston Marathon explosions',
                'Boston attack',
                'Boston attack 2013',
                'Boston attacks',
                'Boston bomb attacks',
                'Boston bomb blasts',
                'Boston bomber',
                'Boston bombing',
                'Boston bombings',
                'Boston bombs',
                'Boston explosion',
                'Boston explosions',
                'Boston marathon 2013 bombing',
                'Boston marathon bombings',
                'Boston marathon massacre',
                'Boston terror attack',
                'Marathon bombing',
                'Marathon day bombings',
                'Patriot&rsquo;s Day bombings',
                'The Boston bombings',
            ],
            'Debt Ceiling Crisis': [
                '2013 United States debt-ceiling debate',
                'United States debt-ceiling crisis 2013',
                'United States debt-ceiling debate of 2013',                
            ],
        }

        for topic in TOPICS:
            new_topic, created = Topic.objects.get_or_create(title=topic)
            SearchTopic.objects.get_or_create(title=topic, topic=new_topic, is_master=True)

            for alt in ALTS[topic]:
                SearchTopic.objects.get_or_create(title=alt, topic=new_topic)