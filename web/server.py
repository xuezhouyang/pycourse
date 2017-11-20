import http.server
import socketserver
import io,sys
from sqlalchemy import *

engine = create_engine( 'mysql+mysqlconnector://xxxxxxx:xxxxxx@xxxxxxxxxx:0000/xxxxxxx' )

result = engine.execute(
    "SELECT * FROM warranties WHERE id BETWEEN %(start)s AND %(end)s",
    start=400000, end=405000
)
ret = result.fetchall()
warranties = []
for item in ret:
    line = ''
    item = item[:4]
    for cell in item:
        line = line + '<td>' + str(cell) + '<td>'
    warranties.append('<tr>' + line + '</tr>')

warrantiess = '\n'.join(warranties)

html = '''
        <!DOCTYPE>
        <html>
        <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>
        这里是标题
        </title>
        </head>
        <body>
        <table>
        <tbody>
        realbody
        </tbody>
        </table>
        </body>
        </html>
        '''.replace('realbody', warrantiess)

PORT = 8000

class HttpDemoHandle(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        enc = sys.getfilesystemencoding()
        encoded = html.encode(enc, 'surrogateescape')
        f = io.BytesIO()
        f.write(encoded)
        f.seek(0)
        self.send_response(http.server.HTTPStatus.OK)
        self.send_header("Content-type", "text/html; charset=%s" % enc)
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        if f:
            try:
                self.copyfile(f, self.wfile)
            finally:
                f.close()

Handler = HttpDemoHandle

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()