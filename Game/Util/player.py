class Player:
    def __init__(self,id,client,username,color):
        self.id=id
        self.client=client
        self.username=username
        self.color=color
        self.isPlaying=False
        self.room=None
        self.perm=0
    def setPerm(self,perm):
        self.perm=perm
