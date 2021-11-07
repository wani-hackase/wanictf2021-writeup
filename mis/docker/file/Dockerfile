FROM alpine:3.14
WORKDIR /home/misc
ADD ./solver /home/misc/solver
RUN chmod 550 /home/misc/solver
RUN apk add libc6-compat
RUN ls /home/misc -lh
