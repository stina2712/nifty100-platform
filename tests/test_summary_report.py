from src.analytics.summary_report import generate_company_summary

def test_generate_company_summary():
    # Provide dummy data
    dummy_data = {
        'borrowings': 100, 'equity': 100, 'reserves': 50,
        'op_profit': 20, 'other_income': 5, 'interest': 5,
        'sales': 500, 'total_assets': 1000,
        'start_val': 100, 'end_val': 200, 'years': 5,
        'cfo': 100, 'cfi': -50, 'cff': -20,
        'cfo_sum': 100, 'pat_sum': 100
    }
    
    result = generate_company_summary(dummy_data)
    
    # Assert expected keys exist
    assert "de_ratio" in result
    assert result["allocation_pattern"] == "Mature / Dividend Payer"
    print("Integration successful!")