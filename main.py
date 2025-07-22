#Using the stored script as module

from crypto_utils import CryptoWallet

my_wallet = CryptoWallet('Joseph')
my_wallet.deposit('ETH', 0.7)
print(my_wallet.view_wallet())
my_wallet.Withdraw('ETH', 0.2)
print('')
print(f"I just withdraw {0.2}, I am presently left with {my_wallet.view_wallet()}")