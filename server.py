#!/usr/bin/env python3
"""
Static file server for the Subscrypts docs site.

Replaces `python -m http.server` to log the real client IP when running
behind a reverse proxy chain (Cloudflare → nginx → this container).

IP resolution order:
  1. First entry of X-Forwarded-For  (real client IP set by Cloudflare/nginx)
  2. X-Real-IP                        (direct connecting IP to nginx)
  3. TCP remote address               (fallback: the proxy's own IP)
"""

import http.server
import os
import sys


class ProxyAwareHandler(http.server.SimpleHTTPRequestHandler):

    def address_string(self):
        """Return the real client IP for log output."""
        xff = self.headers.get("X-Forwarded-For", "")
        if xff:
            # X-Forwarded-For: <client>, <proxy1>, <proxy2>
            # The left-most entry is the original client IP.
            return xff.split(",")[0].strip()

        real_ip = self.headers.get("X-Real-IP", "")
        if real_ip:
            return real_ip.strip()

        return self.client_address[0]

    def log_message(self, fmt, *args):
        """Keep the standard Combined Log Format, just with the real IP."""
        sys.stderr.write(
            "%s - - [%s] %s\n"
            % (self.address_string(), self.log_date_time_string(), fmt % args)
        )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    server = http.server.HTTPServer(("", port), ProxyAwareHandler)
    sys.stderr.write(f"Serving on port {port}\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
