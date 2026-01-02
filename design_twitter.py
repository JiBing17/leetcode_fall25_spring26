class Twitter:

    def __init__(self):
        self.followers = {}
        self.tweets = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:

        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append([self.timestamp, tweetId])
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        res = []

        followees = self.followers.get(userId, set())
        followees.add(userId)  # see own tweets

        for uid in followees:
            if uid in self.tweets:
                for time, tid in self.tweets[uid][-10:]:
                    heapq.heappush(heap, (time, tid))

        for _ in range(10):
            if not heap:
                break
            res.append(heapq.heappop(heap)[1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set()
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            self.followers[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)