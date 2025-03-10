FROM rockylinux:8

ARG USERNAME=dicomsorter
ARG GROUP=dicomsorter
ARG UID=${UID}
ARG GID=${GID}
ARG DICOMSORTER_LOG_FILE=${DICOMSORTER_LOG_FILE}

RUN groupadd -g ${GID} ${GROUP}
RUN useradd ${USERNAME} -u ${UID} -g ${GID} -m -s /bin/bash

# install some things
RUN dnf install -y git vim procps findutils cronie

# install miniforge
ARG MFG_PREFIX="/sw/miniforge"
WORKDIR "/tmp"
RUN curl -sL "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh" -o "miniforge.sh"
RUN bash "miniforge.sh" -b -p "${MFG_PREFIX}"
RUN rm "miniforge.sh"
ENV PATH="${MFG_PREFIX}/bin:${PATH}"

# install dicomsorter
RUN mamba create -y --name=dicomsorter python=3.13
ARG VERSION="rename"
RUN mamba run --name dicomsorter --no-capture-output python3 -m pip install "git+https://github.com/harvard-nrg/dicomsorter.git@${VERSION}"

# install crontab file
COPY --chown=${USERNAME}:${GROUP} --chmod=600 ./crontab/dicomsorter /var/spool/cron/${USERNAME}

RUN echo "DICOMSORTER_LOG_FILE=${DICOMSORTER_LOG_FILE}" >> /etc/environment

# twiddle things for a non-root user to run crond
RUN chmod o+rx /var/spool/cron && \
    chmod u+s /usr/sbin/crond && \
    chmod o+rwx /var/run

CMD ["/usr/sbin/crond", "-n"]
