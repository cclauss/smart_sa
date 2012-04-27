""" just pull the data down and save it into a data directory
this is prep for making the windows install USB key """

from django.core.management.base import BaseCommand
from intervention.models import Intervention
from problemsolving_game.models import Issue
from django.conf import settings
from restclient import GET
from zipfile import ZipFile
from cStringIO import StringIO
from simplejson import dumps,loads
import os
import os.path
from optparse import make_option

class Command(BaseCommand):
    args = ''
    help = ''

    option_list = BaseCommand.option_list + (
        make_option('-d', '--db-only', dest='dbonly',
                    default=False,help='only pull the database content'),
    )

    def handle(self, *args, **options):
        if not settings.DEBUG:
            print "this should never be run on production"
            return

        print "fetching content from prod..."
        zc = GET(settings.PROD_BASE_URL + "intervention_admin/content_sync/")
        if not options["dbonly"]:
            uploads = GET(settings.PROD_BASE_URL + "intervention_admin/list_uploads/").split("\n")

        with open("data/intervention.zip","w") as zipfile:
            zipfile.write(zc)
            
        if options["dbonly"]:
            return

        print "updating uploaded files..."
        base_len = len(settings.PROD_MEDIA_BASE_URL)
        for upload in uploads:
            relative_path = upload[base_len:]
            relative_dir = os.path.join(*os.path.split(relative_path)[:-1])
            full_dir = os.path.join(settings.MEDIA_ROOT,relative_dir)
            try:
                os.makedirs(full_dir)
            except OSError:
                pass
            with open(os.path.join(settings.MEDIA_ROOT,relative_path),"w") as f:
                print "   writing %s to %s" % (upload,relative_path)
                f.write(GET(upload))