from src.pipeline import build_context

docs = [
    "The data retention policy requires customer records to be retained for seven years.",
    "Production access must be approved by the data owner and reviewed quarterly.",
    "Incident response requires notification within the defined severity SLA."
]
result = build_context("How long are customer records retained?", docs)
print(result)
