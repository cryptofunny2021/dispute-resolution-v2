# v2.0
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

class DisputeResolution(gl.Contract):
    disputes: TreeMap[Address, str]
    reputation_address: Address

    def __init__(self):
        # Hardcoded reputation address
        self.reputation_address = Address("0x77f86b0D8A0230BD612F41F9c638d682f6aBc476")

    @gl.public.write
    def submit_dispute(self, description: str) -> None:
        user = gl.message.sender_address
        self.disputes[user] = description
        
        # Small reputation penalty
        try:
            rep = gl.contract(self.reputation_address)
            rep.record_action(u256(-5))
        except:
            pass

    @gl.public.view
    def my_dispute(self) -> str:
        user = gl.message.sender_address
        return self.disputes.get(user, "")
