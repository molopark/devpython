import http.server

HTTPHandler = http.server.SimpleHTTPRequestHandler


HTTPHandler.extensions_map.update({
    '.m3u8':'application/x-xmpegURL',
    '.ts':'video/MP2T'
})

httpd = http.server.HTTPServer(('127.0.0.1',8888),HTTPHandler)
httpd.serve_forever()
