# Telnet Script Documentation

## Overview
This Python script (`telnet_script.py`) connects to a telnet server and sends bash commands to create a text file using the `vi` editor.

## Requirements
- Python 3.6 or higher
- A telnet server running on the target host and port

## Usage

### Basic Usage
Connect to the default host (127.0.0.1) and port (5555):
```bash
python3 telnet_script.py
```

### Custom Host and Port
Specify a custom host and/or port:
```bash
python3 telnet_script.py <host> <port>
```

Example:
```bash
python3 telnet_script.py 192.168.1.100 23
```

## What the Script Does

1. **Connects** to the telnet server at the specified host and port
2. **Opens vi editor** with the filename `test.txt`
3. **Enters insert mode** in vi (by pressing 'i')
4. **Writes generic content** to the file:
   - "Hello World!"
   - "This is a test file created via telnet."
   - "This file contains generic content for testing purposes."
   - "Python telnet script demonstration."
   - "End of file."
5. **Exits insert mode** (by pressing ESC)
6. **Saves and quits** vi (using `:wq`)
7. **Verifies file creation** by running `cat test.txt`
8. **Displays the output** from the server
9. **Closes the connection**

## Testing

To test the script, you need a telnet server running. You can set up a simple telnet server using:

### Option 1: Using Docker
```bash
docker run -d -p 5555:23 --name telnet-server alpine sh -c "apk add --no-cache busybox-extras && telnetd -F"
```

### Option 2: Using xinetd (on Linux)
Configure xinetd to run a telnet server on port 5555.

## Error Handling

The script includes error handling for common issues:
- **Connection refused**: The telnet server is not running or not accessible
- **Connection timeout**: Cannot reach the specified host
- **General exceptions**: Other unexpected errors

## Exit Codes
- `0`: Success
- `1`: Failure

## Notes
- The script uses the `socket` module instead of the deprecated `telnetlib` module
- Timing delays are included to ensure commands are processed correctly by the server
- The script is compatible with Python 3.12 and future versions
