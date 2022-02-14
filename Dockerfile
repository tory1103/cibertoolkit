FROM kalilinux/kali-rolling

ADD . /cibertoolkit

WORKDIR /cibertoolkit

RUN apt update
RUN bash install.sh -y

CMD ["toolkit"]