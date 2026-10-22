class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for i in range(len(asteroids)):
            if(len(stack)>0):
                if((stack[-1]>0 and asteroids[i]>0) or (stack[-1]<0 and asteroids[i]<0) or (stack[-1]<0 and asteroids[i]>0)): stack.append(asteroids[i])
                else:
                    while(len(stack)>0 and stack[-1]>0 and stack[-1]<abs(asteroids[i])): stack.pop()
                    if(len(stack) == 0): stack.append(asteroids[i])
                    elif(stack[-1] == abs(asteroids[i])): stack.pop()
                    elif(stack[-1] > abs(asteroids[i])): continue
                    else: stack.append(asteroids[i])
            else: stack.append(asteroids[i])
        return stack