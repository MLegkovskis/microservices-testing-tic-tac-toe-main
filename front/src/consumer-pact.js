
const { Pact, Matchers } = require('@pact-foundation/pact');

// Create a new Pact object
const pact = new Pact({
  consumer: 'FrontendService',
  provider: 'BackendService',
  port: 1234, // Port where the mock service will be running
});

// Define the interaction for the /number endpoint
pact.addInteraction({
  uponReceiving: 'a request for a random number',
  withRequest: {
    method: 'GET',
    path: '/number',
  },
  willRespondWith: {
    status: 200,
    body: Matchers.term({
      matcher: '\\d', // Expecting a single digit as a response
      generate: '5', // Example response
    }),
  },
});

// Generate the Pact contract file
pact.finalize();
