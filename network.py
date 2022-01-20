import socket
import pickle



class Network:
    def __init__(self):
        self.client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "26.96.216.85"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client1.connect(self.addr)
            return pickle.loads(self.client1.recv(2048))
        except:
            pass

    def send(self, data):
        try:
            self.client1.send(pickle.dumps(data))
            return pickle.loads(self.client1.recv(2048))
        except socket.error as e:
            print(e)
            




