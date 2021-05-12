import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = ""
        self.port = 5555
        self.addr = (self.server, self.port)
        self.d = self.connect()
        self.p = self.d[0]
        self.f = self.d[1]

    def getP(self):
        return self.p

    def getF(self):
        return self.f

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048*4))
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048*4))
        except socket.error as e:
            print(e)
