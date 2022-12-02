import pandas as pd
class FundingRaised:

  @staticmethod
  def filter(options):
    df = pd.read_csv("../startup_funding.csv",dtype={'number_employees':'string','raised_amount':'string'})
    for option in options.keys():
      df = df[df[option]==options[option]]
    return df.to_dict(orient='records')

  @staticmethod
  def where(options = {}):
    return FundingRaised.filter(options)
   
  @staticmethod
  def find_by(options):
    if len(FundingRaised.filter(options))!=0:
      return FundingRaised.filter(options)[0]
    raise RecordNotFound

class RecordNotFound(Exception):
  pass

if __name__ == "__main__":
    print(FundingRaised.where({'company_name': 'Facebook'}))
    print("___________________________________________________")
    print(FundingRaised.find_by({'company_name': 'Facebook'}))