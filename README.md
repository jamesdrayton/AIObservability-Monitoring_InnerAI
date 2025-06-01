# AIObservability-Monitoring_InnerAI


Project Name: **AI Observability & Monitoring**

Group Name: **Inner AI**

Main Participant Name: **James Drayton Beninger**

Team Participant Names:

Amogh Thoutu, Farhan Mahamud, Shubhangi Singh, Bardia Azami

------------------------------------------------------- -

AWS Codes:

James Drayton Beninger: XXXXXXXXXXX 

Amogh Thoutu: XXXXXXXXXXX 

Farhan Mahamud : XXXXXXXXXXX 

Shubhangi Singh : XXXXXXXXXXX 

Bardia Azami : XXXXXXXXXXX 

Track 2: AI Observability & Monitoring</br>
● Theme: Build observability for a deployed GenAI application.
Project Idea:
o Create a monitoring system for a deployed GenAI API (e.g., chatbot or image
generator):
○ Track latency, token usage, user satisfaction (via feedback collection)
○ Detect hallucinations or toxic outputs using classifiers
○ Visualize outputs and anomalies via Grafana dashboards
○ Generate alerts for performance degradation or safety violations
Suggested Tools: Prometheus, Grafana, OpenTelemetry, FastAPI, Langfuse,
Arize AI
Project purpose and Target audience:
Purpose: Create a middleware solution which can integrate into target audience apps (requiring developer access)
Audience: Text-based GenAI applications. Anything that includes sending a text prompt to an LLM and which receives text back (can reduce scope if this is too much)

Project Design
    Integration
        API call wrappers? 
    Metrics 
        Latency
        Token Usage
        Hallucinations
        Model or Logic Drift
        Reasoning steps or state representations (optional, Anthropic paper or prolog)
	Testing
        Simulated users
        Application load analysis (sampling?)

	Visualizations and performance/safety alerts
        Grafana
        Scripts to sample and flag when metrics reach a threshold
        Contradiction flags (if using prolog, we can flag contradictions or failures to run)

