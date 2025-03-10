FROM rockylinux:8

ARG USERNAME=rossbuddy
ARG GROUP=rossbuddy
ARG UID=${UID}
ARG GID=${GID}

# create user
RUN groupadd -g ${GID} ${GROUP}
RUN useradd ${USERNAME} -u ${UID} -g ${GID} -m -s /bin/bash

# install some things
RUN dnf install -y git vim telnet procps findutils epel-release
RUN dnf install -y dcmtk supervisor sendmail
RUN pip3 install superlance

RUN mkdir /var/run/supervisord && chown ${USERNAME}:${GROUP} /var/run/supervisord

COPY --chmod=644 ./supervisor/storescp.ini /etc/supervisord.d/storescp.ini
COPY --chmod=644 ./supervisor/supervisord.conf /etc/supervisord.conf
COPY --chmod=755 ./scripts/slack.py /usr/bin/slack.py

RUN chmod o+rwx /run /var/run

CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]
