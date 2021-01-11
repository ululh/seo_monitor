FROM grafana/grafana

# load TLS certicate in container
COPY fullchain.pem /etc/grafana/
COPY privkey.pem /etc/grafana/

# configure https in grafana.ini
USER root
RUN mv /etc/grafana/grafana.ini /etc/grafana/grafana.ini.orig
RUN sed -e 's/^;protocol = .*$/protocol = https/' /etc/grafana/grafana.ini.orig | \
    sed -e 's/^;root_url = .*$/root_url = https:\/\/grafana.minederien.ulul.org/' | \
    sed -e 's/^;domain = .*$/domain = grafana.minederien.ulul.org/' | \
    sed -e 's/^# https certs & key file$/# https certs \& key file\ncert_file = \/etc\/grafana\/fullchain.pem\ncert_key = \/etc\/grafana\/privkey.pem/' \
    > /etc/grafana/grafana.ini

