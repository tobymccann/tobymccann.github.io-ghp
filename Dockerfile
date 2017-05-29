FROM python:3.6.1-slim
MAINTAINER tobymccann <jason@kennemers.com@>

# Install dependencies
RUN sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list \
  && apt-get update \
  && apt-get -y upgrade \
  && apt-get install \
  make \
  git \
  tex-common \
  texlive \
  pandoc -y \
  && pip install pelican Markdown typogrify ghp-import \
  && pip install --upgrade pelican Markdown typogrify ghp-import

RUN git clone https://github.com/getpelican/pelican-plugins /site/

WORKDIR /site
# Need to mount /site/content
CMD pelican content/ -o output/ -s publishconf.py