#!/usr/bin/python3
import os
from brownie import LegalDocumentsCollectible, accounts, network, config


def main():
    dev = accounts.add(os.getenv(config['wallets']['from_key']))
    print(network.show_active())
    simple_collectible = LegalDocumentsCollectible[len(LegalDocumentsCollectible) - 1]
    return simple_collectible.createCollectible("None", {'from': dev})
