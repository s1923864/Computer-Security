import sys
import os

from common import *
from const import *

dialog = Dialog('print')
option = sys.argv[1][2:]
if option == "relay" :
    os.rename(BUFFER_DIR + BUFFER_FILE_NAME ,BUFFER_DIR + "Spoofing_buffer_unknown")
    socket_a, aes_a = setup("bob", BUFFER_DIR, "Spoofing_buffer_unknown")
    socket_b, aes_b = setup("alice", BUFFER_DIR, BUFFER_FILE_NAME)
    received = receive_and_decrypt(aes_b, socket_b)
    dialog.chat('Eavesdrop on Bob and Bob said: "{}"'.format(received))
    encrypt_and_send(received, aes_a, socket_a)
    received = receive_and_decrypt(aes_a, socket_a)
    dialog.chat('Eavesdrop on Alice and Alice said: "{}"'.format(received))
    encrypt_and_send(received, aes_b, socket_b)
    tear_down(socket_a, BUFFER_DIR, "Spoofing_buffer_unknown")
    tear_down(socket_b, BUFFER_DIR, BUFFER_FILE_NAME)

elif option == "break-heart" :
    os.rename(BUFFER_DIR + BUFFER_FILE_NAME ,BUFFER_DIR + "Spoofing_buffer_unknown")
    socket_a, aes_a = setup("bob", BUFFER_DIR, "Spoofing_buffer_unknown")
    socket_b, aes_b = setup("alice", BUFFER_DIR, BUFFER_FILE_NAME)
    received = receive_and_decrypt(aes_b, socket_b)
    dialog.chat('Eavesdrop on Bob and Bob said: "{}"'.format(received))
    to_send = "I hate you!"
    dialog.info("Waiting for sending spoofing message to Alice...")
    encrypt_and_send(to_send, aes_a, socket_a)
    dialog.info("Successfully send spoofing message to Alice...")
    received = receive_and_decrypt(aes_a, socket_a)
    dialog.chat('Eavesdrop on Alice and Alice said: "{}"'.format(received))
    to_send = "You broke my heart..."
    encrypt_and_send(to_send, aes_b, socket_b)
    tear_down(socket_a, BUFFER_DIR, "Spoofing_buffer_unknown")
    tear_down(socket_b, BUFFER_DIR, BUFFER_FILE_NAME)

elif option == "custom" :
    os.rename(BUFFER_DIR + BUFFER_FILE_NAME ,BUFFER_DIR + "Spoofing_buffer_unknown")
    socket_a, aes_a = setup("bob", BUFFER_DIR, "Spoofing_buffer_unknown")
    socket_b, aes_b = setup("alice", BUFFER_DIR, BUFFER_FILE_NAME)
    received = receive_and_decrypt(aes_b, socket_b)
    dialog.chat('Eavesdrop on Bob and Bob said: "{}"'.format(received))
    print("Please ENTER the spoofing message sent to Alice :")
    to_send = input()
    dialog.info("Waiting for sending spoofing message to Alice...")
    encrypt_and_send(to_send, aes_a, socket_a)
    dialog.info("Successfully send spoofing message to Alice...")
    received = receive_and_decrypt(aes_a, socket_a)
    dialog.chat('Eavesdrop on Alice and Alice said: "{}"'.format(received))
    print("Please ENTER the spoofing message sent to Bob :")
    to_send = input()
    dialog.info("Waiting for sending spoofing message to Bob...")
    encrypt_and_send(to_send, aes_b, socket_b)
    dialog.info("Successfully send spoofing message to Bob...")
    tear_down(socket_a, BUFFER_DIR, "Spoofing_buffer_unknown")
    tear_down(socket_b, BUFFER_DIR, BUFFER_FILE_NAME)
    
    

