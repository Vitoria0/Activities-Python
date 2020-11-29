class computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    pass

    def ligar(self):
        print('O computador está ligando...')

    def desligar(self):
        print('O computador está desligando...')

    def inf(self):
        print(self.marca, self.memoria_ram, self.placa_de_video, sep= ' - ')


marca = input('Marca do pc: ')
memoria_ram = input('Memoria: ')
placa_de_video = input('Placa de video: ')

computador1 = computador(marca, memoria_ram, placa_de_video)
computador1.ligar()
computador1.inf()
computador1.desligar()
