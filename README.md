# Monitor OpenAI API and GPT Models with OpenTelemetry and Elastic

ChatGPT is a powerful AI language model developed by OpenAI. As the use of ChatGPT-based solutions grows, developers need to monitor the performance and costs of these applications. This README demonstrates how to use OpenTelemetry and Elastic to monitor ChatGPT applications.

## OpenAI API and Cost Monitoring

The OpenAI API returns token counts and other useful information in each API response. This data can be used to calculate the cost of each API call based on OpenAI's pricing.

## OpenTelemetry

OpenTelemetry is a powerful and widely adopted observability tool that can be used to monitor ChatGPT applications. This example uses Flask, ChatGPT API, and OpenTelemetry to instrument external calls and monitor the performance of OpenAI API calls.

## Setup

1. Set up an Elastic Cloud Account and create a deployment.
2. Install the required Python libraries.

 - pip3 install opentelemetry-api
 - pip3 install opentelemetry-sdk
 - pip3 install opentelemetry-exporter-otlp
 - pip3 install opentelemetry-instrumentation
 - pip3 install opentelemetry-instrumentation-requests
 - pip3 install openai
 - pip3 install flask

4. Replace the environment variables below with your own values.

- export OPEN_AI_KEY=sk-abcdefgh5ijk2l173mnop3qrstuvwxyzab2cde47fP2g9jij
- export OTEL_EXPORTER_OTLP_AUTH_HEADER=abc9ldeofghij3klmn
- export OTEL_EXPORTER_OTLP_ENDPOINT=https://123456abcdef.apm.us-west2.gcp.elastic-cloud.com:443

5. Check out the example Python application.

## Example Application

The example application demonstrates how to use OpenTelemetry to instrument a Flask application that makes ChatGPT API calls. The magic happens inside the `monitor` code that you can use freely to instrument your OpenAI code.

## Monkey Patching

Monkey patching is used to modify the behavior of the `Completion` call at runtime so that the response metrics can be captured and sent to the OpenTelemetry OTLP endpoint (in this case, Elastic).

## Cost Calculation

The `calculate_cost` function calculates the cost of a single request to the OpenAI APIs based on the token counts and the model used.

## Elastic

Once the data is captured, it can be visualized and analyzed in Elastic. You can use the captured data to build dashboards, monitor transactions and latency, and assess the performance of your ChatGPT service.

