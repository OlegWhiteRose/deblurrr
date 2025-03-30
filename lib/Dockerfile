FROM ubuntu:latest

WORKDIR /mydir

COPY . .

EXPOSE 4444

RUN apt update && \
    apt install -y python3 python3.12-venv && \
    python3 -m venv venv && \
    . venv/bin/activate && \
    chmod u+x build.sh && \
    ./build.sh setup_root

