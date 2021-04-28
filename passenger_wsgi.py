from minimal_django_app.wsgi import application

INTERP = "/home/wwagah/AgahSolutionsRepositories/minimal-django-app/venv/bin/python"

if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

from django_project.wsgi import application