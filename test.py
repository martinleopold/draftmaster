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
    
    # Chapter 8: Drawing Polygons and Using the Polygon Buffer
    
    assert EP() == 'EP;'
    assert ep() == 'EP;'
    assertTypeError(lambda: EP(0))
    assertTypeError(lambda: EP(0,1))
    
    assert FP() == 'FP;'
    assert fp() == 'FP;'
    assertTypeError(lambda: FP(0))
    assertTypeError(lambda: FP(0,1))
    
    assert GM() == 'GM;'
    assert gm() == 'GM;'
    assert GM(0) == 'GM0;'
    assert GM(0,1) == 'GM0,1;'
    assert GM(0,1,2) == 'GM0,1,2;'
    assert GM(0,1,2,3) == 'GM0,1,2,3;'
    assert GM(0,1,2,3,4) == 'GM0,1,2,3,4;'
    assertTypeError(lambda: GM(0,1,2,3,4,5))
    
    assert PM() == 'PM;'
    assert pm() == 'PM;'
    assert PM(0) == 'PM0;'
    assertTypeError(lambda: PM(0,1))
    
    # Chapter 9: Changing Picture Area and Orientation
    
    assert IW() == 'IW;'
    assert iw() == 'IW;'
    assert IW(0,1,2,3) == 'IW0,1,2,3;'
    assertTypeError(lambda: IW(0))
    assertTypeError(lambda: IW(0,1))
    assertTypeError(lambda: IW(0,1,2))
    assertTypeError(lambda: IW(0,1,2,3,4))
    
    assert OH() == 'OH;'
    assert oh() == 'OH;'
    assertTypeError(lambda: OH(0))
    
    assert OP() == 'OP;'
    assert op() == 'OP;'
    assertTypeError(lambda: OP(0))
    
    assert OW() == 'OW;'
    assert ow() == 'OW;'
    assertTypeError(lambda: OW(0))

    assert RO() == 'RO;'
    assert ro() == 'RO;'
    assert RO(0) == 'RO0;'
    assert RO(90) == 'RO90;'
    assertTypeError(lambda: RO(0,1))
    
    # Chapter 10: Advanced Pen Control and Front-Panel Interaction
    
    assert AP() == 'AP;'
    assert ap() == 'AP;'
    assert AP(0) == 'AP0;'
    assertTypeError(lambda: AP(0,1))

    assert AS() == 'AS;'
    assert as_() == 'AS;'
    assert AS(0) == 'AS0;'
    assert AS(0,1) == 'AS0,1;'
    assertTypeError(lambda: AS(0,1,2))
    
    assert CV() == 'CV;'
    assert cv() == 'CV;'
    assert CV(0) == 'CV0;'
    assert CV(0,1) == 'CV0,1;'
    assertTypeError(lambda: CV(0,1,2))
    
    assert FS() == 'FS;'
    assert fs() == 'FS;'
    assert FS(0) == 'FS0;'
    assert FS(0,1) == 'FS0,1;'
    assertTypeError(lambda: FS(0,1,2))
    
    assert GP() == 'GP;'
    assert gp() == 'GP;'
    assert GP(0) == 'GP0;'
    assert GP(0,1) == 'GP0,1;'
    assert GP(0,1,2) == 'GP0,1,2;'
    assert GP(0,1,2,3) == 'GP0,1,2,3;'
    assertTypeError(lambda: GP(0,1,2,3,4))

    assert KY() == 'KY;'
    assert ky() == 'KY;'
    assert KY(0) == 'KY0;'
    assert KY(0,1) == 'KY0,1;'
    assertTypeError(lambda: KY(0,1,2))
    
    assert NR() == 'NR;'
    assert nr() == 'NR;'
    assertTypeError(lambda: NR(0))
    
    assert OK() == 'OK;'
    assert ok() == 'OK;'
    assertTypeError(lambda: OK(0))

    assert SG() == 'SG;'
    assert sg() == 'SG;'
    assert SG(0) == 'SG0;'
    assertTypeError(lambda: SG(0,1))
    
    assert VS() == 'VS;'
    assert vs() == 'VS;'
    assert VS(0) == 'VS0;'
    assert VS(0,1) == 'VS0,1;'
    assertTypeError(lambda: VS(0,1,2))
    
    assert WD() == 'WD\x03'
    assert wd() == 'WD\x03'
    assert WD('') == 'WD\x03'
    assert WD('abc') == 'WDabc\x03'
    assert WD('abc', '#') == 'WDabc#'
    assertTypeError(lambda: WD(0,1,2))
    assertValueError(lambda: WD('012345678901234567890123456789012'))
    assertValueError(lambda: WD(chr(0)))
    assertValueError(lambda: WD(chr(3)))
    assertValueError(lambda: WD(chr(5)))
    assertValueError(lambda: WD(chr(27)))
    assertValueError(lambda: WD(chr(127)))
    
    # Part III – Special Applications
    # Chapter 11: Digitizing
    
    assert DC() == 'DC;'
    assert dc() == 'DC;'
    assertTypeError(lambda: DC(0))
    
    assert DP() == 'DP;'
    assert dp() == 'DP;'
    assertTypeError(lambda: DP(0))
    
    assert OD() == 'OD;'
    assert od() == 'OD;'
    assertTypeError(lambda: OD(0))
    
    # Chapter 12: Rollfeed Instructions and Long-Axis Printing
    
    assert AF() == 'AF;'
    assert af() == 'AF;'
    assertTypeError(lambda: AF(0))
    
    assert AH() == 'AH;'
    assert ah() == 'AH;'
    assertTypeError(lambda: AH(0))
    
    assert EC() == 'EC;'
    assert ec() == 'EC;'
    assert EC(0) == 'EC0;'
    assertTypeError(lambda: EC(0,1))
    
    assert FR() == 'FR;'
    assert fr() == 'FR;'
    assertTypeError(lambda: FR(0))
    
    assert PG() == 'PG;'
    assert pg() == 'PG;'
    assert PG(0) == 'PG0;'
    assertTypeError(lambda: PG(0,1))
    
    assert PS() == 'PS;'
    assert ps() == 'PS;'
    assert PS(10) == 'PS10;'
    assert PS(10,20) == 'PS10,20;'
    assertTypeError(lambda: PS(0,1,2))
    
    # Chapter 13: Alternate Character Sets and User-Designed Characters
    
    assert CA() == 'CA;'
    assert ca() == 'CA;'
    assert CA(0) == 'CA0;'
    assertTypeError(lambda: CA(0,1))
    
    assert CC() == 'CC;'
    assert cc() == 'CC;'
    assert CC(0) == 'CC0;'
    assertTypeError(lambda: CC(0,1))
    
    assert CM() == 'CM;'
    assert cm() == 'CM;'
    assert CM(0) == 'CM0;'
    assert CM(0,1) == 'CM0,1;'
    assertTypeError(lambda: CM(0,1,2))
    
    assert CS() == 'CS;'
    assert cs() == 'CS;'
    assert CS(0) == 'CS0;'
    assertTypeError(lambda: CS(0,1))

    assert DL() == 'DL;'
    assert dl() == 'DL;'
    assert DL(0) == 'DL0;'
    assert DL(0,1) == 'DL0,1;'
    assert DL(0,1,2) == 'DL0,1,2;'
    assert DL(0,1,2,3) == 'DL0,1,2,3;'
    assert DL(0,1,2,3,4) == 'DL0,1,2,3,4;'
    assert DL(0,-1,2,3,-1,4,5,6,7) == 'DL0,-1,2,3,-1,4,5,6,7;'
    
    assert DS() == 'DS;'
    assert ds() == 'DS;'
    assert DS(0,1) == 'DS0,1;'
    assertTypeError(lambda: DS(0))
    assertTypeError(lambda: DS(0,1,2))
    
    assert IV() == 'IV;'
    assert iv() == 'IV;'
    assert IV(0) == 'IV0;'
    assert IV(0,1) == 'IV0,1;'
    assertTypeError(lambda: IV(0,1,2))

    assert SA() == 'SA;'
    assert sa() == 'SA;'
    assertTypeError(lambda: SA(0))
    
    assert SS() == 'SS;'
    assert ss() == 'SS;'
    assertTypeError(lambda: SS(0))
    
    assert UC() == 'UC;'
    assert uc() == 'UC;'
    assert UC(0) == 'UC0;'
    assert UC(0,1) == 'UC0,1;'
    assert UC(0,1,2) == 'UC0,1,2;'
    assert UC(0,1,2,3) == 'UC0,1,2,3;'
    assert UC(0,1,2,3,4) == 'UC0,1,2,3,4;'
    assert UC(0,-1,2,3,-1,4,5,6,7) == 'UC0,-1,2,3,-1,4,5,6,7;'
    
    # Part IV – Interfacing, Handshaking, Output, and Device Control
    # Chapter 14: Obtaining Information from the Plotter
    
    assert GC() == 'GC;'
    assert gc() == 'GC;'
    assert GC(0) == 'GC0;'
    assertTypeError(lambda: GC(0,1))
    
    assert IM() == 'IM;'
    assert im() == 'IM;'
    assert IM(0) == 'IM0;'
    assert IM(0,1) == 'IM0,1;'
    assert IM(0,1,2) == 'IM0,1,2;'
    assertTypeError(lambda: IM(0,1,2,3))
    
    assert OA() == 'OA;'
    assert oa() == 'OA;'
    assertTypeError(lambda: OA(0))
    
    assert OC() == 'OC;'
    assert oc() == 'OC;'
    assertTypeError(lambda: OC(0))
    
    assert OE() == 'OE;'
    assert oe() == 'OE;'
    assertTypeError(lambda: OE(0))
    
    assert OF() == 'OF;'
    assert of() == 'OF;'
    assertTypeError(lambda: OF(0))
    
    assert OG() == 'OG;'
    assert og() == 'OG;'
    assertTypeError(lambda: OG(0))
    
    assert OI() == 'OI;'
    assert oi() == 'OI;'
    assertTypeError(lambda: OI(0))
    
    assert OL() == 'OL;'
    assert ol() == 'OL;'
    assertTypeError(lambda: OL(0))
    
    assert OO() == 'OO;'
    assert oo() == 'OO;'
    assertTypeError(lambda: OO(0))
    
    assert OS() == 'OS;'
    assert os() == 'OS;'
    assertTypeError(lambda: OS(0))
    
    assert OT() == 'OT;'
    assert ot() == 'OT;'
    assertTypeError(lambda: OT(0))
    
    
    # Chapter 15: Device-Control Instructions
    _esc = chr(27)
    
    assert ESC_A() == f'{_esc}.A'
    assertTypeError(lambda: ESC_A(0))
    
    assert ESC_B() == f'{_esc}.B'
    assertTypeError(lambda: ESC_B(0))
    
    assert ESC_E() == f'{_esc}.E'
    assertTypeError(lambda: ESC_E(0))
    
    assert ESC_J() == f'{_esc}.J'
    assertTypeError(lambda: ESC_J(0))
    
    assert ESC_K() == f'{_esc}.K'
    assertTypeError(lambda: ESC_K(0))
    
    assert ESC_L() == f'{_esc}.L'
    assertTypeError(lambda: ESC_L(0))
    
    assert ESC_O() == f'{_esc}.O'
    assertTypeError(lambda: ESC_O(0))
    
    assert ESC_Q() == f'{_esc}.Q:'
    assert ESC_Q(0) == f'{_esc}.Q0:'
    assert ESC_Q(1) == f'{_esc}.Q1:'
    assertTypeError(lambda: ESC_Q(0,1))
    
    assert ESC_R() == f'{_esc}.R'
    assertTypeError(lambda: ESC_R(0))
    
    assert ESC_S(0) == f'{_esc}.S0:'
    assert ESC_S(1) == f'{_esc}.S1:'
    assertTypeError(lambda: ESC_S())
    assertTypeError(lambda: ESC_S(0,1))
    
    assert ESC_T() == f'{_esc}.T;;;0;;:'
    assert ESC_T(1) == f'{_esc}.T1;;;0;;:'
    assert ESC_T(1,2) == f'{_esc}.T1;2;;0;;:'
    assert ESC_T(1,2,3) == f'{_esc}.T1;2;3;0;;:'
    assert ESC_T(1,2,3,4) == f'{_esc}.T1;2;3;0;4;:'
    assert ESC_T(1,2,3,4,5) == f'{_esc}.T1;2;3;0;4;5:'
    assert ESC_T(physical_io_buffer=1) == f'{_esc}.T1;;;0;;:'
    assert ESC_T(polygon_buffer=1) == f'{_esc}.T;1;;0;;:'
    assert ESC_T(downloadable_character_buffer=1) == f'{_esc}.T;;1;0;;:'
    assert ESC_T(vector_buffer=1) == f'{_esc}.T;;;0;1;:'
    assert ESC_T(pen_sort_buffer=1) == f'{_esc}.T;;;0;;1:'
    assertTypeError(lambda: ESC_T(0,1,2,3,4,5))
    
    assert ESC_U() == f'{_esc}.U'
    assertTypeError(lambda: ESC_U(0))
    
    assert ESC_Y() == f'{_esc}.Y'
    assertTypeError(lambda: ESC_Y(0))
    
    assert ESC_Z() == f'{_esc}.Z'
    assertTypeError(lambda: ESC_Z(0))
    
    assert ESC_AT() == f'{_esc}.@;:'
    assert ESC_AT(1) == f'{_esc}.@1;:'
    assert ESC_AT(1,2) == f'{_esc}.@1;2:'
    assert ESC_AT(logical_io_buffer_size=1) == f'{_esc}.@1;:'
    assert ESC_AT(io_conditions=1) == f'{_esc}.@;1:'
    assertTypeError(lambda: ESC_AT(1,2,3))
    
    # Chapter 15: Device-Control Instructions
    
    assert ESC_H() == f'{_esc}.H:'
    assert ESC_H(1) == f'{_esc}.H1;;:'
    assert ESC_H(1,2) == f'{_esc}.H1;2;:'
    assert ESC_H(1,2,3) == f'{_esc}.H1;2;3:'
    assert ESC_H(data_block_size=1) == f'{_esc}.H1;;:'
    assert ESC_H(enquiry_character=1) == f'{_esc}.H;1;:'
    assert ESC_H(acknowledgement_string=1) == f'{_esc}.H;;1:'
    assertTypeError(lambda: ESC_H(1,2,3,4))
    
    assert ESC_I() == f'{_esc}.I;;:'
    assert ESC_I(1) == f'{_esc}.I1;;:'
    assert ESC_I(1,2) == f'{_esc}.I1;2;:'
    assert ESC_I(1,2,3) == f'{_esc}.I1;2;3:'
    assert ESC_I(xoff_threshold_level_or_data_block_size=1) == f'{_esc}.I1;;:'
    assert ESC_I(omitted_or_enquiry_character=1) == f'{_esc}.I;1;:'
    assert ESC_I(xon_trigger_characters_or_acknowledgement_string=1) == f'{_esc}.I;;1:'
    assertTypeError(lambda: ESC_I(1,2,3,4))
    
    assert ESC_M() == f'{_esc}.M;;;;:'
    assert ESC_M(1) == f'{_esc}.M1;;;;:'
    assert ESC_M(1,2) == f'{_esc}.M1;2;;;:'
    assert ESC_M(1,2,3) == f'{_esc}.M1;2;3;;:'
    assert ESC_M(1,2,3,4) == f'{_esc}.M1;2;3;4;:'
    assert ESC_M(turnaround_delay=1) == f'{_esc}.M1;;;;:'
    assert ESC_M(output_trigger=1) == f'{_esc}.M;1;;;:'
    assert ESC_M(echo_terminator=1) == f'{_esc}.M;;1;;:'
    assert ESC_M(output_terminator=1) == f'{_esc}.M;;;1;:'
    assert ESC_M(output_initiator=1) == f'{_esc}.M;;;;1:'
    assert ESC_M(1,2,3,4,5) == f'{_esc}.M1;2;3;4;5:'
    assertTypeError(lambda: ESC_M(1,2,3,4,5,6))
    
    assert ESC_N() == f'{_esc}.N;:'
    assert ESC_N(1) == f'{_esc}.N1;:'
    assert ESC_N(1,2) == f'{_esc}.N1;2:'
    assert ESC_N(intercharacter_delay=1) == f'{_esc}.N1;:'
    assert ESC_N(handshake_dependent_parameter=1) == f'{_esc}.N;1:'
    assertTypeError(lambda: ESC_N(1,2,3))
    
    assert ESC_P() == f'{_esc}.P:'
    assert ESC_P(1) == f'{_esc}.P1:'
    assertTypeError(lambda: ESC_P(1,2))
    