from collections import deque
stack = deque()

stack.append('www.website/page01')
stack.append('www.website/page02')
stack.append('www.website/page03')
stack.append('www.website/page04')
print(stack)
#deque(['www.website/page01', 'www.website/page02', 'www.website/page03', 'www.website/page04'])
stack.pop()
print(stack)
#deque(['www.website/page01', 'www.website/page02', 'www.website/page03'])