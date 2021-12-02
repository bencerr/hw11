"""
CSCI-141: Homework 11
file: cbc_mode.py
language: python3
author: Ben Cerrone
"""


import encryption
import linked_list_type
import mutable_list


def cbc_mode_encryption(plaintext, IV, key):
    """
    purpose: encrypt the plaintext using cbc
    :param plaintext: linked list
    :param IV: python list
    :param key: python list
    :return: linked list
    """

    ll = linked_list_type.make_empty_list()

    current = plaintext.head

    element = encryption.encryption(encryption.xor_gate(current.value, IV), key)
    ll.head = linked_list_type.MutableNode(element, None)
    ll.size += 1

    current = current.next
    prev_element = element
    prev_node = ll.head

    while current is not None:
        element = encryption.encryption(encryption.xor_gate(current.value, prev_element), key)
        node = linked_list_type.MutableNode(element, None)
        prev_node.next = node

        ll.size += 1
        prev_element = element
        current = current.next
        prev_node = node

    return ll


def cbc_mode_decryption(ciphertext, IV, key):
    """
    purpose: decrypt the ciphertext using cbc
    :param ciphertext: linked list
    :param IV: python list
    :param key: python list
    :return: linked list
    """
    ll = linked_list_type.make_empty_list()

    current = ciphertext.head

    element = encryption.xor_gate(encryption.decryption(current.value, key), IV)
    ll.head = linked_list_type.MutableNode(element, None)
    ll.size += 1

    prev = current
    current = current.next
    prev_node = ll.head

    while current is not None:
        element = encryption.xor_gate(encryption.decryption(current.value, key), prev.value)
        node = linked_list_type.MutableNode(element, None)
        prev_node.next = node

        ll.size += 1
        prev = current
        current = current.next
        prev_node = node

    return ll
