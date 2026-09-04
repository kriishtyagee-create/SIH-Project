import os, sys, socket

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))
from app import create_app

def find_available_port(start_port=5000):
    for port in range(start_port, 6000):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('127.0.0.1', port))
                return port
        except OSError:
            continue
    return start_port

if __name__ == '__main__':
    port = int(os.getenv('PORT', find_available_port()))
    print(f"🚀 Server running at: http://127.0.0.1:{port}")
    create_app().run(host='0.0.0.0', port=port, debug=True)
