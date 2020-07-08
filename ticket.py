# Creating Passenger's and Agent Classes

class passenger:
    def __init__(self, idNum, ArrivalTime):
        self._idNum = idNum
        self._arrivalTime = ArrivalTime

    # Return id Number
    def idNum(self):
        return self._idNum

    # Return Arrival Time
    def timeArrived(self):
        return self._arrivalTime


class TicketAgent:
    def __init__(self, idNum):
        self._idNum = idNum
        self._passenger = None
        self._stopTime = -1
    # Return Id Number
    def idNum(self):
        return self._idNum

    # Determine if Agent is Free
    def isFree(self):
        return self._passenger is None

    # Setermine if Agent has finished a Service
    def isFinished(self, CurTime):
        return self._passenger is not None and CurTime == self._stopTime

    # Start Attending to a Passenger
    def startService(self, passenger, stopTime):
        self._passenger = passenger
        self._stopTime = stopTime

    # Stop Service to a Passenger
    def stopService(self):
        thepassenger = self._passenger
        self._passenger = None
        return thepassenger