# Define a class to represent a packet
class Packet:
    def _init_(self, id, gen_time):
        self.id = id  # packet identifier
        self.gen_time = gen_time  # generation time of the packet

# Define a comparator function to sort packets based on their generation time
def cmp(a, b):
    return a.gen_time < b.gen_time

if __name__ == "__main__":
    m = int(input())  # number of servers

    alpha = 0  # alpha is the smallest generation time of the packets under service
    I = m  # I is the number of idle servers
    Q = []  # Q is the set of distinct packets that are under service

    while True:
        s = int(input())  # generation time of the incoming packet

        if s == -1:  # end of input
            break

        if I == 0:  # all servers are busy
            if s <= alpha:  # packet pi is stale
                pi = Packet(len(Q), s)
                Q.append(pi)
            else:  # packet pi carries fresh information
                pj = min(Q, key=lambda x: x.gen_time)  # find packet pj with generation time alpha
                Q.remove(pj)  # preempt packet pj and remove it from the queue
                pi = Packet(len(Q), s)
                Q.append(pi)  # assign packet pi to the idle server
        else:  # at least one of the servers is idle
            pi = Packet(len(Q), s)
            Q.append(pi)  # assign packet pi to an idle server
            I -= 1  # decrease the number of idle servers

        alpha = min(Q, key=lambda x: x.gen_time).gen_time  # update alpha

        if Q:  # a packet is delivered
            pl = min(Q, key=lambda x: x.gen_time)  # pick the packet with the smallest generation time in the queue
            Q.remove(pl)  # remove the delivered packet from the queue

            if I > 0 and Q:  # there is an idle server and the queue is not empty
                ph = max(Q, key=lambda x: x.gen_time)  # find the packet with the largest generation time in the queue
                Q.append(ph)  # assign the packet with the largest generation time to the idle server
                I -= 1  # decrease the number of idle servers

        alpha = min(Q, key=lambda x: x.gen_time).gen_time  # update alpha
