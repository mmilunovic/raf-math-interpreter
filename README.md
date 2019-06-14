# Math Interpreter 

This is a simple math interpreter written in python for Compiler Construction course at Faculty of Computer Science. 

## Feature

Math interpreter is capable of calculating math expressions in infix, postfix or prefix notation. It also supports variable initialization and usage, logical expressions as well as Roman numbers. 


## Example:  

prefix --> + + 1 * 2 3 4 = 11

prefix --> + RIM(MCDXV) 66 = 1481

prefix --> > <= 334 RIM(MD) 4 = True

---

infix --> 4 * ( y = 5 + 8 * 6 ) / 7 = 30

infix --> 10 + RIM(XX) +  hana = RIM(M) + 10 = 1040

---

postfix --> 1 2 + 3 4 + * = 21

postfix --> 70 hana 10 = / = 7

## Usage

To try just run following commands. 

```bash
git clone https://github.com/mmilunovic/raf-math-interpreter.git
cd raf-math-interpreter
python main.py
```

To change the type of notation just write **infix**, **prefix** of **postfix** and write expressions as you like.
