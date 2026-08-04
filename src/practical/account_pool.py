import queue
import time


class AccountPool:
    """Thread-safe pool of account identifiers, handed out oldest-idle-first.

    Callers check an account out with `get_account()` and must return it with `release_account()`
    when done. If none are available, `get_account()` blocks (up to `timeout` seconds) until one is
    released, so this is safe to share across threads that each need exclusive use of an account.
    """

    class AccountPoolTimeoutError(Exception):
        """Raised when no account becomes available within the pool's timeout."""

        def __init__(self, timeout: float):
            super().__init__(f"No accounts available after {timeout} seconds")

    def __init__(self, accounts, timeout: float = 30):
        self.timeout = timeout
        self.account_queue = queue.PriorityQueue[tuple[int, str]]()
        self.accounts = accounts
        self.outstanding_accounts: set[str] = set()

        for account in accounts:
            self.account_queue.put((time.monotonic_ns(), account))

    def add_account(self, account: str):
        """Add a new account to the pool, immediately available for checkout."""
        self.accounts.append(account)
        self.account_queue.put((time.monotonic_ns(), account))

    def get_account(self) -> str:
        """Check out and return the account that's been idle longest, blocking until one is free.

        Raises `AccountPoolTimeoutError` if none becomes available within `self.timeout` seconds.
        """
        try:
            _, account = self.account_queue.get(block=True, timeout=self.timeout)
        except queue.Empty:
            raise self.AccountPoolTimeoutError(timeout=self.timeout)

        self.outstanding_accounts.add(account)
        return account

    def release_account(self, account):
        """Return a checked-out account to the pool."""
        self.outstanding_accounts.remove(account)
        self.account_queue.put((time.monotonic_ns(), account))

    def size(self):
        """Return the total number of accounts in the pool, checked out or not."""
        return len(self.accounts)

    def used_accounts(self):
        """Return the accounts currently checked out."""
        return list(self.outstanding_accounts)
