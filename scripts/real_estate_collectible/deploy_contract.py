#!/usr/bin/python3
import os
from brownie import RealEstateCollectible, accounts, network, config


def main():
    dev = accounts.add(os.getenv(config['wallets']['from_key']))
    print(network.show_active())
    simple_collectible = RealEstateCollectible.deploy({'from': accounts[1]})
    simple_collectible.createCollectible("None")
    print(simple_collectible.ownerOf(0))
