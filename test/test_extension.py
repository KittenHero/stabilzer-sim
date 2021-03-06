from stabilizer_sim import *
from unittest import TestCase, main, mock
from test.test_core import GateTest, I, X, Y, Z, ket


class TestX(GateTest):
    '''
    {I,X} ->  {I,X}
    {Z,Y} -> -{Z,Y}
    '''
    def test_state(self):
        x0 = PauliX(0)

        inputs   = [[I], [X], [Y], [Z]]
        outputs  = [[I], [X], [Y], [Z]]
        signflip = [  0,   0,   1,   1]

        self.assert_gate_transform(x0, inputs, outputs, signflip)


class TestZ(GateTest):
    '''
    {I,Z} ->  {I,Z}
    {X,Y} -> -{X,Y}
    '''
    def test_state(self):
        z0 = PauliZ(0)

        inputs   = [[I], [X], [Y], [Z]]
        outputs  = [[I], [X], [Y], [Z]]
        signflip = [  0,   1,   1,   0]

        self.assert_gate_transform(z0, inputs, outputs, signflip)



class TestSwap(GateTest):
    '''
    {II,XX,YY,ZZ} -> {II,XX,YY,ZZ}
      {IX,IY,IZ}  ->  {XI,YI,ZI}
      {XY,XZ,YZ}  ->  {YX,ZX,ZY}
    '''
    def test_single(self):
        swap01 = Swap(target=(0, 1))

        inputs    = [[I, I], [Z, Z], [X, X], [Y, Y]]
        outputs   = [[I, I], [Z, Z], [X, X], [Y, Y]]
        signflip  = [     0,      0,      0,      0]

        inputs   += [[I, Z], [Z, I], [I, X], [X, I]]
        outputs  += [[Z, I], [I, Z], [X, I], [I, X]]
        signflip += [     0,      0,      0,      0]

        inputs   += [[Y, I], [I, Y], [X, Y], [Y, X]]
        outputs  += [[I, Y], [Y, I], [Y, X], [X, Y]]
        signflip += [     0,      0,      0,      0]

        inputs   += [[X, Z], [Z, X], [Z, Y], [Y, Z]]
        outputs  += [[Z, X], [X, Z], [Y, Z], [Z, Y]]
        signflip += [     0,      0,      0,      0]

        self.assert_gate_transform(swap01, inputs, outputs, signflip)


class TestCZ(GateTest):
    '''
    {II,ZI,IZ,ZZ} ->  {II,ZI,IZ,ZZ}
       {IX,IY}    ->     {ZX,ZY}
       {XI,YI}    ->     {XZ,YZ}
       {XX,YX}    ->    -{YY,XY}
    '''
    def test_definite(self):
        s = QState.zeros(2)
        cz01 = ControlledZ(target=(0, 1))

        inputs    = [[I, I], [I, Z], [Z, I], [Z, Z]]
        outputs   = [[I, I], [I, Z], [Z, I], [Z, Z]]
        signflip  = [     0,      0,      0,      0]

        inputs   += [[I, X], [Z, X], [I, Y], [Z, Y]]
        outputs  += [[Z, X], [I, X], [Z, Y], [I, Y]]
        signflip += [     0,      0,      0,      0]

        inputs   += [[X, I], [X, Z], [Y, I], [Y, Z]]
        outputs  += [[X, Z], [X, I], [Y, Z], [Y, I]]
        signflip += [     0,      0,      0,      0]

        inputs   += [[X, X], [Y, Y], [X, Y], [Y, X]]
        outputs  += [[Y, Y], [X, X], [Y, X], [X, Y]]
        signflip += [     1,      1,      1,      1]

        self.assert_gate_transform(cz01, inputs, outputs, signflip)


if __name__ == '__main__':
    main()
