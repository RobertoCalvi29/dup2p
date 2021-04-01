#!/usr/bin/python3

import os
from brownie import RealEstateCollectible, accounts, network, config


def main():
    dev = accounts.add(os.getenv(config['wallets']['from_key']))
    print(network.show_active())
    simple_collectible = RealEstateCollectible[len(RealEstateCollectible)-1]
    return simple_collectible.createCollectible("None", {'from': dev})
