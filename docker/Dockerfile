FROM ubuntu:jammy

# install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    gcc && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /opt/requirements.txt
RUN pip3 install -r /opt/requirements.txt

# Build application
COPY src /opt/src
COPY binding_cpp_root /opt/binding_cpp_root

COPY docker/build_binding.sh /opt/build_binding.sh
RUN chmod +x /opt/build_binding.sh && /opt/build_binding.sh

# Run main
COPY docker/entrypoint.sh /opt/entrypoint.sh
RUN chmod +x /opt/entrypoint.sh && chmod +x /opt/binding_cpp_root/build/bin/binding
CMD /opt/entrypoint.sh
