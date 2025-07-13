class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        
        from collections import defaultdict

        loss_count = defaultdict(int)
        players = set()

        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            loss_count[loser] += 1

        zero_losses = []
        one_loss = []

        for player in players:
            if loss_count[player] == 0:
                zero_losses.append(player)
            elif loss_count[player] == 1:
                one_loss.append(player)

        return [sorted(zero_losses), sorted(one_loss)]