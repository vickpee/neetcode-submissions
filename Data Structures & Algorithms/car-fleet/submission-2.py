class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        firstTime = (target - cars[0][0]) / cars[0][1]
        fleets = [firstTime]
        
        for i in range(1, len(cars)):
            time = (target - cars[i][0]) / cars[i][1]
            if time > fleets[-1]:
                fleets.append(time)
        
        return len(fleets)

