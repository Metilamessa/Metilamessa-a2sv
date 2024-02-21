class ListNode:
    def __init__(self, x=""):
        self.val = x
        self.next = None
        self.prev = None

class BrowserHistory(object):

    def __init__(self, homepage: str):
        self.backward = ListNode(homepage)
        self.forward11 = None

    def visit(self, url: str) -> None:
        newUrl = ListNode(url)
        self.backward.next = newUrl
        newUrl.prev = self.backward
        self.backward = newUrl
        self.forward11 = None

    def back(self, steps: int) -> str:
        while steps and self.backward.prev:
            self.backward = self.backward.prev
            steps -= 1
        return self.backward.val

    def forward(self, steps: int) -> str:
        while steps and self.backward.next:
            self.backward = self.backward.next
            steps -= 1
        return self.backward.val


    
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


