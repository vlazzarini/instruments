from pythonosc import osc_message_builder as mb
from pythonosc import udp_client as ud
import time

dest = ud.UDPClient("127.0.0.1",40000)

frs = [220., 130., 390., 660.]

def pack_and_send(dest,m):
  msg = mb.OscMessageBuilder(address=m[0])
  for i in m[1:]: msg.add_arg(i)
  dest.send(msg.build())
  print('Message sent: %r' % m)  
  
for i in  range(1,5):
    pack_and_send(dest,['/amp',i,1.])
    pack_and_send(dest,['/filter/cf',i,1.])
   
for i in  range(1,5):
   pack_and_send(dest,['/inst/on',i,frs[i-1],5000.])
   time.sleep(1)

for i in  range(1,5):
   pack_and_send(dest,['/filter/cf',i,3.0])
   time.sleep(1)

time.sleep(1)
pack_and_send(dest,['/pitch',4/3])
time.sleep(2)
pack_and_send(dest,['/pitch',1.])
time.sleep(1)

for i in  range(1,5):
   pack_and_send(dest,['/filter/cf',i,0.5])
   time.sleep(1)

for i in  range(1,5):
   pack_and_send(dest,['/inst/off',i])
   time.sleep(1)
   
