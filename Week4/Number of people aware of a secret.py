class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        q = deque([(delay, forget)])
        print(q)
        for i in range(n - 1):
            num_people = len(q)
            for j in range(num_people):
                cur_delay, cur_forget = q.popleft()
                cur_delay-=1
                cur_forget -= 1
                if cur_forget != 0:
                    q.append((cur_delay, cur_forget))
                else:
                    continue
                if cur_delay <= 0:
                    q.append((delay, forget))
                
        return len(q)