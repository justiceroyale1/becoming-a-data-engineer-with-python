from collections import deque

order_queue = deque(["Jollof Rice", "Pizza", "Spaghetti"])

order_queue.append("Moi-moi and fish stew")
order_queue.append("Akara and Akamu")

order = order_queue.popleft()
while order:
    print('Serve', order)
    if(len(order_queue) == 0):
        print('All done!')
        break
    order = order_queue.popleft()