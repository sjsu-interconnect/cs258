import networkx as nx
import numpy as np
import random

class Request:
    """This class represents a request. Each request is characterized by source and destination nodes and holding time (represented by an integer).

    The holding time of a request is the number of time slots for this request in the network. You should remove a request that exhausted its holding time.
    """
    def __init__(self, s, t, ht):
        self.s = s
        self.t = t
        self.ht = ht

    def __str__(self) -> str:
        return f'req({self.s}, {self.t}, {self.ht})'
    
    def __repr__(self) -> str:
        return self.__str__()
        
    def __hash__(self) -> int:
        # used by set()
        return self.id


class EdgeStats:
    """This class saves all state information of the system. In particular, the remaining capacity after request mapping and a list of mapped requests should be stored.
    """
    def __init__(self, u, v, cap) -> None:
        self.id = (u,v)
        self.u = u
        self.v = v 
        # remaining capacity
        self.cap = cap 

        # spectrum state (a list of requests showing color <-> request mapping). Each index of this list represents a color
        self.__slots = [None] * cap

    def __str__(self) -> str:
        return f'{self.id}, cap = {self.cap}: {self.reqs}'
    
    def add_request(req: Request, color:int):
        """update self.__slots by adding a request to the specific color slot

        Args:
            req (Request): a request
            color (int): a color to be used for the request
        """
        pass

    def remove_request(req: Request):
        """update self.__slots by removing a request

        Args:
            req (Request): a request to be removed
        """
        pass

    def get_available_colors() -> list[int]:
        """return a list of integers available to accept requests
        """
        pass
    
    def show_spectrum_state():
        """Come up with a representation to show the utilization state of a link (by colors)
        """
        pass
    

def generate_requests(num_reqs: int, g: nx.Graph) -> list[Request]:
    """Generate a set of requests, given the number of requests and an optical network (topology)

    Args:
        num_reqs (int): the number of requests
        g (nx.Graph): network topology

    Returns:
        list[Request]: a list of request instances
    """
    pass


def generate_graph() -> nx.Graph:
    """Generate a networkx graph instance importing a GML file. Set the capacity attribute to all links based on a random distribution.

    Returns:
        nx.Graph: a weighted graph
    """
    pass


def route(g: nx.Graph, estats: list[EdgeStats], req:Request) -> list[EdgeStats]:
    """Use a routing algorithm to decide a mapping of requests onto a network topology. The results of mapping should be reflected. Consider available colors on links on a path. 

    Args:
        g (nx.Graph): a network topology
        req (Request): a request to map

    Returns:
        list[EdgeStats]: updated EdgeStats
    """
    return estats

        
if __name__ == "__main__":
    # 1. generate a network

    # 2. generate a list of requests (num_reqs)
    # we simulate the sequential arrivals of the pre-generated requests using a for loop in this simulation
    requests = list()

    # 3. prepare an EdgeStats instance for each edge.

    # 4. this simulation follows the discrete event simulation concept. Each time slot is defined by an arrival of a request
    for req in requests:
        # 4.1 use the route function to map the request onto the topology (update EdgeStats)

        # 4.2 remove all requests that exhausted their holding times
        pass