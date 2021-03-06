from sql.parse import parse

def test_parse_no_sql():
    assert parse("will:longliveliz@localhost/shakes") == \
           {'connection': "will:longliveliz@localhost/shakes",
            'sql': ''}
    
def test_parse_with_sql():
    assert parse("will:longliveliz@localhost/shakes SELECT * FROM work") == \
           {'connection': "will:longliveliz@localhost/shakes",
            'sql': 'SELECT * FROM work'}    
    
def test_parse_sql_only():
    assert parse("SELECT * FROM work") == \
           {'connection': "",
            'sql': 'SELECT * FROM work'} 