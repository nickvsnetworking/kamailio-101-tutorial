## Kamailio - equivalent of routing blocks in Python
import sys
import Router.Logger as Logger
import KSR as KSR

import requests
import sys
# global function to instantiate a kamailio class object
# -- executed when kamailio app_python module is initialized
def mod_init():
    KSR.info("===== from Python mod init\n");
    return kamailio();


# -- {start defining kamailio class}
class kamailio:
    def __init__(self):
        KSR.info('===== kamailio.__init__\n');


    # executed when kamailio child processes are initialized
    def child_init(self, rank):
        KSR.info('===== kamailio.child_init(%d)\n' % rank);
        return 0;


    # SIP request routing
    # -- equivalent of request_route{}
    def ksr_request_route(self, msg):

        KSR.dbg("method " + KSR.pv.get("$rm") + " r-uri " + KSR.pv.get("$ru"))


        if KSR.is_method("REGISTER"):
            KSR.sl.send_reply(200, "OK")

        elif KSR.is_method("INVITE"):
                #Lookup our public IP address
                try:
                    ip = requests.get('https://api.ipify.org').text
                except:
                    ip = "Failed to resolve"

                #Add that as a header
                KSR.hdr.append("X-KEMI: I came from KEMI at " + str(ip) + "\r\n");

                #Set host IP to 10.1.1.1
                KSR.sethost("10.1.1.1");

                #Forward the request on
                KSR.forward()
        else:
               KSR.sl.send_reply(500, "Got no idea...")
