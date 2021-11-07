FROM python:3.9-buster

RUN apt update -q && apt upgrade -q -y && \
    apt install --no-install-recommends -q -y \
        # 日本語環境
	    locales \
        # chromiumに必要なもの
        libasound2 libatk-bridge2.0-0 libatk1.0-0 libatspi2.0-0 libcairo2 libcups2 libdbus-1-3 \
        libdrm2 libgbm1 libglib2.0-0 libnspr4 libnss3 libpango-1.0-0 libx11-6 libxcb1 \
        libxcomposite1 libxdamage1 libxext6 libxfixes3 libxkbcommon0 libxrandr2 libxshmfence1 && \
    # language / timezone settings
    locale-gen ja_JP.UTF-8 && \
    dpkg-reconfigure locales && \
    ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    echo "Asia/Tokyo" > /etc/timezone && \
    apt clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install -U pip

ENV LC_ALL ja_JP.UTF-8
ENV LC_MESSAGES ja_JP.UTF-8
ENV LC_IDENTIFICATION ja_JP.UTF-8
ENV LC_COLLATE ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LC_MEASUREMENT ja_JP.UTF-8
ENV LC_CTYPE ja_JP.UTF-8
ENV LC_TIME ja_JP.UTF-8
ENV LC_NAME ja_JP.UTF-8

RUN localedef -f UTF-8 -i ja_JP ja_JP.utf8

# Initial Running Script
COPY run.sh /run.sh

CMD ["/bin/sh", "/run.sh"]