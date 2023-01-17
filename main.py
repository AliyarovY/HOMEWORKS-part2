import socket


for _ in iter(bool, 111):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.bind(('127.0.0.1', 2000))
            sock.listen(0)
            cl, _ = sock.accept()
            hdrs = b'HTTP/1.1 200 OK\r\nContent-Type: text/html; chrset=utf-8\r\n\r\n'
            cl.send(hdrs + 'Hello, World wide web!'.encode('utf-8'))
        except:
            continue
        finally:
            cl.shutdown(socket.SHUT_WR)
