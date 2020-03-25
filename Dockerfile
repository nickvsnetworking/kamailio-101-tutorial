#Kamailio Test Stuff
FROM kamailio/kamailio:5.3.3-stretch

#Copy the config file onto the Filesystem of the Docker instance
COPY kamailio.cfg /etc/kamailio/

#Print out the current IP Address info
RUN ip add

#Expose port 5060 (SIP) for TCP and UDP
EXPOSE 5060
EXPOSE 5060/udp
