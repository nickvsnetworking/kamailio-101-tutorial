#Kamailio Test Stuff
FROM kamailio/kamailio:5.3.3-stretch

COPY kamailio.cfg /etc/kamailio/

RUN ip add

EXPOSE 5060
