from coapthon.server.coap import CoAP
from coapthon.resources.resource import Resource
#from dbhandler import DataBase

class GpsFlowTempResource(Resource):
  def __init__(self, name="gpsflowtemp", coap_server=None):
     super(GpsFlowTempResource, self).__init__(name, coap_server,visible=True,observable=True,allow_children=True)
     self.payload = None
     #self.dbhandler = DataBase()
     #self.dbhandler.connect_db()
  def render_GET(self, request):
     return self

  def render_PUT(self, request):
     return self

  def render_POST(self, request):
   res = self.init_resource(request, GpsFlowTempResource())
   res.location_query = request.uri_query
   res.payload = request.payload
   print("\n"+res.payload)
   #self.dbhandler.on_message(request.payload)
   print("armazenou no banco os dados:"+"\n")
   
   return res
  def render_DELETE(self, request):
   return True
