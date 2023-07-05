workers={"rick":5,"marcus":5,"theo":5,"maman":5,"max":5,"luca":7}

class Fire:
    def __init__(self):
        self.worker={}
    def staff(self,workers):
        self.worker.append(workers)
    def keep(self):
        return self.worker
    def gone(self,people):
        return workers.pop(people)


class Opinion:
    def __init__(self):
        self.worker={}
    def good(self,workers,worker):
        self.workers[worker]+=1
    def excellent(self,worker,workers):
        self.workers[worker]+=2
    def bad(self,worker,workers):
        self.workers[worker]-=1


opinions=Opinion()
for worker in workers:
    opinion=input("What did you think of " + worker + "'s performance this year? ")
    if opinion=="good":
        workers[worker]+=1
    elif opinion=="excellent":
        workers[worker]+=2
    elif opinion=="ok":
        workers[worker]+=0
    else:
        workers[worker]-=1


fire=Fire()
for people in workers.copy():
        if workers[people]<5:
            fire.gone(people)
        else:
            fire.keep

print(workers)

def supervisor():
    new_supervisor=(max(workers.keys()))
    print("Supervisors:", *new_supervisor)
supervisor()