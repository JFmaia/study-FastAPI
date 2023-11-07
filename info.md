## Dados de ajuda:

> Senha do Postgress: pgdata741

> Name do volume: pgdata

- Comando para criar o container do Postgress: docker run -d  --name teste-postgres --network=postgres-network -e "POSTGRES_PASSWORD=Postgres2018!" -p 5432:5432 -v /home/renatogroffe/Desenvolvimento/PostgreSQL:/var/lib/postgresql/data -d postgres

- Comando para criar o pgadmin do Postgress: docker run --name teste-pgadmin --network=postgres-network -p 15432:80 -e "PGADMIN_DEFAULT_EMAIL=renatogroff@yahoo.com.br" -e "PGADMIN_DEFAULT_PASSWORD=PgAdmin2018!" -d dpage/pgadmin4

## Dados sobre o ambiente:

> ```mkvirtualenv``` -> para criar e já abrir o ambiente
> ```workon``` -> para ver os ambientes e tbm para entrar só colocar o nome na frente
> ```rmvirtualenv``` -> para deletar ambientes
> ```pip freeze > requirements.txt``` -> criando um requirements.txt com todas as dependências 
> ``` uvicorn main:app --reload ``` -> para rodar o app fastAPI no modo reload
> ``` gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker ``` -> comando para rodar o gunicorn, usado para deploy junto com uvicorn pois é mais parrudo.

## Dados do pgadmin
- pgadmin senha : pgdata741
- pgadmin email: jfmaia.dev@gmail.com
> Link de acesso para o pg admin:  http://localhost:15432

## Executando containes
- para rodar container pgadmin criado: sudo docker start pgadmin-fast-api
- para rodar container postgres criado: sudo docker start postgres-fast-api