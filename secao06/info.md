## para gerar um token
```
import secrets
token: str = secrets.token_urlsafe(32)
```

## Para ver seu banco:

```
psql -h localhost -p 5432 -U [user] -d [nome_do_banco]

```