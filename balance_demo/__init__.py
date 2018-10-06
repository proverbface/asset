from plug.abstract import Plugin

import balance_demo.error
import balance_demo.model
import balance_demo.transform


class BalanceTutorialPlugin(Plugin):
    @classmethod
    def setup(cls, registry):
        components = [
            # Include your plugin's models/transforms/errors etc here.
            balance_demo.error.NotEnoughMoneyError,
            balance_demo.error.InvalidAmountError,
            balance_demo.model.BalanceModel,
            balance_demo.transform.BalanceTransfer,
        ]

        for component in components:
          registry.register(component)