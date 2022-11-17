import currency

def test_convert():
    assert currency.convert(1,1) == 1
    assert currency.convert(1,10) == 10
    assert currency.convert(1,0.1) == 0.1
    assert currency.convert(5,1) == 5
    assert currency.convert(5,10) == 50
    assert currency.convert(5,0.1) == 0.5
    
    
