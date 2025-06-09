class PhotosClient:
    def __init__(self, n: int) -> None:
        '''
        param n: total no. of photos
        '''
        # boolean list of size n+1, ignore index zero for convenince
        self.acked = [False] * (n + 1)
        # represents the max index k, such that phots [1..k] have been ackgn
        self.maxSoFar = 0
    
    def ack(self, x: int) -> None:
        '''
        Called whenever we need to acknoledge a incoming photo x
        '''
        # not required as such, but checking if inout is not validated
        if x < 1 or x > len(self.acked):
            return
        
        # mark teh current incooing true
        self.acked[x] = True

        # check to se if we have further acknowledgements and increase the max
        # accordingly until then
        while self.maxSoFar + 1 < len(self.acked) and self.acked[self.maxSoFar + 1]:
            self.maxSoFar += 1


    def getMax(self) -> int:
        '''
        Returns the maximum photo k that has been uploaded in a
        continious manner from [1..k]
        '''
        return self.maxSoFar
    

if __name__ == "__main__":
    photos_client = PhotosClient(10)

    photos_client.ack(1)
    print(photos_client.getMax())

    photos_client.ack(2)
    print(photos_client.getMax())

    photos_client.ack(4)
    print(photos_client.getMax())

    photos_client.ack(5)
    print(photos_client.getMax())

    photos_client.ack(3)
    print(photos_client.getMax())