# Dispute Resolution v2.0
# Fair Dispute System with Reputation Impact

from genlayer import *

class DisputeResolution(gl.Contract):
    disputes: TreeMap[Address, str]
    reputation_address: Address

    def __init__(self, rep_addr: Address):
        self.reputation_address = rep_addr

    @gl.public.write
    def submit_dispute(self, description: str) -> None:
        """Submit a new dispute"""
        user = gl.message.sender_address
        self.disputes[user] = description
        
        # Small reputation penalty for submitting dispute
        try:
            rep = gl.contract(self.reputation_address)
            rep.record_action(u256(-5))  # Negative impact
        except:
            pass

    @gl.public.view
    def my_dispute(self) -> str:
        """Get my submitted dispute"""
        return self.disputes.get(gl.message.sender_address, "")
