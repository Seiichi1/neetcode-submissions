class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=sorted(zip(position,speed),reverse=True)
        times=[(target-pos)/spd for pos,spd in cars]
        fleet=1
        max_time=times[0]
        for time in times:
            if time>max_time:
                fleet+=1
                max_time=time
        return fleet
        