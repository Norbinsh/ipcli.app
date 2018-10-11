from flask import Flask, request
from os import environ

app = Flask(__name__)

TEMPLATE = '''
/----------------------------------------\\
| {ip:39}|
|                                        |
| Created by Yuval Adam                  |
| https://github.com/yuvadm/ipcli.app    |
| Comments welcome at hello@ipcli.app    |
\\----------------------------------------/
'''

def get_ip(request):
    if 'PROD' in environ:
        # Routing layers and proxies along the way might mask the original IP
        # So fetch it from the custom header
        # And make sure we just take the first (source) IP address
        ips = request.headers.get('X-Forwarded-For')
        return ips.split(',')[0]
    else:
        return request.remote_addr

@app.route('/')
def index():
    ip = get_ip(request)
    return TEMPLATE.format(ip=ip)

@app.route('/p')
def plain():
    return get_ip(request)
