from pythonosc import osc_message_builder as mb
from pythonosc import udp_client as ud
import time

dest = ud.UDPClient("127.0.0.1",5510)

pars = [(220.,0.1,0.8),
        (261.,0.2,0.6),
        (330.,0.4,0.4),
        (440.,0.8,0.3)]

def pack_and_send(dest,m):
  msg = mb.OscMessageBuilder(address=m[0])
  for i in m[1:]: msg.add_arg(i)
  dest.send(msg.build())
  print('Message sent: %r' % m)  
  
for i in pars:
    pack_and_send(dest,['/nblsum/freq',i[0]])
    pack_and_send(dest,['/nblsum/amp',i[1]])
    pack_and_send(dest,['/nblsum/a',i[2]])
    time.sleep(1.5)
   


   
