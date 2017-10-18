import sys
from oekit import oe_client_env
import xmlrpclib

envclient = oe_client_env.OEClientEnv()

if len(sys.argv) > 1 and sys.argv[1] == 'erppeek':
    oe = envclient.get_erppeek_client()
else:
    oe = envclient.get_proxy()

def ckfault(function, *args, **kwargs):
    try:
        return function(*args, **kwargs)
    except xmlrpclib.Fault, exc:
        sys.stderr.write('Fault code: %s\nFault string:%s\n' % (exc.faultCode, exc.faultString))
        raise exc

sys.stderr.write("Proxy set up with name 'oe'\n")
