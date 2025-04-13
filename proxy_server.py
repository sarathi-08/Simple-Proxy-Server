import socket
import threading

# Function to handle requests from clients and forward them to the server
def proxy_thread(conn, client_addr, server_addr, server_port):
    try:
        # Receive request from the browser
        request_from_browser = conn.recv(4096)
        
        # Decode the bytes received from the browser into a string
        request_from_browser = request_from_browser.decode('utf-8')

        # Extract the first line of the request (this contains the method and URL)
        first_line = request_from_browser.split('\n')[0]
        
        # Extract the URL from the first line
        url = first_line.split(' ')[1]
        print(f"URL Requested: {url}")

        # Create a socket to connect to the destination server
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.connect((server_addr, server_port))
        
        # Forward the browser request to the destination server
        server_socket.send(request_from_browser.encode('utf-8'))

        # Receive the response from the server and forward it to the client
        while True:
            response = server_socket.recv(4096)
            if len(response) > 0:
                # Send the server's response back to the browser
                conn.send(response)
            else:
                break

        # Close the connection to the server
        server_socket.close()

    except Exception as error_msg:
        print(f'ERROR: {client_addr} - {error_msg}')
    finally:
        # Close the connection to the client
        conn.close()

# Main function to set up the proxy server
def start_proxy(listen_addr, listen_port, server_addr, server_port):
    # Create a TCP socket to listen for incoming connections
    proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_socket.bind((listen_addr, listen_port))
    proxy_socket.listen(5)
    print(f"[*] Proxy server listening on {listen_addr}:{listen_port}")

    while True:
        # Accept incoming client connection
        conn, client_addr = proxy_socket.accept()
        print(f"[*] Connection received from {client_addr}")

        # Start a new thread to handle the request
        threading.Thread(target=proxy_thread, args=(conn, client_addr, server_addr, server_port)).start()

# Configuration settings
LISTEN_ADDR = '127.0.0.1'  # IP address of the proxy server
LISTEN_PORT = 8888          # Port the proxy server listens on
SERVER_ADDR = 'example.com'  # Destination server address (replace with your target server)
SERVER_PORT = 80            # Destination server port (usually 80 for HTTP)

if __name__ == "__main__":
    start_proxy(LISTEN_ADDR, LISTEN_PORT, SERVER_ADDR, SERVER_PORT)
