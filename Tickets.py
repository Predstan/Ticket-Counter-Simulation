# Implementation of Main Simulation
# Displaying result accordinmg to customer arrival and agent's services

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
        self.printResult()
            

    def printResult(self):
        numServed = self._numPassengers - len(self._passengers)
        avgwait = float(self._totalWaitTime) / numServed
        print("")
        print("Number of passengers served  =" , numServed)
        print("Number of passengers remaining in line = %d" % len(self._passengers) )
        print("the average wait time was %4.2f minutes." %avgwait)
    

      # Handle Customer Arrival
    def _handleArrival(self, curTime):
        prob = randint(0.0, 1.0)
        if 0.0 <= prob and prob <= self._arriveprob:
            person = passenger(self._numPassengers + 1, curTime)
            self._passengers.enqueue( person )
            self._numPassengers += 1
            print ( "Time {}: Passenger {} arrived".format(curTime, person.idNum() ))
            
            
            
    # Begin Customer Service
    def _handleBeginService(self, curTime):
        
        i = 0
        while i < len(self._Agents):
            if self._Agents[i].isFree() and not self._passengers.isEmpty() and curTime != self._numMinutes:
                passenger = self._passengers.dequeue()
                self.served += 1
                stoptime = curTime + self._serviceTime
                self._Agents[i].startService(passenger, stoptime)
                self._totalWaitTime += (curTime - passenger.timeArrived())
                print ( "Time {}: Agent {} started serving passenger {}".format(curTime, self._Agents[i].idNum(), passenger.idNum()))
            i += 1
            
        
            

    # Stop Customer Service
    def _handleEndService(self, curTime): 
        i = 0
        while i < len(self._Agents): 
            if self._Agents[i].isFinished(curTime):
                passenger = self._Agents[i].stopService()
                print ( "Time {}: Agent {} stopped serving passenger {}".format(curTime, self._Agents[i].idNum(), passenger.idNum() ))
            i += 1
            
        

done = TicketCounterSimulation( 2, 25, 2, 3)
done.run()

        
