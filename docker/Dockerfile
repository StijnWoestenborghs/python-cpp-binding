FROM ubuntu:jammy

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    gcc && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /opt/requirements.txt
RUN pip3 install -r /opt/requirements.txt

# Coppy application
COPY src /opt/src
COPY binding_cpp_root /opt/binding_cpp_root

# Build & Run main
COPY docker/entrypoint.sh /opt/entrypoint.sh
RUN chmod +x /opt/entrypoint.sh
CMD /opt/entrypoint.sh
