from scapy.all import *
import sys

import StringIO



class U_Sniffer():
    def __init__(self):
        self.u_iface = "eth0"
        self.u_filter = ""

    def start(self):
        
        #sniff(iface = self.u_iface,prn = lambda x: x.sprintf("{IP:%IP.src% -> %IP.dst%\n}"))
        pkt = sniff(count = 1)
        #pkt[0].show()
        if len(pkt[0].sprintf("{IP:%IP.proto%}")) != 0:
            return pkt[0].sprintf("{IP:%IP.proto%}:{IP:%IP.src%}>{IP:%IP.dst%}")
        else:
            return 0
        #return pkt[0].sprintf("{IP:%IP.proto%} Src : %src% {IP:%IP.src%} {TCP:%TCP.sport%}  -> Dst : %dst%  {IP:%IP.dst%} {TCP:%TCP.dport% } {Raw:%Raw.load%} ")
        '''
        #sniff(iface = self.u_iface, prn=lambda x: x.summary(),filter = self.u_filter,count=1)
        #sniff(iface = self.u_iface,prn = lambda x: x.sprintf("{IP:%IP.src% -> %IP.dst%\n}"))
        stdout = sys.stdout
        sys.stdout = f = StringIO.StringIO()
        sniff(iface = self.u_iface,filter = self.u_filter,prn=lambda x:x.summary(),count=1)
        sys.stdout = stdout
        s = f.getvalue()
        s = s.strip('\r\n')
        return s
        '''

if __name__ == "__main__":
    a=U_Sniffer()
    a.start()



