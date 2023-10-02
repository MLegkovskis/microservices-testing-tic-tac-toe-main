
from pact import Verifier

def verify_pact():
    # Assume that the Flask app is running locally on port 5000
    provider_base_url = 'http://localhost:5000'
    
    # Create a Verifier object
    verifier = Verifier(provider='BackendService', provider_base_url=provider_base_url)
    
    # Specify the path to the Pact file generated by the consumer
    pact_file_path = './pacts/FrontendService-BackendService.json'
    
    # Verify the contract
    verifier.verify_pact(pact_file_path)
    verifier.finalize()

if __name__ == "__main__":
    verify_pact()
