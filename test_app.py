import alerts

def test_alert_poll(): #placeholder unit test
    assert alerts.poll_vitals(130, (164,80), 97) == "Pulse is abnormally high; Blood pressure is abnormally high"
    assert alerts.poll_vitals(130, (164,80), 93) == "Pulse is abnormally high; Blood pressure is abnormally high; Blood oxygen is abnormally low"
    assert alerts.poll_vitals(70, (120,80), 98) == ""
    assert alerts.poll_vitals(70, (120,80), 91) == "Blood oxygen is abnormally low"
    assert alerts.poll_vitals(70, (80,60), 98) == "Blood pressure is abnormally low"

if __name__ == "__main__":
    test_alert_poll()
    