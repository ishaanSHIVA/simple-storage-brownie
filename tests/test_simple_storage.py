from brownie import SimpleStorage, accounts


def testDeploy():
    # Arranging
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})

    # Acting
    starting_value = simple_storage.retrieve()
    expected = 0
    # Asserting
    assert starting_value == expected


def testUpdateStorage():
    # Arrange
    # Arranging
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Acting
    simple_storage.store(15, {"from": account})
    expected = 15
    # Assert
    assert 5 == simple_storage.retrieve()
