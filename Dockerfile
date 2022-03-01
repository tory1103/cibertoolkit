FROM kalilinux/kali-rolling

WORKDIR /cibertoolkit
COPY requirements.txt install.sh fresh-install.sh uninstall.sh config.sh update.sh ./
COPY src/ciber-toolkit/data/tools.json src/ciber-toolkit/data/tools.json
COPY src/ciber-toolkit/builtins src/ciber-toolkit/builtins

RUN bash install.sh -y

COPY . .

CMD toolkit