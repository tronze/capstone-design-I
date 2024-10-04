set +e
echo "==> Django deploy"
gunicorn -b 0.0.0.0:8000 --env DJANGO_SETTINGS_MODULE=backend_module.settings.production backend_module.wsgi.production:application