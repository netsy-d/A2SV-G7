class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        statues= {}
        for winners,looser in matches:
            if winners not in statues:
                statues[winners]=0
            if looser not in statues:
                statues[looser]=1
            else:
                statues[looser]+=1
        player_0=[]
        player_1 = []
        for players in sorted(statues.keys()):
            if statues[players] == 0:
                player_0.append(players)
            elif statues[players] ==1:
                player_1.append(players)
        return [player_0,player_1]
