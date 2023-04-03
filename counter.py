import openai
from flask import Flask
import monitor  # Import the module
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
import urllib
import os

from opentelemetry import trace
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.requests import RequestsInstrumentor


# Service name is required for most backends
resource = Resource(attributes={
    SERVICE_NAME: "your-service-name"
})

provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(OTLPSpanExporter(endpoint=os.getenv('OTEL_EXPORTER_OTLP_ENDPOINT'),
        headers="Authorization=Bearer%20"+os.getenv('OTEL_EXPORTER_OTLP_AUTH_HEADER')))

provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)
RequestsInstrumentor().instrument()



# Initialize Flask app and instrument it
app = Flask(__name__)

# Set OpenAI API key
openai.api_key = os.getenv('OPEN_AI_KEY')

@app.route("/completion")
@tracer.start_as_current_span("do_work")
def completion():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Why is Elastic an amazing observability tool?",
        max_tokens=20,
        temperature=0
    )

    return response.choices[0].text.strip()

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)

