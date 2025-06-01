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
● Theme: Build observability for a deployed GenAI application.</br>
Project Idea:</br>
o Create a monitoring system for a deployed GenAI API (e.g., chatbot or image
generator):</br>
○ Track latency, token usage, user satisfaction (via feedback collection)</br>
○ Detect hallucinations or toxic outputs using classifiers</br>
○ Visualize outputs and anomalies via Grafana dashboards</br>
○ Generate alerts for performance degradation or safety violations</br>
Suggested Tools: Prometheus, Grafana, OpenTelemetry, FastAPI, Langfuse,</br>
Arize AI</br>
Project purpose and Target audience:</br>
Purpose: Create a middleware solution which can integrate into target audience apps (requiring developer access)</br>
Audience: Text-based GenAI applications. Anything that includes sending a text prompt to an LLM and which receives text back (can reduce scope if this is too much)</br>

Project Design</br>
    Integration</br>
        API call wrappers? </br>
    Metrics </br>
        Latency</br>
        Token Usage</br>
        Hallucinations</br>
        Model or Logic Drift</br>
        Reasoning steps or state representations (optional, Anthropic paper or prolog)</br>
	Testing</br>
        Simulated users</br>
        Application load analysis (sampling?)</br>

	Visualizations and performance/safety alerts</br>
        Grafana</br>
        Scripts to sample and flag when metrics reach a threshold</br>
        Contradiction flags (if using prolog, we can flag contradictions or failures to run)</br>

