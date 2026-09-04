#!/usr/bin/env python3
"""
SIH 2024 Problem Statement ID 26044:
"Portal for Academia - Industry collaboration for Skill Mapping, Internships and Placement"
Organization: Ministry of Ayush / Department: All India Institute of Ayurveda
Theme: Smart Automation

Unified Full-Stack Runner
"""
import os
import sys
import subprocess
import socket

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
BACKEND_DIR = os.path.join(BASE_DIR, 'backend')
FRONTEND_DIR = os.path.join(BASE_DIR, 'frontend')

def find_available_port(start_port=5000):
    """Find an available port starting from start_port"""
    port = start_port
    while port < 6000:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('127.0.0.1', port))
                return port
        except OSError:
            port += 1
    return start_port

def main():
    print("=" * 70)
    print("🌿 SIH Problem Statement ID: 26044")
    print("   Portal for Academia - Industry Collaboration")
    print("   Ministry of Ayush • All India Institute of Ayurveda")
    print("=" * 70)
    
    # Ensure backend venv or python path
    sys.path.insert(0, BACKEND_DIR)
    
    try:
        from app import create_app
        from models import db, User
    except ImportError as e:
        print(f"Error importing Flask backend modules: {e}")
        print("Please activate the backend virtual environment: source backend/venv/bin/activate")
        sys.exit(1)
        
    app = create_app()
    port = int(os.getenv('PORT', find_available_port()))
    
    print(f"\n🚀 Server running at: http://127.0.0.1:{port}")
    print("👉 Frontend SPA & REST API are served together from this endpoint.")
    print("👉 For live frontend Vite development: cd frontend && npm run dev\n")
    
    app.run(host='0.0.0.0', port=port, debug=True)

if __name__ == '__main__':
    main()
