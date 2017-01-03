Implement Stack using Queues
=======
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
Update (2015-06-11):
The class name of the Java function had been updated to MyStack instead of Stack.

这道题让我们设计一个栈，并且不能用栈直接实现，要用队列。

解法：我们可以用两个队列来操作，一个是Top队列，只存栈顶，另外一个是普通的队列，保存出了栈顶以外的所有数。

1. push，如果之前栈顶队列不为空，那么我们就把它放回普通队列，再把当前这个数放到栈顶队列就可以了。
1. top，这里要获取最顶的元素，我们要检查一下栈顶队列是不是为空，如果为空的话，我们要把普通队列的最后一个数字放到这里。
1. pop，这里去除栈顶，我们要保证栈顶一定有元素，可以先top一下。
1. empty，只要两个队列都为空了，那么就代表这个栈为空

```
class Stack {
private:
    queue<int> qTop,q;
public:
    // Push element x onto stack.
    void push(int x) {
        while (!qTop.empty()) {
            q.push(qTop.front());
            qTop.pop();
        }
        qTop.push(x);
    }

    // Removes the element on top of the stack.
    void pop() {
        top();
        qTop.pop();
    }

    // Get the top element.
    int top() {
        if (qTop.empty()) {
            for (int i = 1; i < q.size(); i++) {
                q.push(q.front());
                q.pop();
            }
            qTop.push(q.front());
            q.pop();
        }

        return qTop.front();
    }

    // Return whether the stack is empty.
    bool empty() {
        return q.empty() && qTop.empty();
    }
};
```
