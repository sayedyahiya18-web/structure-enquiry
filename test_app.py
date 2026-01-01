from app import apply_leave

def test_apply_leave():
    result = apply_leave("John", "E101", "Sick", 3)

    assert result["employee_name"] == "John"
    assert result["employee_id"] == "E101"
    assert result["leave_type"] == "Sick"
    assert result["days"] == 3