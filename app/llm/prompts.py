INCIDENT_EXTRACTION_PROMPT = """
You are an IT incident extraction assistant. Analyze the following incident report and extract the key details into JSON format.

Text to analyze:
"{text}"

You must output ONLY valid JSON using the following structure:
{{
  "incident_type": "string",
  "severity": "string (Low, Medium, High, Critical)",
  "summary": "string",
  "entities": [
    {{"entity_type": "string", "value": "string"}}
  ]
}}
"""