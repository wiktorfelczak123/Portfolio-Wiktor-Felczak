"""Local in-memory API mock for the portfolio API/UAT example."""
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json
import re
import uuid

HOST, PORT = "127.0.0.1", 4010
deliveries = {}
references = set()

def response(handler, status, payload):
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.send_header("Access-Control-Allow-Origin", "*")
    handler.end_headers()
    handler.wfile.write(body)

class ApiHandler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        print("%s - %s" % (self.address_string(), fmt % args))

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/health":
            return response(self, 200, {"status": "ok"})
        match = re.fullmatch(r"/api/v1/deliveries/([A-Za-z0-9-]+)", path)
        if match:
            item = deliveries.get(match.group(1))
            if item is None:
                return response(self, 404, {"error": {"code": "NOT_FOUND", "message": "Delivery not found"}})
            return response(self, 200, item)
        return response(self, 404, {"error": {"code": "NOT_FOUND", "message": "Route not found"}})

    def do_POST(self):
        if urlparse(self.path).path != "/api/v1/deliveries":
            return response(self, 404, {"error": {"code": "NOT_FOUND", "message": "Route not found"}})
        try:
            length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
        except (ValueError, UnicodeDecodeError, json.JSONDecodeError):
            return response(self, 400, {"error": {"code": "INVALID_JSON", "message": "Request body must be valid JSON"}})

        registration = payload.get("vehicle_registration") if isinstance(payload, dict) else None
        reference = payload.get("client_reference") if isinstance(payload, dict) else None
        volume = payload.get("volume_m3") if isinstance(payload, dict) else None
        customer = payload.get("customer_id") if isinstance(payload, dict) else None
        errors = []
        if not isinstance(registration, str) or not registration.strip():
            errors.append("vehicle_registration is required")
        if not isinstance(reference, str) or not reference.strip():
            errors.append("client_reference is required")
        if not isinstance(customer, str) or not customer.strip():
            errors.append("customer_id is required")
        if isinstance(volume, bool) or not isinstance(volume, (int, float)) or volume <= 0:
            errors.append("volume_m3 must be a positive number")
        if errors:
            return response(self, 400, {"error": {"code": "VALIDATION_ERROR", "message": "Request validation failed", "details": errors}})
        if reference in references:
            return response(self, 409, {"error": {"code": "DUPLICATE_REFERENCE", "message": "client_reference already exists"}})

        delivery_id = str(uuid.uuid4())
        item = {
            "id": delivery_id,
            "vehicle_registration": registration.strip().upper(),
            "client_reference": reference.strip(),
            "customer_id": customer.strip(),
            "volume_m3": float(volume),
            "status": "accepted",
        }
        deliveries[delivery_id] = item
        references.add(reference)
        return response(self, 201, item)

if __name__ == "__main__":
    print(f"Portfolio mock API listening on http://{HOST}:{PORT}")
    HTTPServer((HOST, PORT), ApiHandler).serve_forever()
