# Usa a imagem oficial do PostgreSQL mais recente
FROM postgres:latest
RUN localedef -i de_DE -c -f UTF-8 -A /usr/share/locale/locale.alias pt_BR.UTF-8
ENV LANG=pt_BR.UTF-8

# Carregar as Variáveis de ambiente do .env
ARG POSTGRES_PASSWORD
ARG POSTGRES_USER
ARG POSTGRES_DB

# Variáveis de ambiente para configuração do PostgreSQL
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_DB=${POSTGRES_DB}

# Expõe a porta padrão do PostgreSQL
EXPOSE 5432

# Set the default command to run when starting the container
CMD ["postgres"]