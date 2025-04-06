FROM postgres:latest

# Instala e configura o locale en_US.UTF-8
RUN apt-get update \
    && apt-get install -y locales \
    && sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && dpkg-reconfigure --frontend=noninteractive locales \
    && locale-gen en_US.UTF-8 \
    && update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Configura o locale padrão
ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

# Copia os arquivos de configuração personalizados
COPY custom-pg_hba.conf /tmp/custom-pg_hba.conf
COPY custom-postgresql.conf /tmp/custom-postgresql.conf