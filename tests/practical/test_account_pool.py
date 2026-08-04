import threading

import pytest

from src.practical.account_pool import AccountPool


def test_account_pool_init():
    accounts = ["account1", "account2", "account3"]
    pool = AccountPool(accounts)

    assert pool.size() == 3
    assert pool.used_accounts() == []


def test_get_account():
    accounts = ["account1", "account2", "account3"]
    pool = AccountPool(accounts)

    account = pool.get_account()
    assert account == "account1"  # PriorityQueue returns items in the order they were added
    assert account in pool.used_accounts()


def test_release_account():
    accounts = ["account1", "account2", "account3"]
    pool = AccountPool(accounts)

    account = pool.get_account()
    assert account in pool.used_accounts()

    pool.release_account(account)
    assert account not in pool.used_accounts()


def test_accounts_ordered_by_priority():
    accounts = ["account1", "account2", "account3"]
    pool = AccountPool(accounts)

    account1 = pool.get_account()
    assert account1 == "account1"

    account2 = pool.get_account()
    assert account2 == "account2"

    pool.release_account(account1)
    account3 = pool.get_account()
    assert account3 == "account3"

    account4 = pool.get_account()
    assert account4 == "account1"


def test_block_until_account_available():
    accounts = ["account1"]
    pool = AccountPool(accounts, timeout=1)

    account = pool.get_account()
    assert account == "account1"
    assert account in pool.used_accounts()

    result = []
    thread = threading.Thread(target=lambda: result.append(pool.get_account()), daemon=True)
    thread.start()
    thread.join(timeout=0.01)
    assert thread.is_alive()  # Priority Queue should be blocking call
    assert result == []

    pool.release_account("account1")
    thread.join(timeout=0.1)
    assert not thread.is_alive()
    assert result == ["account1"]
    assert account in pool.used_accounts()


def test_timeout():
    accounts = ["account1"]
    pool = AccountPool(accounts, timeout=0.01)

    account = pool.get_account()
    assert account in accounts

    with pytest.raises(AccountPool.AccountPoolTimeoutError):
        pool.get_account()


def test_size():
    pool = AccountPool([])
    assert pool.size() == 0

    pool.add_account("account1")
    assert pool.size() == 1
