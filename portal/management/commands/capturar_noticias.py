from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup as BS
from portal.models import Noticia, Site

class Command(BaseCommand):

    help = 'It gets information from others portals to populate our database.'

    def add_arguments(self, parser):
        parser.add_argument('-o', '--origin', type=str, help='For now, we just accept the value \'Tecmundo\' e it\'s the default value.')

    def handle(self, *args, **kwargs):
        origin = kwargs['origin'].title() if(kwargs['origin']) else 'Tecmundo';

        Site.objects.get_or_create(nome=origin, url='https://www.tecmundo.com.br/',
                                          class_pattern='tec--card__title__link')
        if origin != 'Tecmundo':
            self.stdout.write(self.style.NOTICE('Please, choose a valid value.'))
        else:
            self.stdout.write(self.style.SUCCESS('Starting web scraping at "' + origin + '".'))
            site = Site.objects.get(nome=origin)
            # self.stdout.write(self.style.SUCCESS(site.url))
            url = site.url

            page = requests.get(url)

            soup = BS(page.text, 'html.parser')

            noticesFromPage = soup.find_all(class_=site.class_pattern)

            for notice in noticesFromPage:
                try:
                    obj = Noticia.objects.get(titulo=BS.getText(notice).strip(), link=BS.get(notice, 'href'), site=site)
                except Noticia.DoesNotExist:
                    obj = Noticia(titulo=BS.getText(notice).strip(), link=BS.get(notice, 'href'), site=site)
                    obj.save()


            self.stdout.write(self.style.SUCCESS('Finished!'))
