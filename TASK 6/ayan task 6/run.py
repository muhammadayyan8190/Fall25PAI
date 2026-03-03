#!/usr/bin/env python3
# Simple installer and runner script

import subprocess
import sys
import os

def print_header(text):
    print("\n" + "="*50)
    print(f"  {text}")
    print("="*50 + "\n")

def print_section(step, text):
    print(f"\n[{step}] {text}")
    print("-" * 50)

def check_python():
    """Check if Python is installed"""
    print_section("1/3", "Checking Python installation")
    result = subprocess.run([sys.executable, "--version"], capture_output=True, text=True)
    print(f"✓ Python {result.stdout.strip()}")
    return True

def install_requirements():
    """Install required packages"""
    print_section("2/3", "Installing dependencies")
    try:
        requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_path], check=True)
        print("✓ All dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("✗ Failed to install dependencies")
        return False

def run_flask():
    """Run Flask application"""
    print_section("3/3", "Starting Flask application")
    print("\n" + "="*50)
    print("  Server running at: http://localhost:5000")
    print("  Press Ctrl+C to stop the server")
    print("="*50 + "\n")
    
    try:
        subprocess.run([sys.executable, "app.py"], check=True)
    except KeyboardInterrupt:
        print("\n\n✓ Server stopped")
    except Exception as e:
        print(f"✗ Error running Flask: {e}")

def main():
    print_header("Object Counter - Video Analysis")
    
    try:
        if not check_python():
            sys.exit(1)
        
        if not install_requirements():
            sys.exit(1)
        
        run_flask()
    
    except KeyboardInterrupt:
        print("\n\n✗ Installation cancelled")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
