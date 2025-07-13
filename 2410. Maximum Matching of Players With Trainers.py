class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        
        n_trainers = len(trainers)
        count = 0
        for player in players:
            if player <= trainers[count]:
                count += 1
                if count == n_trainers:
                    break
        
        return count