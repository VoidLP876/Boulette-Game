import pygame
from pygame.locals import *
import socket
import pickle


# Fonction pour envoyer des données sur le réseau
def send_data(data, server_address):
    # Créez un socket UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Sérialisez les données à l'aide de pickle avant de les envoyer
    serialized_data = pickle.dumps(data)

    # Envoyer les données sur le réseau
    client_socket.sendto(serialized_data, server_address)


# Fonction pour recevoir des données du réseau
def receive_data(server_address):
    # Créez un socket UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Liez le socket à l'adresse du serveur
    server_socket.bind(server_address)

    # Définir un délai d'attente pour la réception de données (en secondes)
    server_socket.settimeout(0.001)

    try:
        # Essayez de recevoir des données du réseau
        serialized_data, client_address = server_socket.recvfrom(1024)

        # Désérialisez les données à l'aide de pickle pour les convertir en objet Python
        data = pickle.loads(serialized_data)
        return data
    except socket.timeout:
        # Si aucune donnée n'est reçue dans le délai imparti, retournez None
        return None


# Fonction pour obtenir les adresses IP des autres joueurs
def get_player_addresses():
    player_addresses = []
    num_players = 4  # Vous pouvez ajuster le nombre de joueurs selon vos besoins

    for i in range(num_players):
        player_address = input(f"Entrez l'adresse IP du joueur {i + 1}: ")
        player_addresses.append((player_address,
                                 12345))  # Utilisation du port 12345 pour tous les joueurs (vous pouvez changer cela si nécessaire)

    return player_addresses


# Fonction principale du jeu
def main():
    # Demander les adresses IP des autres joueurs
    player_addresses = get_player_addresses()

    pygame.display.set_caption("Pong 4 joueurs en réseau LAN")

    # Récupérer les entrées des joueurs distants
    for i in range(len(player_addresses)):
        data = receive_data(player_addresses[i])
        if data is not None:
            paddles[i].move(data)

    # Récupérer les entrées des joueurs locaux
    keys = pygame.key.get_pressed()
    paddles[0].move(paddles[0].rect.y - 5 if keys[K_w] else paddles[0].rect.y)
    paddles[1].move(paddles[1].rect.y - 5 if keys[K_UP] else paddles[1].rect.y)
    paddles[2].move(paddles[2].rect.x - 5 if keys[K_a] else paddles[2].rect.x)
    paddles[3].move(paddles[3].rect.x - 5 if keys[K_LEFT] else paddles[3].rect.x)

    # Mettre à jour la position de la balle
    ball.move()

    # Gestion des collisions entre la balle et les paddles
    for paddle in paddles:
        if paddle.rect.colliderect(ball.rect):
            ball.dx = -ball.dx

    # Dessiner tout sur l'écran

    # Envoyer les positions des paddles aux autres joueurs
    paddle_positions = [paddle.rect.y for paddle in paddles]
    for i in range(len(player_addresses)):
        send_data(paddle_positions[i], player_addresses[i])

