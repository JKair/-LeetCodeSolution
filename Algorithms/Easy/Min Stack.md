Min Stack
=======
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

这道题让我们写一个可以获取最小值的栈。

解法：我们可以用两个栈来解决这个问题，一个是普通栈，一个是最小栈，遇到最小值我们就push进最小栈，然后有比最小栈的栈顶更小的就push进最小栈。pop的时候比较看一下最小栈的栈顶是不是和普通栈同一个数字，是的话就跟着一起pop。

```
class MinStack {
private:
    stack<int> res;
    stack<int> min;
public:
    void push(int x) {
        res.push(x);
        if (min.empty() || min.top() >= x)
            min.push(x);
    }

    void pop() {
        if (res.top() == min.top()) {
            min.pop();
        }
        res.pop();
    }

    int top() {
        if (res.empty()) return 0;
        return res.top();
    }

    int getMin() {
        if (min.empty()) return 0;
        return min.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
```
