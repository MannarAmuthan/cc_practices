class VoteMachine:
    def __init__(self):
        self.party_votes = {}

    def vote(self, n):
        if n not in self.party_votes:
            self.party_votes[n] = 0
        self.party_votes[n] += 1

    def result(self):
        p = ''
        c = 0
        for party in self.party_votes:
            if self.party_votes[party] > c:
                c = self.party_votes[party]
                p = party

        win_party = p
        print(f"{win_party} won with {c} votes")

        p = ''
        c = 0
        for party in self.party_votes:
            if self.party_votes[party] > c and party != win_party:
                c = self.party_votes[party]
                p = party

        print(f"{p} is opposition with {c} votes")

        d_parties = []
        for party in self.party_votes:
            if self.party_votes[party] < 5:
                d_parties.append(party)

        print(f"Deposit lost parties - {",".join(d_parties)}")


vote_machine = VoteMachine()
vote_machine.vote('A')
vote_machine.vote('A')
vote_machine.vote('A')
vote_machine.vote('A')
vote_machine.vote('A')
vote_machine.vote('B')
vote_machine.vote('B')
vote_machine.vote('C')

vote_machine.result()
