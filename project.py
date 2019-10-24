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


def tiempo_lim(tiempo_max): #Aqui se define el tiempo que va a durar el cliente
    return randint(1, tiempo_max) #Regresar el número aleatorio de 1 al tiempo_max definido


def resultados(clientes):
    with open("results.csv", "w") as f:
        f.write("Cliente, Num Cajero, Tiempo entre llegadas, Hora de llegada, Tiempo del trámite, Inicia Servicio, Termina Servicio, Tiempo de Espera Cliente")
        #para cada cajero
        #hay que agregar su Tiempo espera ATMi en el header
        f.write("\n")
        for client in clientes:
            f.write("{}, {}, {}, {}, {}, {}, {}, {}\n".format(client.num, client.num_cajero, client.tiempo_entre_llegada, client.hora_llegada, client.tiempo_tramite, client.inicia_servicio, client.termina_servicio,) client.tiempo_espera))
            #para cada cajero hay que agregar su inactividad cuando llega x cliente

def actualiza_tiempos_inactividad(inicia_servicio)
    for i in range(num_cajeros):
        if inicia_servicio > lista_termina_servicio[i]:
            lista_inactividad_cajero[i] = inicia_servicio - lista_termina_servicio[i]
        else:
            lista_termina_servicio[i] = 0


'''
[905, 913, 900]
[[0, 0, 5], [0, 3, 0], [0, 3, 10]]

1: 900, 5, 905
2: 903, 10, 913
3: 910, 5, 915
'''

if __name__ == '__main__': #Buenas practicas de Main
    N = int(input('Ingresa el numero de clientes: ')) #Aqui el usuario va a introducir el numero de clientes que quiere
    lista_clientes = [Client(num=1, tiempo_llegada=0, cliente_anterior=None)]
    for i in range(1, N):
        lista_clientes.append(Client(num=i+1, tiempo_llegada=tiempo_lim(10), cliente_anterior=lista_clientes[i-1]))
    #num_cajeros = int(input('Ingresa el numero de cajeros: ')) #Aqui el usuario introduce el numero de cajeros que quiere
    num_cajeros = int(input('Ingresa el numero de Cajeros: ')) #Aqui se define el numero de cajeros
    #lista_clientes = list() #Generar un arreglo de lista de clientes
    lista_termina_servicio = [900 for _ in range(num_cajeros)] #Definimos una lista de termina servicio
    lista_cliente_cajero = [None for _ in range(num_cajeros)] #Definimos una lista de cajeros que estan atendiendo a un cliente
    lista_inactividad_cajero = [[] for _ in range(num_cajeros)] #Cada arreglo hace referencia a los tiempos de inactividad de un cajero
    for i in range(N): #Para que recorra todos los clientes, i es clientes
        if i == 0: #Si es el primer cliente el que entra al banco
            lista_termina_servicio[0] += lista_clientes[i].tiempo_tramite
            lista_cliente_cajero[0] = lista_clientes[i]
            lista_clientes[i].tiempo_espera = 0
            lista_clientes[i].num_cajero = 1
        else:
            for j in range(num_cajeros): #j es para cajeros
                if lista_cliente_cajero[j] is None: #Busca un cajero vacío
                    lista_clientes[i].inicia_servicio = lista_clientes[i].hora_llegada
                    lista_clientes[i].termina_servicio = lista_clientes[i].inicia_servicio + lista_clientes[i].tiempo_tramite
                    lista_clientes[i].tiempo_espera = 0
                    lista_clientes[i].num_cajero = j+1
                    #Tiempo de espera cliente = 0
                    #Tiempo de inactividad atm = client.inicia_servicio - lista_termina_servicio[i]
                    actualiza_tiempos_inactividad(lista_clientes[i].inicia_servicio)
                    lista_termina_servicio[j] = lista_clientes[i].hora_llegada + lista_clientes[i].tiempo_tramite #Actualizar el termina servicio del cajero
                    lista_cliente_cajero[j] = lista_clientes[i] #esto pa qué era?
                    break
            else: #A ESTE ELSE SE ENTRA CUANDO NINGUN CAJERO ESTA VACÍO
                min_ind = lista_termina_servicio.index(min(lista_termina_servicio)) #regresa el index del cajero que tenga la hora de termina serivicio más pequeña
                lista_clientes[i].num_cajero = min_ind+1
                if lista_clientes[i].hora_llegada < lista_termina_servicio[min_ind]:
                    lista_clientes[i].inicia_servicio = lista_termina_servicio[min_ind]
                    actualiza_tiempos_inactividad(lista_clientes[i].inicia_servicio)
                    lista_clientes[i].termina_servicio = lista_clientes[i].inicia_servicio + lista_clientes[i].tiempo_tramite
                    lista_clientes[i].tiempo_espera = lista_termina_servicio[min_ind] - lista_clientes[i].hora_llegada
                    #Tiempo de espera cliente = lista_termina_servicio[min_ind] - client.hora_llegada
                    #Tiempo de inactividad atm = 0
                else:
                    lista_clientes[i].inicia_servicio = lista_clientes[i].hora_llegada
                    actualiza_tiempos_inactividad(lista_clientes[i].inicia_servicio)
                    lista_clientes[i].termina_servicio = lista_clientes[i].inicia_servicio + lista_clientes[i].tiempo_tramite
                    lista_clientes[i].tiempo_espera = 0
                    #Tiempo de espera cliente = 0
                    #Tiempo de inactividad atm = client.inicia_servicio - lista_termina_servicio[min_ind]
                lista_termina_servicio[min_ind] = lista_clientes[i].termina_servicio
                lista_cliente_cajero[min_ind] = lista_clientes[i]
    resultados(lista_clientes)



    #fila_espera.append() #Agrega al valor al final de la list (el valor que esté hasta la derecha)
    #fila_espera.popleft() #popleft elimina el primer valor de la lista (el valor que esté hasta la izquierda)
