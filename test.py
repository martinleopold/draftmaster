def assertRaises(error, fn):
    try:
        fn()
    except Exception as e:
        assert type(e) is error, f'Should have raised {error.__name__} instead of {type(e).__name__}'
        return
    raise AssertionError(f'Should have raised {error.__name__}')

if __name__ == '__main__':
    from draftmaster import *
    
    # Chapter 3: Beginning Your HP-GL Program
    
    assert DF() == 'DF;'
    assert df() == 'DF;'
    assertRaises(TypeError, lambda: DF(0))
    
    assert IN() == 'IN;'
    assert in_() == 'IN;'
    assert IN(partial=True) == 'IN-1;'
    assertRaises(TypeError, lambda: IN(False, 0))
    
    assert IP() == 'IP;'
    assert ip() == 'IP;'
    assert IP(0,1) == 'IP0,1;'
    assert IP(0,1,2,3) == 'IP0,1,2,3;'
    assertRaises(TypeError, lambda: IP(0))
    assertRaises(TypeError, lambda: IP(0,1,2))
    assertRaises(TypeError, lambda: IP(0,1,2,3,4))
    
    assert SC() == 'SC;'
    assert sc() == 'SC;'
    assert SC(0,1,2,3) == 'SC0,1,2,3;'
    assert SC(0,1,2,3,4) == 'SC0,1,2,3,4;'
    assert SC(0,1,2,3,4,5,6) == 'SC0,1,2,3,4,5,6;'
    assertRaises(TypeError, lambda: SC(0))
    assertRaises(TypeError, lambda: SC(0,1))
    assertRaises(TypeError, lambda: SC(0,1,2))
    assertRaises(TypeError, lambda: SC(0,1,2,3,4,5))
    assertRaises(TypeError, lambda: SC(0,1,2,3,4,5,6,7))
    
    # Chapter 4: Drawing Lines and Rectangles
    
    assert EA(0,1) == 'EA0,1;'
    assert ea(0,1) == 'EA0,1;'
    assertRaises(TypeError, lambda: EA())
    assertRaises(TypeError, lambda: EA(0))
    assertRaises(TypeError, lambda: EA(0,1,2))
    
    assert ER(0,1) == 'ER0,1;'
    assert er(0,1) == 'ER0,1;'
    assertRaises(TypeError, lambda: ER())
    assertRaises(TypeError, lambda: ER(0))
    assertRaises(TypeError, lambda: ER(0,1,2))
    
    assert PA() == 'PA;'
    assert pa() == 'PA;'
    assert PA(0) == 'PA0;'
    assert PA(0,1) == 'PA0,1;'
    assert PA(0,1,2) == 'PA0,1,2;'
    assert PA(0,1,2,3) == 'PA0,1,2,3;'
    assert PA(0,1,2,3,4) == 'PA0,1,2,3,4;'
    assert PA(0,1,2,3,4,5) == 'PA0,1,2,3,4,5;'
    assert PA(0,1,2,3,4,5,6) == 'PA0,1,2,3,4,5,6;'
    assert PA(0,1,2,3,4,5,6,7) == 'PA0,1,2,3,4,5,6,7;'
    assert PA(0,1,2,3,4,5,6,7,8) == 'PA0,1,2,3,4,5,6,7,8;'
    assert PA(0,1,2,3,4,5,6,7,8,9) == 'PA0,1,2,3,4,5,6,7,8,9;'
    
    assert PD() == 'PD;'
    assert pd() == 'PD;'
    assert PD(0) == 'PD0;'
    assert PD(0,1) == 'PD0,1;'
    assert PD(0,1,2) == 'PD0,1,2;'
    assert PD(0,1,2,3) == 'PD0,1,2,3;'
    assert PD(0,1,2,3,4) == 'PD0,1,2,3,4;'
    assert PD(0,1,2,3,4,5) == 'PD0,1,2,3,4,5;'
    assert PD(0,1,2,3,4,5,6) == 'PD0,1,2,3,4,5,6;'
    assert PD(0,1,2,3,4,5,6,7) == 'PD0,1,2,3,4,5,6,7;'
    assert PD(0,1,2,3,4,5,6,7,8) == 'PD0,1,2,3,4,5,6,7,8;'
    assert PD(0,1,2,3,4,5,6,7,8,9) == 'PD0,1,2,3,4,5,6,7,8,9;'

    assert PR() == 'PR;'
    assert pr() == 'PR;'
    assert PR(0) == 'PR0;'
    assert PR(0,1) == 'PR0,1;'
    assert PR(0,1,2) == 'PR0,1,2;'
    assert PR(0,1,2,3) == 'PR0,1,2,3;'
    assert PR(0,1,2,3,4) == 'PR0,1,2,3,4;'
    assert PR(0,1,2,3,4,5) == 'PR0,1,2,3,4,5;'
    assert PR(0,1,2,3,4,5,6) == 'PR0,1,2,3,4,5,6;'
    assert PR(0,1,2,3,4,5,6,7) == 'PR0,1,2,3,4,5,6,7;'
    assert PR(0,1,2,3,4,5,6,7,8) == 'PR0,1,2,3,4,5,6,7,8;'
    assert PR(0,1,2,3,4,5,6,7,8,9) == 'PR0,1,2,3,4,5,6,7,8,9;'

    assert PU() == 'PU;'
    assert pu() == 'PU;'
    assert PU(0) == 'PU0;'
    assert PU(0,1) == 'PU0,1;'
    assert PU(0,1,2) == 'PU0,1,2;'
    assert PU(0,1,2,3) == 'PU0,1,2,3;'
    assert PU(0,1,2,3,4) == 'PU0,1,2,3,4;'
    assert PU(0,1,2,3,4,5) == 'PU0,1,2,3,4,5;'
    assert PU(0,1,2,3,4,5,6) == 'PU0,1,2,3,4,5,6;'
    assert PU(0,1,2,3,4,5,6,7) == 'PU0,1,2,3,4,5,6,7;'
    assert PU(0,1,2,3,4,5,6,7,8) == 'PU0,1,2,3,4,5,6,7,8;'
    assert PU(0,1,2,3,4,5,6,7,8,9) == 'PU0,1,2,3,4,5,6,7,8,9;'
    
    assert SP() == 'SP;'
    assert sp() == 'SP;'
    for i in range(9):
        assert SP(i) == f'SP{i};'
    assertRaises(TypeError, lambda: SP(0,1))
    
    # Part II – Advanced Plotting
    # Chapter 5: Enhancing Your Plots
    
    
    