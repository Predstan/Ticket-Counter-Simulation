# Implements Ticket Counter Simulation and Display Result in a Table

import plotly.graph_objects as go
from HandleService import TicketCounterSimulation

# Main Function
def main():
    header = ["Num Minutes", "Num Agents", "Average Service", "Time Between", "Average Wait", "Passengers Served", "Passengers Remaining"]
    # Request user for number of Simulations
    num = int(input("How many times do you want Simulation to Run?")) 
    table = [ [] for _ in range(7) ]
    # Request user for simulation details
    for i in range(num):
        numAgents = int(input("Enter Number of Agents"))
        numMinutes = int(input("Enter Number of Total Minutes"))
        betweenTime = int(input("Enter estimated time for Passenger's Arrival"))
        serviceTime = int(input("Enter Service Time"))
        numServed, avgwait, remaining = simulate(numAgents, numMinutes, betweenTime, serviceTime)
        value = [numMinutes, numAgents, serviceTime, betweenTime, avgwait, numServed, remaining]
        for i in range(len(value)):
            table[i].append(value[i])
    # Creates Table and Plot Datas
    fig = go.Figure(data=[go.Table(
    header=dict(values=header,
                line_color='darkslategray',
                fill_color='lightskyblue',
                align='left'),
    cells=dict(values=table,
               line_color='darkslategray',
               fill_color='lightcyan',
               align='left'))])

    fig.update_layout(width=700, height=len(table[i] * 100))
    fig.show()

# Reun Simulation
def simulate(numAgents, numMinutes, betweenTime, serviceTime):
    simul = TicketCounterSimulation(numAgents, numMinutes, betweenTime, serviceTime)
    numServed, avgwait, remaining = simul.run()
    return numServed, avgwait, remaining



if __name__ == "__main__":
    main()
