#!/usr/bin/env python3
"""
Python script to connect to a telnet server and send bash commands.
This script connects to 127.0.0.1:5555 and creates a text file using vi.
"""

import socket
import time
import sys


def send_command_via_telnet(host="127.0.0.1", port=5555):
    """
    Connect to telnet server and send commands to create a file with vi.
    
    Args:
        host (str): The telnet host to connect to
        port (int): The telnet port to connect to
    """
    sock = None
    try:
        # Connect to the telnet server
        print(f"Connecting to {host}:{port}...")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        sock.connect((host, port))
        print("Connected successfully!")
        
        # Wait for the prompt
        time.sleep(1)
        
        # Send command to open vi with test.txt
        print("Opening vi editor with test.txt...")
        sock.sendall(b"vi test.txt\n")
        time.sleep(1)
        
        # Enter insert mode in vi
        print("Entering insert mode...")
        sock.sendall(b"i")
        time.sleep(0.5)
        
        # Write generic content to the file
        print("Writing content to file...")
        content = """Hello World!
This is a test file created via telnet.
This file contains generic content for testing purposes.
Python telnet script demonstration.
End of file.
"""
        sock.sendall(content.encode('utf-8'))
        time.sleep(0.5)
        
        # Exit insert mode (press ESC)
        print("Exiting insert mode...")
        sock.sendall(b"\x1b")  # ESC key
        time.sleep(0.5)
        
        # Save and quit vi (:wq)
        print("Saving and quitting vi...")
        sock.sendall(b":wq\n")
        time.sleep(1)
        
        # Verify the file was created
        print("Verifying file creation...")
        sock.sendall(b"cat test.txt\n")
        time.sleep(1)
        
        # Read the output
        try:
            output = sock.recv(4096).decode('utf-8', errors='ignore')
            if output:
                print("\nOutput from server:")
                print(output)
            else:
                print("\nNo output received from server (connection closed)")
        except socket.timeout:
            print("\nNo response received from server (timeout)")
        
        return True
        
    except ConnectionRefusedError:
        print(f"Error: Connection refused. Make sure the telnet server is running on {host}:{port}")
        return False
    except socket.timeout:
        print(f"Error: Connection timeout. Cannot reach {host}:{port}")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False
    finally:
        if sock:
            sock.close()
            print("\nConnection closed successfully!")


if __name__ == "__main__":
    # Allow custom host and port via command line arguments
    host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    
    try:
        port = int(sys.argv[2]) if len(sys.argv) > 2 else 5555
    except ValueError:
        print(f"Error: Invalid port number '{sys.argv[2]}'. Port must be an integer.")
        sys.exit(1)
    
    print("=" * 60)
    print("Telnet Script - Create File with Vi")
    print("=" * 60)
    
    success = send_command_via_telnet(host, port)
    
    if success:
        print("\n✓ Script completed successfully!")
        sys.exit(0)
    else:
        print("\n✗ Script failed!")
        sys.exit(1)
