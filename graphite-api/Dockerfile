FROM brutasse/graphite-api

ADD . /build
WORKDIR /build
RUN python setup.py sdist
RUN pip install dist/metronome-graphite-finder*.tar.gz
RUN pip install requests futures
