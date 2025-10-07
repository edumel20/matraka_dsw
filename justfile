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