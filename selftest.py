"""Local tester for server.py and client.py - not the hidden grader.

    python3 selftest.py

Starts your server.py in the background, calls contact_server on it and prints the answer.
"""
import os
import subprocess
import sys
import time

HOST = "127.0.0.1"
PORT = 2405


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    server = subprocess.Popen([sys.executable, os.path.join(here, "server.py")], cwd=here)
    try:
        time.sleep(1)
        sys.path.insert(0, here)
        from client import contact_server

        answer = contact_server(HOST, PORT)
        print("the server answered:", repr(answer))
        print("OK" if answer == "Kululu" else 'expected "Kululu"')
    finally:
        server.kill()


if __name__ == "__main__":
    main()
