from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():

    account = get_account()
    transactionDetail = {
        "from": account,
    }
    simple_storage = SimpleStorage.deploy(transactionDetail)
    storedValue = simple_storage.retrieve()
    print(storedValue)
    transaction = simple_storage.store(12, transactionDetail)
    transaction.wait(1)
    storedValue = simple_storage.retrieve()
    print(storedValue)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])


def main():
    print("Hello")
    deploy_simple_storage()
