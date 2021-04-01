#!/usr/bin/python3
import os
from brownie import LegalDocumentsCollectible, accounts, network, config


def main():
    dev = accounts.add(os.getenv(config['wallets']['from_key']))
    print(network.show_active())
    legal_documents_collectible = LegalDocumentsCollectible.deploy({'from': accounts[1]})
    legal_documents_collectible.createCollectible("None", "0")
    print(legal_documents_collectible.ownerOf(0))
