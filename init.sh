#!/bin/bash
echo "Copiando pg_hba.conf e postgresql.conf customizados..."
cp /docker-entrypoint-initdb.d/pg_hba.conf /var/lib/postgresql/data/pg_hba.conf
cp /docker-entrypoint-initdb.d/postgresql.conf /var/lib/postgresql/data/postgresql.conf
chown postgres:postgres /var/lib/postgresql/data/*.conf
