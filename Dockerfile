FROM odoo:18.0

USER root
COPY ./addons /mnt/extra-addons
COPY ./requirements.txt /mnt/requirements.txt
RUN pip3 install -r /mnt/requirements.txt --break-system-packages

USER odoo