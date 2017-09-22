# model

model = Model()
in0 = Input("op1", "TENSOR_FLOAT32", "{3}")
weights = Input("op2", "TENSOR_FLOAT32", "{1, 1}")
bias = Input("b0", "TENSOR_FLOAT32", "{1}")
out0 = Output("op3", "TENSOR_FLOAT32", "{3}")
act = Int32Scalar("act", 0)
model = model.Operation("FULLY_CONNECTED", in0, weights, bias, act).To(out0)

# Example 1. Input in operand 0,
input0 = {in0: # input 0
             [2, 32, 16],
         weights: [2],
         bias: [4]}
output0 = {out0: # output 0
               [8, 68, 36]}

# Instantiate an example
Example((input0, output0))