import numpy as np

class Tensor (object):
    def __init__(self,data,autograd=False, creators=None, creation_op=None, id=None):
        """
        creators: is a list containing any tensors used in the creation of the current tensor
        creators_op: is a related feature that stores the instructions creators used in the creation process.

        """
        self.data = np.array(data)
        self.creation_op = creation_op
        self.creators = creators
        self.grad = None
        self.autograd = autograd
        self.children = {}
        if (id is None):
            id = np.random.randint(0,100000)
        self.id = id

        # tracks how many children a tensor has
        if (creators is not None):
            for c in creators:
                if (self.id not in c.children):
                    c.children[self.id] = 1
                else:
                    c.children[self.id] += 1

    # check whether a tensor has received the correct number of gradients  from each child
    def all_children_grads_accounted_for(self):
        for id,cnt in self.children.items():
            if (cnt != 0):
                return False
        return True


    def backpropagation(self, grad=None, grad_origin=None):
        """
        For compute Gradients
        """
        if (self.autograd):
            if(grad_origin is not  None):
                # Checks to make sure you can backpropagate or whether you’re waiting for a gradient, in which case decrement the counter
                if(self.children[grad_origin.id] == 0):
                    raise  Exception("cannot backdrop more than once")
                else:
                    self.children[grad_origin.id] -= 1

            if(self.grad is None):
                 #accumulates gradients from several children
                self.grad = grad
            else:
                self.grad += grad

            if( self.creators is not None
                and (self.all_children_grads_accounted_for()
                or grad_origin is None)):

                if(self.creation_op == "add"):
                    self.creators[0].backpropagation(self.grad, self)
                    self.creators[1].backpropagation(self.grad, self)

    def __add__(self, other):
        if(self.autograd and other.autograd):
            return Tensor(
                    self.data + other.data,
                    autograd=True,
                    creators=[self,other],
                    creation_op="add"
            )

        return Tensor(self.data + other.data)

    def __repr__(self):
        return str(self.data.__repr__())

    def __str__(self):
        return str(self.data.__str__())

# prueba 1
x = Tensor([1,2,3,4])
y = Tensor([2,2,2,2])
print(x)


z = x + y
z.backpropagation(Tensor(np.array([1,1,1,1])))
print(x.grad)
print(y.grad)
print(z.creators)
print(z.creation_op)

# prueba 2
a = Tensor([1,2,3,4,5], autograd=True)
b = Tensor([2,2,2,2,2], autograd=True)
c = Tensor([5,4,3,2,1], autograd=True)
d = a + b
e = b + c
f = d + e
f.backpropagation(Tensor(np.array([1,1,1,1,1])))
print(b.grad.data == np.array([2,2,2,2,2]))

def hola(x):
    return x

hola(x)