def assertRaises(error, fn):
    try:
        fn()
    except Exception as e:
        assert type(e) is error, f'Should have raised {error.__name__} instead of {type(e).__name__}'
        return
    raise AssertionError(f'Should have raised {error.__name__}')

def assertTypeError(fn):
    return assertRaises(TypeError, fn)

def assertValueError(fn):
    return assertRaises(ValueError, fn)

if __name__ == '__main__':
    from draftmaster import *
    
    # Chapter 3: Beginning Your HP-GL Program
    
    assert DF() == 'DF;'
    assert df() == 'DF;'
    assertTypeError(lambda: DF(0))
    
    assert IN() == 'IN;'
    assert in_() == 'IN;'
    assert IN(partial=True) == 'IN-1;'
    assertTypeError(lambda: IN(False, 0))
    
    assert IP() == 'IP;'
    assert ip() == 'IP;'
    assert IP(0,1) == 'IP0,1;'
    assert IP(0,1,2,3) == 'IP0,1,2,3;'
    assertTypeError(lambda: IP(0))
    assertTypeError(lambda: IP(0,1,2))
    assertTypeError(lambda: IP(0,1,2,3,4))
    
    assert SC() == 'SC;'
    assert sc() == 'SC;'
    assert SC(0,1,2,3) == 'SC0,1,2,3;'
    assert SC(0,1,2,3,4) == 'SC0,1,2,3,4;'
    assert SC(0,1,2,3,4,5,6) == 'SC0,1,2,3,4,5,6;'
    assertTypeError(lambda: SC(0))
    assertTypeError(lambda: SC(0,1))
    assertTypeError(lambda: SC(0,1,2))
    assertTypeError(lambda: SC(0,1,2,3,4,5))
    assertTypeError(lambda: SC(0,1,2,3,4,5,6,7))
    
    # Chapter 4: Drawing Lines and Rectangles
    
    assert EA(0,1) == 'EA0,1;'
    assert ea(0,1) == 'EA0,1;'
    assertTypeError(lambda: EA())
    assertTypeError(lambda: EA(0))
    assertTypeError(lambda: EA(0,1,2))
    
    assert ER(0,1) == 'ER0,1;'
    assert er(0,1) == 'ER0,1;'
    assertTypeError(lambda: ER())
    assertTypeError(lambda: ER(0))
    assertTypeError(lambda: ER(0,1,2))
    
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
    assertTypeError(lambda: SP(0,1))
    
    # Part II – Advanced Plotting
    # Chapter 5: Enhancing Your Plots
    
    assert FT() == 'FT;'
    assert ft() == 'FT;'
    assert FT(0) == 'FT0;'
    assert FT(0,1) == 'FT0,1;'
    assert FT(0,1,2) == 'FT0,1,2;'
    assertTypeError(lambda: FT(0,1,2,3))
    
    assert LT() == 'LT;'
    assert lt() == 'LT;'
    assert LT(0) == 'LT0;'
    assert LT(0,1) == 'LT0,1;'
    assertTypeError(lambda: LT(0,1,2))
    
    assert PT() == 'PT;'
    assert pt() == 'PT;'
    assert PT(0) == 'PT0;'
    assertTypeError(lambda: PT(0,1))
    
    assert RA(0,1) == 'RA0,1;'
    assert ra(0,1) == 'RA0,1;'
    assertTypeError(lambda: RA())
    assertTypeError(lambda: RA(0))
    assertTypeError(lambda: RA(0,1,2))
    
    assert RR(0,1) == 'RR0,1;'
    assert rr(0,1) == 'RR0,1;'
    assertTypeError(lambda: RR())
    assertTypeError(lambda: RR(0))
    assertTypeError(lambda: RR(0,1,2))
    
    assert SM() == 'SM;'
    assert sm() == 'SM;'
    assert SM('a') == 'SMa;'
    assert SM('a','x') == 'SMa,x;'
    assertTypeError(lambda: SM(0,1,2))
    assertTypeError(lambda: SM('a','b','c'))
    assertValueError(lambda: SM('ab'))
    assertValueError(lambda: SM('a','bc'))
    
    assert TL() == 'TL;'
    assert tl() == 'TL;'
    assert TL(0) == 'TL0;'
    assert TL(0,1) == 'TL0,1;'
    assertTypeError(lambda: TL(0,1,2))
    
    assert UF() == 'UF;'
    assert uf() == 'UF;'
    assert UF(0) == 'UF0;'
    assert UF(0,1) == 'UF0,1;'
    assert UF(0,1,2) == 'UF0,1,2;'
    assert UF(0,1,2,3) == 'UF0,1,2,3;'
    assert UF(0,1,2,3,4) == 'UF0,1,2,3,4;'
    assert UF(0,1,2,3,4,5) == 'UF0,1,2,3,4,5;'
    assert UF(0,1,2,3,4,5,6) == 'UF0,1,2,3,4,5,6;'
    assert UF(0,1,2,3,4,5,6,7) == 'UF0,1,2,3,4,5,6,7;'
    assert UF(0,1,2,3,4,5,6,7,8) == 'UF0,1,2,3,4,5,6,7,8;'
    assert UF(0,1,2,3,4,5,6,7,8,9) == 'UF0,1,2,3,4,5,6,7,8,9;'
    assert UF(0,1,2,3,4,5,6,7,8,9,10) == 'UF0,1,2,3,4,5,6,7,8,9,10;'
    assert UF(0,1,2,3,4,5,6,7,8,9,10,11) == 'UF0,1,2,3,4,5,6,7,8,9,10,11;'
    assert UF(0,1,2,3,4,5,6,7,8,9,10,11,12) == 'UF0,1,2,3,4,5,6,7,8,9,10,11,12;'
    assert UF(0,1,2,3,4,5,6,7,8,9,10,11,12,13) == 'UF0,1,2,3,4,5,6,7,8,9,10,11,12,13;'
    assert UF(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14) == 'UF0,1,2,3,4,5,6,7,8,9,10,11,12,13,14;'
    assert UF(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15) == 'UF0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15;'
    assert UF(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16) == 'UF0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16;'
    assert UF(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17) == 'UF0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17;'
    assert UF(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18) == 'UF0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18;'
    assert UF(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19) == 'UF0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19;'
    assertTypeError(lambda: UF(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
    
    assert XT() == 'XT;'
    assert xt() == 'XT;'
    assertTypeError(lambda: XT(0))
    
    assert YT() == 'YT;'
    assert yt() == 'YT;'
    assertTypeError(lambda: YT(0))
    
    # Chapter 6: Drawing Circles, Arcs, and Wedges
    
    assert AA(0,1,2) == 'AA0,1,2;'
    assert aa(0,1,2) == 'AA0,1,2;'
    assert AA(0,1,2,3) == 'AA0,1,2,3;'
    assertTypeError(lambda: AA())
    assertTypeError(lambda: AA(0))
    assertTypeError(lambda: AA(0,1))
    assertTypeError(lambda: AA(0,1,2,3,4))
    
    assert AR(0,1,2) == 'AR0,1,2;'
    assert ar(0,1,2) == 'AR0,1,2;'
    assert AR(0,1,2,3) == 'AR0,1,2,3;'
    assertTypeError(lambda: AR())
    assertTypeError(lambda: AR(0))
    assertTypeError(lambda: AR(0,1))
    assertTypeError(lambda: AR(0,1,2,3,4))
    
    assert CI(10) == 'CI10;'
    assert ci(10) == 'CI10;'
    assert CI(10,20) == 'CI10,20;'
    assertTypeError(lambda: CI())
    assertTypeError(lambda: CI(10,20,30))
    
    assert CT() == 'CT;'
    assert ct() == 'CT;'
    assert CT(0) == 'CT0;'
    assertTypeError(lambda: CT(0,1))
    
    assert EW(1,2,3) == 'EW1,2,3;'
    assert ew(1,2,3) == 'EW1,2,3;'
    assert EW(1,2,3,4) == 'EW1,2,3,4;'
    assertTypeError(lambda: EW())
    assertTypeError(lambda: EW(1))
    assertTypeError(lambda: EW(1,2))
    assertTypeError(lambda: EW(1,2,3,4,5))
    
    assert WG(1,2,3) == 'WG1,2,3;'
    assert wg(1,2,3) == 'WG1,2,3;'
    assert WG(1,2,3,4) == 'WG1,2,3,4;'
    assertTypeError(lambda: WG())
    assertTypeError(lambda: WG(1))
    assertTypeError(lambda: WG(1,2))
    assertTypeError(lambda: WG(1,2,3,4,5))
    
    # Chapter 7: Labeling Your Plots
    
    assert BL() == 'BL\x03'
    assert bl() == 'BL\x03'
    assert BL(terminator='#') == 'BL#'
    assert BL('abcxyz') == 'BLabcxyz\x03'
    assertValueError(lambda: BL('012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'))
    
    assert CP() == 'CP;'
    assert cp() == 'CP;'
    assert CP(0,1) == 'CP0,1;'
    assertTypeError(lambda: CP(0))
    assertTypeError(lambda: CP(0,1,2))

    assert DI() == 'DI;'
    assert di() == 'DI;'
    assert DI(0,1) == 'DI0,1;'
    assertTypeError(lambda: DI(0))
    assertTypeError(lambda: DI(0,1,2))

    assert DR() == 'DR;'
    assert dr() == 'DR;'
    assert DR(0,1) == 'DR0,1;'
    assertTypeError(lambda: DR(0))
    assertTypeError(lambda: DR(0,1,2))
    
    assert DT() == 'DT;'
    assert dt() == 'DT;'
    assert DT(0) == 'DT0;'
    assert DT('\x03') == 'DT\x03;'
    assertTypeError(lambda: DT(0,1))
    assertValueError(lambda: DT(chr(0)))
    assertValueError(lambda: DT(chr(5)))
    assertValueError(lambda: DT(chr(10)))
    assertValueError(lambda: DT(chr(27)))
    assertValueError(lambda: DT(';'))
    assertValueError(lambda: DT(chr(59)))
    
    assert DV() == 'DV;'
    assert dv() == 'DV;'
    assert DV(0) == 'DV0;'
    assertTypeError(lambda: DV(0,1))
    assertTypeError(lambda: DV(0,1,2))
    
    assert ES() == 'ES;'
    assert es() == 'ES;'
    assert ES(0) == 'ES0;'
    assert ES(0,1) == 'ES0,1;'
    assertTypeError(lambda: ES(0,1,2))
    
    assert LB('') == 'LB\x03'
    assert lb('') == 'LB\x03'
    assert LB('', terminator='#') == 'LB#'
    assert LB('abc', terminator='#') == 'LBabc#'
    assert LB('abcxyz') == 'LBabcxyz\x03'
    assertValueError(lambda: LB('012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'))
    
    assert LO() == 'LO;'
    assert lo() == 'LO;'
    assert LO(0) == 'LO0;'
    assertTypeError(lambda: LO(0,1))
    
    assert PB() == 'PB;'
    assert pb() == 'PB;'
    assertTypeError(lambda: PB(0))
    
    assert SI() == 'SI;'
    assert si() == 'SI;'
    assert SI(0,1) == 'SI0,1;'
    assertTypeError(lambda: SI(0))
    assertTypeError(lambda: SI(0,1,2))
    
    assert SL() == 'SL;'
    assert sl() == 'SL;'
    assert SL(0) == 'SL0;'
    assertTypeError(lambda: SL(0,1))
    
    assert SR() == 'SR;'
    assert sr() == 'SR;'
    assert SR(0,1) == 'SR0,1;'
    assertTypeError(lambda: SR(0))
    assertTypeError(lambda: SR(0,1,2))
    