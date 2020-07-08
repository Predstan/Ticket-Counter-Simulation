# # Implementation of the main simulation class

from Array  import Array
from Queue  import queue
from ticket import passenger, TicketAgent
from random import randint

class TicketCounterSimulation:
    # Create a simulation object.
    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
        # Parameters supplied by the user
        self._arriveprob = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes
        self.served = 0

        # Simulation components.
        self._passengers = queue()
        self._Agents = Array(numAgents)
        for i in range(numAgents):
            self._Agents[i] = TicketAgent(i+1)

        # Computed during the simulation.
        self._totalWaitTime = 0
        self._numPassengers = 0
 
    # Run the simulation using the parameters supplied
    def run(self):
        for curTime in range(self._numMinutes + 1):
            self._handleArrival ( curTime )
            self._handleBeginService( curTime )
            self._handleEndService( curTime )

        return self.Result()

    # Print the simulation results.
    def Result(self):
        numServed = self._numPassengers - len(self._passengers)
        avgwait = float(self._totalWaitTime) / numServed
        remaining = len(self._passengers)
        return numServed, avgwait, remaining

    # Handle Customer Arrival
    def _handleArrival(self, curTime):
        prob = randint(0.0, 1.0)
        if 0.0 <= prob and prob <= self._arriveprob:
            person = passenger(self._numPassengers, curTime)
            self._passengers.enqueue( person )
            self._numPassengers += 1
            
            
    # Begin Service
    def _handleBeginService(self, curTime):
        
        i = 0
        while i < len(self._Agents):
            if self._Agents[i].isFree() and not self._passengers.isEmpty() and curTime != self._numMinutes:
                passenger = self._passengers.dequeue()
                self.served += 1
                stoptime = curTime + self._serviceTime
                self._Agents[i].startService(passenger, stoptime)
                self._totalWaitTime += (curTime - passenger.timeArrived())
            i += 1
            

    # End Service
    def _handleEndService(self, curTime): 
        i = 0
        while i < len(self._Agents): 
            if self._Agents[i].isFinished(curTime):
                self._Agents[i].stopService()
            i += 1
            
        

done = TicketCounterSimulation( 2, 25, 2, 3)
done.run()

        
