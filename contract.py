# v2.5 Stable
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

class DisputeResolution(gl.Contract):
    disputes: TreeMap[Address, str]
    scores: TreeMap[Address, u256]

    def __init__(self):
        pass

    @gl.public.write
    def submit_dispute(self, description: str) -> None:
        user = gl.message.sender_address
        self.disputes[user] = description
        
        current = self.scores.get(user, u256(0))
        self.scores[user] = current - u256(5)

    @gl.public.view
    def my_dispute(self) -> str:
        user = gl.message.sender_address
        return self.disputes.get(user, "No dispute")

    @gl.public.view
    def my_score(self) -> u256:
        user = gl.message.sender_address
        return self.scores.get(user, u256(0))
