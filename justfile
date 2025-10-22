dev:
    uv run manage.py runserver

check:
    uv run manage.py check

create_app app:
    uv run manage.py startapp {{app}}

alias mm:=create_migration
create_migration:
    uv run manage.py makemigrations 

alias m:=make_migration
make_migration:
    uv run manage.py migrate

alias sh:=shell
shell:
    uv run manage.py shell

alias sm:=showmigrations
showmigrations app="":
    uv run manage.py showmigrations {{app}}


alias dbsh:=dbshell
dbshell:
    uv run manage.py dbshell


startapp app:
    #!/usr/bin/env bash
    uv run manage.py startapp {{ app }}
    APP_CLASS={{ app }}
    APP_CONFIG="{{ app }}.apps.${APP_CLASS^}Config"
    perl -0pi -e "s/(INSTALLED_APPS *= *\[)(.*?)(\])/\1\2    '$APP_CONFIG',\n\3/smg" ./main/settings.py
    echo "✔ App '{{ app }}' created & added to settings.INSTALLED_APPS"