from financial_analyst_crew.crew import FinancialAnalystCrew

def run():
    inputs={
        'company_name':'Tesla',
    }
    FinancialAnalystCrew().crew().kickoff(inputs=inputs)
if __name__ == "__main__":
    run()