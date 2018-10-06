from plug.constant import TransactionEvent
from plug.key import ED25519SigningKey
from plug.message import Event
from plug.proof import SingleKeyProof
from plug.registry import Registry
from plug.transaction import Transaction
from plug.util import plug_address
from plug.util import sha256
from transform import BalanceTransform

class User:
    def __init__(self, signing_key, nonce=0):
        self.signing_key = signing_key
        self.nonce = nonce
        self.address = plug_address(signing_key)


async def main():
    bob = User(ED25519SigningKey.new())
    alice = User(ED25519SigningKey.new())

    transform = BalanceTransform(
        sender=bob.address,
        receiver=alice.address,
        amount=100,
    )

    challenge = transform.hash(sha256)

    proof = SingleKeyProof(user.address, user.nonce, challenge)
    proof.sign(bob.signing_key)

    transaction = Transaction(transform, {proof.address: proof})

    event = Event(
        event=TransactionEvent.ADD,
        payload=transaction
    )

    registry = Registry().with_default()
    registry.register(Event)
    registry.register(BalanceTransfer)

    payload = registry.pack(event)

    async with aiohttp.ClientSession() as session:
        async with session.post("http://localhost:8181/_api/v1/transaction", json=payload) as response:
            data = await response.json()

    print(data)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


