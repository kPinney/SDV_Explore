from src.constraints import get_constraints

def test_get_constraints():
    """
    Tests that get_constraints returns a list.
    """
    constraints = get_constraints()
    assert isinstance(constraints, list)
