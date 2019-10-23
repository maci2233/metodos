from random import randint

class Client: #Clase del cliente

    def __init__(self, num, tiempo_llegada, cliente_anterior=None): #Clase cliente recibe como parametro num que es el numero de cliente que se le asigna
        self.num = num #Aqui se le asigna el numero de cliente que es
        self.tiempo_tramite = tiempo_lim(10) #Aqui se genera un número random del 1 al 10 que dicta cuanto tiempo va a durar en la caja
        self.tiempo_entre_llegada = tiempo_llegada
        if cliente_anterior is None: #Si el cliente es el primero
            self.hora_llegada = 900 #Definir hora de llegada como las 9:00
            self.inicia_servicio = self.hora_llegada
            self.termina_servicio = self.hora_llegada + self.tiempo_tramite
        else:
            self.hora_llegada = cliente_anterior.hora_llegada + self.tiempo_entre_llegada

    def calcula_tiempos(self, cliente_cajero):
        pass

def tiempo_lim(tiempo_max): #Aqui se define el tiempo que va a durar el cliente
    return randint(1, tiempo_max) #Regresar el número aleatorio de 1 al tiempo_max definido


if __name__ == '__main__': #Buenas practicas de Main
    N = int(input('Ingresa el numero de clientes: ')) #Aqui el usuario va a introducir el numero de clientes que quiere
    lista_clientes = [Client(num=1, tiempo_llegada=0, cliente_anterior=None)]
    for i in range(1, N):
        lista_clientes.append(Client(num=i+1, tiempo_llegada=tiempo_lim(10), cliente_anterior=lista_clientes[i-1]))
    #num_cajeros = int(input('Ingresa el numero de cajeros: ')) #Aqui el usuario introduce el numero de cajeros que quiere
    num_cajeros = 2 #Aqui se define el numero de cajeros
    lista_clientes = list() #Generar un arreglo de lista de clientes
    lista_termina_servicio = [900 for _ in range(num_cajeros)] #Definimos una lista de termina servicio
    lista_cliente_cajero = [None for _ in range(num_cajeros)] #Definimos una lista de cajeros que estan atendiendo a un cliente
    for i in range(N): #Para que recorrre todos los clientes
        client = client[i]
        if i == 0: #Si es el primer cliente el que entra al banco
            lista_termina_servicio[0] += client.tiempo_tramite
            lista_cliente_cajero[0] = client
        else:
            for i in range(num_cajeros):
                if  lista_cliente_cajero[i] is None: #Busca un cajero vacío
                    lista_termina_servicio[i] += client.hora_llegada + client.tiempo_tramite
                    lista_cliente_cajero[i] = client
                    break
            else: #A ESTE ELSE SE ENTRA CUANDO NINGUN CAJERO ESTA VACÍO
                min_ind = index(min(lista_termina_servicio))


    #fila_espera.append() #Agreaga al valor al final de la list (el valor que esté hasta la derecha)
    #fila_espera.popleft() #popleft elimina el primer valor de la lista (el valor que esté hasta la izquierda)
