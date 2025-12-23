#!/bin/sh

echo "⏳ Aguardando banco de dados..."

while ! nc -z "$DB_HOST" "$DB_PORT"; do
  sleep 1
done

echo "✅ Banco disponível"

python manage.py migrate --noinput

echo "📦 Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo "👤 Criando superusuário (se não existir)..."

python manage.py shell <<EOF
from django.contrib.auth import get_user_model
import os

User = get_user_model()

username = os.getenv("DJANGO_SUPERUSER_USERNAME")
email = os.getenv("DJANGO_SUPERUSER_EMAIL")
password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

if username and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        print("Superusuário criado")
    else:
        print("Superusuário já existe")
else:
    print("Variáveis de superusuário não definidas")
EOF

echo "🚀 Iniciando servidor"
exec "$@"