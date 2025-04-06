#!/bin/bash
set -e

# Copia as configurações personalizadas para o diretório de dados
cp /tmp/custom-pg_hba.conf "$PGDATA/pg_hba.conf"
cp /tmp/custom-postgresql.conf "$PGDATA/postgresql.conf"

# Configura permissões
chmod 600 "$PGDATA/pg_hba.conf"
chmod 600 "$PGDATA/postgresql.conf"

# Reinicia o PostgreSQL para aplicar as alterações
pg_ctl -D "$PGDATA" reload || true